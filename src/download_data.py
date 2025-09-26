import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
from pathlib import Path

# 1) 데이터 폴더 생성
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# 2) Kaggle API 인증
api = KaggleApi()
api.authenticate()

# 3) dataset slug
dataset_slug = "federalreserve/interest-rates"

# 4) 다운로드 + 압축 해제
api.dataset_download_files(dataset_slug, path=str(data_dir), unzip=True)

# 5) CSV 로드
df = pd.read_csv(data_dir / "index.csv")

# 6) 날짜 컬럼 생성
df['date'] = pd.to_datetime(dict(year=df.Year, month=df.Month, day=df.Day))
df = df.sort_values("date").reset_index(drop=True)

# 7) CSV로 저장
df.to_csv(data_dir / "interest_rates.csv", index=False)

print(f"Data saved to {data_dir / 'interest_rates.csv'}")
print(df.head())
