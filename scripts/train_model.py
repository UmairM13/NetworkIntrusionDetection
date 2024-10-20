from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score

def train_and_evaluate_model(X_train, y_train, X_test, y_test, pipeline):
    # Start with a single model for faster debugging
    models = {
        'Random Forest': RandomForestClassifier(),
        'SVM': SVC(),
        'KNN': KNeighborsClassifier()
    }

    for model_name, model in models.items():
        # Use the pipeline for model training
        pipeline.set_params(classifier=model)

        # Fit the model
        pipeline.fit(X_train, y_train)

        # Evaluate the model using a reduced cross-validation
        cv_scores = cross_val_score(pipeline, X_train, y_train, cv=3)  # Changed from 5 to 3
        print(f"Model: {model_name} CV accuracy: {cv_scores.mean():.2f} +/- {cv_scores.std():.2f}")

        # Make predictions
        if y_test is not None:
            y_pred = pipeline.predict(X_test)

            # Print the evaluation metrics
            print(f"Confusion Matrix for {model_name}:\n{confusion_matrix(y_test, y_pred)}")
            print(f"Classification Report for {model_name}:\n{classification_report(y_test, y_pred)}")
            print("\n")
