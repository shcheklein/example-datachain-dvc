import shutil
from pathlib import Path

from datachain import DataChain

# Read the list of files, instantiate them
# Note: `anon=True` is to propagated it to the `to_storage`
DataChain.from_parquet("data/dataset.parquet", anon=True).to_storage(output='data')

prefix = Path("data") / "dvc-public-versioned" 
shutil.move(prefix / "get-started-pools" / "data" / "pool_data", Path("data") / "pool_data")
shutil.rmtree(prefix)