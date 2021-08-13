import pandas as pd
import sys

df = pd.read_parquet(sys.argv[1])
df['timestamp'].astype('int64')
df.to_csv(sys.argv[2], index=False)