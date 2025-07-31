import pandas as pd

def clean_bike_data(df, is_hour=True):
    if is_hour:
        df['datetime'] = pd.to_datetime(df['dteday']) + pd.to_timedelta(df['hr'], unit='h')
        df['datetime_key'] = df['datetime'].dt.strftime('%Y%m%d%H').astype(int)
        df['hour_key'] = df['hr']
    else:
        df['datetime'] = pd.to_datetime(df['dteday'])
        df['datetime_key'] = df['datetime'].dt.strftime('%Y%m%d').astype(int)
        df['hour_key'] = None  # hoặc bỏ

    df['date_key'] = df['datetime'].dt.strftime('%Y%m%d').astype(int)

    df_clean = df[[
        'datetime_key', 'date_key', 'hour_key',
        'season', 'weathersit', 'holiday', 'workingday',
        'temp', 'atemp', 'hum', 'windspeed',
        'casual', 'registered', 'cnt'
    ]].rename(columns={
        'weathersit': 'weather_key',
        'season': 'season_key',
        'holiday': 'holiday_flag',
        'workingday': 'workingday_flag',
        'cnt': 'total_count',
        'temp': 'temperature',
        'atemp': 'feeling_temp',
        'hum': 'humidity'
    })

    return df_clean
