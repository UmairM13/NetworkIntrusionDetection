import os
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import RandomizedSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

def train_and_evaluate_model(X_train, y_train, X_test, y_test, pipeline):
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Move one directory up from the script location (to the backend folder)
    backend_dir = os.path.abspath(os.path.join(script_dir, '..'))

    # Define the models directory within the backend directory
    models_dir = os.path.join(backend_dir, 'models')
    
    # Create models directory if it doesn't exist
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)

    # Define the models and their hyperparameters
    models = {
        'Random Forest': (RandomForestClassifier(), {
            'classifier__n_estimators': [10, 50],  # Reduced number of estimators
            'classifier__max_depth': [None, 10],   # Simplified hyperparameters
            'classifier__min_samples_split': [2, 5],
        }),
        'KNN': (KNeighborsClassifier(), {
            'classifier__n_neighbors': [3],    # Reduced range and single value
            'classifier__weights': ['uniform'],  # Simplified weights
        }),
        'SVM': (SGDClassifier(loss='hinge'), {  # Using SGDClassifier
            'classifier__alpha': [0.0001, 0.001],
            'classifier__max_iter': [1000],   # Reduced iterations
        })
    }

    for model_name, (model, params) in models.items():
        # Set the classifier in the pipeline
        pipeline.set_params(classifier=model)

        # Reduce cross-validation folds for KNN
        cv_folds = 2 if model_name == 'KNN' else 3

        # Use RandomizedSearchCV with fewer iterations and lower folds
        grid_search = RandomizedSearchCV(pipeline, params, n_iter=5, cv=cv_folds, scoring='accuracy', n_jobs=-1, verbose=1)
        
        try:
            grid_search.fit(X_train, y_train)
        except Exception as e:
            print(f"An error occurred while fitting the model '{model_name}': {e}")
            continue  # Skip to the next model if there's an error

        print(f"Best parameters for {model_name}: {grid_search.best_params_}")
        print(f"Best cross-validation score for {model_name}: {grid_search.best_score_:.2f}")

        # Make predictions and evaluate
        if y_test is not None:
            y_pred = grid_search.predict(X_test)
            print(f"Confusion Matrix for {model_name}:\n{confusion_matrix(y_test, y_pred)}")
            print(f"Classification Report for {model_name}:\n{classification_report(y_test, y_pred)}\n")

        # Save the best model
        model_file_path = os.path.join(models_dir, f'{model_name.lower().replace(" ", "_")}_model.joblib')
        joblib.dump(grid_search.best_estimator_, model_file_path)
        print(f"Best model '{model_name}' saved as '{model_file_path}'")
