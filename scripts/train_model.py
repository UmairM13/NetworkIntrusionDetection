import os
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import RandomizedSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

def train_and_evaluate_model(X_train, y_train, X_test, y_test, pipeline):
    # Create models directory if it doesn't exist
    if not os.path.exists('models'):
        os.makedirs('models')

    # Define the models and their hyperparameters
    models = {
        'Random Forest': (RandomForestClassifier(), {
            'classifier__n_estimators': [10, 20],  # Start with fewer estimators
            'classifier__max_depth': [None, 5],
        }),
        'KNN': (KNeighborsClassifier(), {
            'classifier__n_neighbors': [3],  # Reduce neighbors
            'classifier__weights': ['uniform'],
        }),
        'SVM': (SGDClassifier(loss='hinge'), {  # Using SGDClassifier
            'classifier__alpha': [0.0001],
            'classifier__max_iter': [1000],
        })
    }

    for model_name, (model, params) in models.items():
        # Set the classifier in the pipeline
        pipeline.set_params(classifier=model)

        # Use RandomizedSearchCV with fewer iterations, lower folds, and less verbosity
        grid_search = RandomizedSearchCV(pipeline, params, n_iter=2, cv=2, scoring='accuracy', n_jobs=1, verbose=0)
        
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
        model_file_path = os.path.join('models', f'{model_name.lower().replace(" ", "_")}_model.joblib')
        joblib.dump(grid_search.best_estimator_, model_file_path)
        print(f"Best model '{model_name}' saved as '{model_file_path}'")
