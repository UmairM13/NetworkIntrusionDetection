import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from scripts.data_processing import load_data, split_data
from scripts.train_model import train_and_evaluate_model  # Import the function
import warnings

warnings.filterwarnings("ignore")

def main():
    train_file_path = './data/Train_data.csv'  # Adjust your path
    test_file_path = './data/Test_data.csv'    # Adjust your path

    # Load the training and test data
    train_data, test_data = load_data(train_file_path, test_file_path)

    # Print the loaded data
    print("Train Data:")
    print(train_data.head())
    print("Test Data:")
    print(test_data.head())

    target_column = 'class'
    X_train, y_train = split_data(train_data, target_column)

    if target_column not in test_data.columns:
        print(f"Warning: '{target_column}' not found in test data. Creating placeholder.")
        test_data[target_column] = np.nan

    X_test = test_data.drop(columns=[target_column], errors='ignore')

    categorical_cols = X_train.select_dtypes(include=['object']).columns.tolist()

    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
        ],
        remainder='passthrough'
    )

    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier())  # Start with one model
    ])

    try:
        train_and_evaluate_model(X_train, y_train, X_test, None, pipeline)
        # You can use the pipeline after training to make predictions
        predictions = pipeline.predict(X_test)
        print("Predictions on test data:")
        print(predictions)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
