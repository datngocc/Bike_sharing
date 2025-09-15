import pandas as pd
import os
import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def clean_day_data(input_path, output_path):
    if not os.path.exists(input_path):
        logging.error(f"Input file does not exist: {input_path}")
        sys.exit(1)

    try:
        df = pd.read_csv(input_path)
    except Exception as e:
        logging.error(f"Failed to read input file: {e}")
        sys.exit(1)

    try:
        df['datetime'] = pd.to_datetime(df['dteday'])
        df['date_key'] = df['datetime'].dt.strftime('%Y%m%d').astype(int)

        df_clean = df[[ 
            'date_key', 'season', 'weathersit', 'holiday', 'workingday',
            'temp', 'atemp', 'hum', 'windspeed',
            'casual', 'registered', 'cnt'
        ]].rename(columns={
            'season': 'season_key',
            'weathersit': 'weather_key',
            'holiday': 'holiday_flag',
            'workingday': 'workingday_flag',
            'temp': 'temperature',
            'atemp': 'feeling_temp',
            'hum': 'humidity',
            'cnt': 'total_count',
            'casual': 'casual_count',
            'registered': 'registered_count'
        })

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df_clean.to_csv(output_path, index=False)
        logging.info(f"✅ day_clean.csv đã được tạo: {output_path}")
    except Exception as e:
        logging.error(f"Error during cleaning or saving: {e}")
        sys.exit(1)

def main():
    input_path = os.environ.get('DAY_CLEAN_INPUT', '/opt/airflow/dags/data/bike_sharing/day.csv')
    output_path = os.environ.get('DAY_CLEAN_OUTPUT', '/opt/airflow/dags/data_output/day_clean.csv')

    # Cho phép truyền đối số dòng lệnh
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
    if len(sys.argv) > 2:
        output_path = sys.argv[2]

    clean_day_data(input_path, output_path)

if __name__ == "__main__":
    main()