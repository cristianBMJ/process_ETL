import pandas as pd
from extract  import extract_data_from_dummy_api

def transform_data_with_pandas():
    extracted_data = extract_data_from_dummy_api()

    if extracted_data:
        # Creating a DataFrame from the extracted data
        df = pd.DataFrame(extracted_data)

        # Dropping duplicates based on 'id' column (assuming 'id' is present in the data)
        df.drop_duplicates(subset='id', inplace=True)

        # Handling missing values, replacing NaN values with an empty string in 'title' column
        df['title'].fillna('', inplace=True)

        # Transforming 'title' column to uppercase
        df['title'] = df['title'].str.upper()

        # Displaying the transformed data
        print("Transformed Data:")
        print(df.head())  # Displaying the first few rows of the DataFrame

        # Returning the transformed data
        return df

    else:
        print("No data extracted.")
        return None

if __name__ == "__main__":
    transform_data_with_pandas()
