import pytest
from google.cloud import bigquery

# Replace with your service account key path
SERVICE_ACCOUNT_KEY_PATH = '/home/cris/dataScience/workspace/process_ETL/Scripts/high-gecko-351218-31077ba76204.json'

@pytest.fixture
def bq_client():
    return bigquery.Client.from_service_account_json(SERVICE_ACCOUNT_KEY_PATH)

@pytest.fixture
def test_dataset(bq_client):
    # Create a test dataset for the tests
    dataset_id = 'test_dataset'
    dataset_ref = bq_client.create_dataset(dataset_id)
    yield dataset_ref
    bq_client.delete_dataset(dataset_ref, delete_contents=True, not_found_ok=True)

@pytest.fixture
def test_table(bq_client, test_dataset):
    # Create a test table for the tests
    table_id = 'test_table'
    table_ref = test_dataset.table(table_id)
    schema = [
        bigquery.SchemaField('column1', 'INTEGER', mode='NULLABLE' ),
        bigquery.SchemaField('column2', 'string', mode='NULLABLE' ),
        # Add more schema fields as needed
    ]
    table = bigquery.Table(table_ref, schema=schema)
    bq_client.create_table(table)
    yield table_ref
    bq_client.delete_table(table_ref, not_found_ok=True)

def test_load_to_bigquery(bq_client, test_table):
    # Your data (a DataFrame) to be loaded
    # Replace this with your actual DataFrame to be loaded
    data = [
        (1, 'Row 1'),
        (2, 'Row 2'),
        # Add more data rows as needed
    ]
    columns = ['column1', 'column2']  # Adjust column names based on your schema

    schema = [
        bigquery.SchemaField('column1', 'INTEGER', mode='NULLABLE' ),
        bigquery.SchemaField('column2', 'string', mode='NULLABLE' ),
        # Add more schema fields as needed
    ]

    # Convert the data to DataFrame (using Pandas for example)
    import pandas as pd
    df = pd.DataFrame(data, columns=columns)

    # Load data into BigQuery
    job_config = bigquery.LoadJobConfig(schema= schema, write_disposition='WRITE_TRUNCATE')
    job = bq_client.load_table_from_dataframe(df, test_table, job_config=job_config)

    # Wait for the job to complete
    job.result()

    # Verify the table has been loaded
    loaded_table = bq_client.get_table(test_table)
    assert loaded_table.num_rows == len(data)
