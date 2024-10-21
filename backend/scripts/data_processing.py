import pandas as pd


def load_data(train_file_path, test_file_path):
    # Load training data
    train_data = pd.read_csv(train_file_path)
    # Load test data
    test_data = pd.read_csv(test_file_path)
    
    return train_data, test_data

def split_data(data, target_column):
    # Check if target_column is in the DataFrame
    if target_column not in data.columns:
        raise KeyError(f"{target_column} not found in DataFrame columns: {data.columns.tolist()}")
    
    # Split features and target variable
    X = data.drop(columns=[target_column])
    y = data[target_column]
    return X, y

