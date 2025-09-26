import pandas as pd
import kagglehub
from pathlib import Path

# 데이터 저장 폴더
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# Kagglehub에서 다운로드
path = kagglehub.dataset_download("federalreserve/interest-rates", str(data_dir))

# CSV 로드
df = pd.read_csv(f"{path}/index.csv")

# 날짜 컬럼 생성
df['date'] = pd.to_datetime(dict(year=df.Year, month=df.Month, day=df.Day))
df = df.sort_values("date").reset_index(drop=True)

# 저장
df.to_csv(data_dir / "interest_rates.csv", index=False)

print(f"Data saved to {data_dir / 'interest_rates.csv'}")

