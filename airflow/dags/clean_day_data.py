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
    'clean_day_data',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description='Clean day.csv to day_clean.csv'
)

def clean_day():
    script_path = os.path.join(os.getcwd(),'dags', 'cleaning', 'day_clean.py')
    subprocess.run(['python', script_path], check=True)

task = PythonOperator(
    task_id='run_clean_day',
    python_callable=clean_day,
    dag=dag
)