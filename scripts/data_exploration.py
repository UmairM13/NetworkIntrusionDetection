import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def check_class_balance(data, target_column):
    if target_column in data.columns:
        class_counts = data[target_column].value_counts()
        print("Class distribution:\n", class_counts)

        plt.figure(figsize=(8, 6))
        class_counts.plot(kind='bar', color=['skyblue', 'orange'])
        plt.title("Class Balance: Attack (1) vs. Normal (0)")
        plt.xlabel("Class")
        plt.ylabel("Frequency") 
        plt.xticks(rotation=0)
        plt.show()
    else:
        print(f"Error: '{target_column}' column does not exist in the DataFrame.")

def plot_histograms(data):
    data.hist(figsize=(20, 20), bins=20, color='skyblue', edgecolor='black')
    plt.suptitle("Feature Distributions", fontsize=16)
    plt.show()

def plot_correlations(data):
    plt.figure(figsize=(12, 10))
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title("Feature Correlation Matrix")
    plt.show()

def plot_boxplots(data, target_column):
    plt.figure(figsize=(12, 6))
    numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
    for col in numerical_columns:
        plt.subplot(4, 4, numerical_columns.index(col) + 1)
        sns.boxplot(x=target_column, y=col, data=data)
        plt.title(f'Boxplot of {col} by {target_column}')
    plt.tight_layout()
    plt.show()

def main():
    train_data_path = r'data\cleaned_data.csv'
    train_data = pd.read_csv(train_data_path)
    
    # Check column names
    print("Columns in the DataFrame:", train_data.columns.tolist())

    # Update the target_column to the correct name based on your dataset
    target_column = 'label'  # Change 'label' if necessary
    check_class_balance(train_data, target_column)
    plot_histograms(train_data)
    plot_correlations(train_data)
    plot_boxplots(train_data, target_column)

if __name__ == '__main__':
    main()
