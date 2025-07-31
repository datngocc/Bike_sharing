from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os
import subprocess

default_args = {
    'owner': 'datnguyen',
    'depends_on_past': False,
    'start_date': datetime(2025, 7, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

dag = DAG(
    'bike_hour_pipeline',
    default_args=default_args,
    description='ETL pipeline for bike sharing - hour data',
    schedule_interval='@daily',
    catchup=False       
)

def clean_hour_data():
    # Gọi script hour_clean.py (đúng tên file, đúng đường dẫn)
    subprocess.run(['python', os.path.join(os.getcwd(), 'cleaning', 'hour_clean.py')], check=True)

clean_task = PythonOperator(
    task_id='clean_hour_data',
    python_callable=clean_hour_data,
    dag=dag
)