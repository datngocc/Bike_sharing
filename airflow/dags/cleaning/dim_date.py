import os
import pandas as pd

# Đặt thư mục xuất qua biến môi trường 
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "MyProjectDE/data_output")

# Tạo dải ngày
dates = pd.date_range(start='2011-01-01', end='2012-12-31')

# Chuyển sang dataframe
df = pd.DataFrame({"FULL_DATE": dates})
df["DATE_KEY"] = df["FULL_DATE"].dt.strftime('%Y%m%d').astype(int)
df["YEAR"] = df["FULL_DATE"].dt.year
df["MONTH"] = df["FULL_DATE"].dt.month
df["DAY"] = df["FULL_DATE"].dt.day
df["WEEKDAY"] = df["FULL_DATE"].dt.weekday + 1  # Thứ hai = 1
df["IS_WEEKEND"] = df["WEEKDAY"] >= 6

# Sắp xếp lại thứ tự cột
cols = ["DATE_KEY", "FULL_DATE", "YEAR", "MONTH", "DAY", "WEEKDAY", "IS_WEEKEND"]
df = df[cols]

# Xuất file CSV
df.to_csv(f"{OUTPUT_DIR}/dim_date.csv", index=False)