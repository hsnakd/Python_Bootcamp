import pandas as pd

# Define Excel file paths
excel_file_path_write = 'files/test_write.xlsx'
excel_file_path_read = 'files/test_write.xlsx'

# Creating a DataFrame
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [28, 24, 22],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

# Writing to Excel file
df.to_excel(excel_file_path_write, index=False)

# Reading from Excel file
read_df = pd.read_excel(excel_file_path_read, engine='openpyxl')

# Display the DataFrames
print("Original DataFrame:")
print(df)
# Output:
        #     Name  Age         City
        # 0   John   28     New York
        # 1  Alice   24  Los Angeles
        # 2    Bob   22      Chicago


print("\nDataFrame read from Excel:")
print(read_df)
# Output:
        #     Name  Age         City
        # 0   John   28     New York
        # 1  Alice   24  Los Angeles
        # 2    Bob   22      Chicago