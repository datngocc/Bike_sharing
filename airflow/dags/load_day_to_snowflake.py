from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from datetime import datetime

default_args = {
    'owner': 'datnguyen',
    'start_date': datetime(2025, 7, 1),
}

dag = DAG(
    'load_day_to_snowflake',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description='Load day_clean.csv to Snowflake'
)

load_to_sf = SnowflakeOperator(
    task_id='load_day_data',
    sql="""
        COPY INTO FACT_BIKE_RENTALS_DAY (
        DATE_KEY, SEASON_KEY, WEATHER_KEY, HOLIDAY_FLAG, WORKINGDAY_FLAG,
        TEMPERATURE, FEELING_TEMP, HUMIDITY, WINDSPEED,
        CASUAL, REGISTERED, TOTAL_COUNT
    )
    FROM @bike_stage/day_clean.csv
    FILE_FORMAT = (TYPE=CSV SKIP_HEADER=1 FIELD_OPTIONALLY_ENCLOSED_BY='"' 
                ERROR_ON_COLUMN_COUNT_MISMATCH=FALSE)
    ON_ERROR = 'CONTINUE';
    """,
    snowflake_conn_id='my_snowflake_conn',
    dag=dag
)
