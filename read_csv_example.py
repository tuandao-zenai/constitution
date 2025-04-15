import pandas as pd
import csv

# Method 1: Using pandas (recommended for most cases)
def read_with_pandas():
    # Read the CSV file into a DataFrame
    df = pd.read_csv('sample_data.csv')
    print("\nMethod 1: Using pandas")
    print(df)
    print("\nData types:")
    print(df.dtypes)

# Method 2: Using the built-in csv module
def read_with_csv():
    print("\nMethod 2: Using csv module")
    with open('sample_data.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)

def read_csv_to_dict():
    data = []
    with open('sample_data.csv', 'r') as file:
        # Create a DictReader object
        csv_reader = csv.DictReader(file)
        # Convert each row to a dictionary and add to the list
        for row in csv_reader:
            data.append(dict(row))
    
    print("\nCSV data as list of dictionaries:")
    for item in data:
        print(item)
    
    return data

if __name__ == "__main__":
    read_with_pandas()
    read_with_csv()
    result = read_csv_to_dict() 