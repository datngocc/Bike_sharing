from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess
import os

default_args = {
    'owner': 'datnguyen',
    'start_date': datetime(2025, 7, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'clean_hour_data',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description='Clean hour.csv to hour_clean.csv'
)

def clean_hour():
    subprocess.run(['python', '/opt/airflow/dags/cleaning/hour_clean.py'], check=True)

task = PythonOperator(
    task_id='run_clean_hour',
    python_callable=clean_hour,
    dag=dag
)
