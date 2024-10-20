import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os


def load_data(file_path):

    columns = [
        'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 
        'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 
        'root_shell', 'su_attempted', 'num_root', 'num_file_creations', 'num_shells', 
        'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login', 'count', 
        'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 
        'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 
        'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 
        'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 
        'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate'
    ]

    dtypes = {
        'duration': 'int64', 'protocol_type': 'object', 'service': 'object', 'flag': 'object',
        'src_bytes': 'int64', 'dst_bytes': 'int64', 'land': 'int64', 'wrong_fragment': 'int64',
        'urgent': 'int64', 'hot': 'int64', 'num_failed_logins': 'int64', 'logged_in': 'int64',
        'num_compromised': 'int64', 'root_shell': 'int64', 'su_attempted': 'int64',
        'num_root': 'int64', 'num_file_creations': 'int64', 'num_shells': 'int64',
        'num_access_files': 'int64', 'num_outbound_cmds': 'int64', 'is_host_login': 'int64',
        'is_guest_login': 'int64', 'count': 'int64', 'srv_count': 'int64',
        'serror_rate': 'float64', 'srv_serror_rate': 'float64', 'rerror_rate': 'float64',
        'srv_rerror_rate': 'float64', 'same_srv_rate': 'float64', 'diff_srv_rate': 'float64',
        'srv_diff_host_rate': 'float64', 'dst_host_count': 'int64', 'dst_host_srv_count': 'int64',
        'dst_host_same_srv_rate': 'float64', 'dst_host_diff_srv_rate': 'float64',
        'dst_host_same_src_port_rate': 'float64', 'dst_host_srv_diff_host_rate': 'float64',
        'dst_host_serror_rate': 'float64', 'dst_host_srv_serror_rate': 'float64',
        'dst_host_rerror_rate': 'float64', 'dst_host_srv_rerror_rate': 'float64'
    }

    data = pd.read_csv(file_path, header=0, names=columns, dtype=dtypes)

    return data


def preprocess_data(data):

    data = data.dropna()

    categorical_columns = ['protocol_type', 'service', 'flag']
    le = LabelEncoder()

    for col in categorical_columns:
        data[col] = le.fit_transform(data[col])

    numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
    scaler = StandardScaler()
    data[numerical_columns] = scaler.fit_transform(data[numerical_columns])

    return data


def save_cleaned_data(data, file_path):

    cleaned_file_path = os.path.join(file_path, 'cleaned_data.csv')
    data.to_csv(cleaned_file_path, index=False)
    print(f'Cleaned data saved to {cleaned_file_path}')


def main(): 
    train_data_path = r'data\Test_data.csv'
    train_data = load_data(train_data_path)

    cleaned_train_data = preprocess_data(train_data)

    save_cleaned_data(cleaned_train_data, './data')


if __name__ == '__main__':
    main()
