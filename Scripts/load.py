from google.cloud import bigquery
from transform import transform_data_with_pandas

def load_to_bigquery():
    # Authenticate using a service account key file
    # Replace 'path/to/service_account_key.json' with your service account key path
    client = bigquery.Client.from_service_account_json('/home/cris/dataScience/workspace/process_ETL/Scripts/high-gecko-351218-31077ba76204.json')

    # Your GCP project ID
    project_id = 'high-gecko-351218'

    # Your BigQuery dataset ID and table name

    dataset_id = 'process_ETL'
    table_name = 'Load_demo'

    

    # Get the transformed data
    df = transform_data_with_pandas()
    
    
    if df is not None:
        # Create a BigQuery dataset reference
        dataset_ref = client.dataset(dataset_id)

        # Create a job config with the schema (adjust this according to your data)
        job_config = bigquery.LoadJobConfig(
            schema=[
                bigquery.SchemaField('userId', 'INTEGER'),
                bigquery.SchemaField('title', 'STRING'),
                bigquery.SchemaField('body', 'STRING')
                # Add more schema fields as needed
            ],
            write_disposition='WRITE_TRUNCATE',  # Options: WRITE_TRUNCATE, WRITE_APPEND, WRITE_EMPTY
        )

        # Load data into BigQuery
        table_ref = dataset_ref.table(table_name)
        job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)

        # Wait for the job to complete
        job.result()
        print(f'Data loaded into BigQuery table {project_id}.{dataset_id}.{table_name} successfully.')

if __name__ == "__main__":
    load_to_bigquery()
