import pandas as pd
import os

def main():
    # Đường dẫn file
    INPUT_PATH = '/opt/airflow/dags/data/bike_sharing/day.csv'
    OUTPUT_PATH = '/opt/airflow/dags/data_output/day_clean.csv'

    # Đọc file gốc
    df = pd.read_csv(INPUT_PATH)

    # Tạo datetime và khóa
    df['datetime'] = pd.to_datetime(df['dteday'])
    df['date_key'] = df['datetime'].dt.strftime('%Y%m%d').astype(int)

    # Chọn cột cần thiết và đổi tên
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
        'casual': 'casual',
        'registered': 'registered'
    })

    # Xuất file đã làm sạch
    df_clean.to_csv(OUTPUT_PATH, index=False)
    print("✅ day_clean.csv đã được tạo:", OUTPUT_PATH)

if __name__ == "__main__":
    main()
