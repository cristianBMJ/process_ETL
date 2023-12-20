from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from google.cloud import bigquery

from load import load_to_bigquery
from transform  import transform_data_with_pandas
from extract  import extract_data_from_dummy_api



# Define a function to load data into BigQuery
#def load_to_bigquery():
    # Your code to load data to BigQuery

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 12, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('ETL_DAG', default_args=default_args, description='ETL process DAG', schedule_interval='@daily')

# Define tasks in the DAG using PythonOperator
extract_task = PythonOperator(
    task_id='extract_data',
    python_callable= extract_data_from_dummy_api,  # Function to extract data
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data_with_pandas,  # Function to transform data
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_to_bigquery',
    python_callable=load_to_bigquery,  # Function to load data into BigQuery
    dag=dag,
)

# Define task dependencies
extract_task >> transform_task >> load_task
