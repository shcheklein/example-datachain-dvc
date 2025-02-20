from datachain import DataChain, C

# Read the list of _files_ from the bucket (including version id and etags,
# so it is safe to change remove files upstream).
# This way we are getting a snapshot or a version of the dataset.
# Next time it runs it gets the new list. Thus creating a new version.
# `data/dataset.parquet` can be saved in DVC - to share with the team +
# to serve as entry point to the pipeline.
(
    DataChain
        .from_storage("s3://dvc-public-versioned/get-started-pools/", type="image", anon=True, update=True)
        .filter(C("file.path").glob("*.jpg") | C("file.path").glob("*.png"))
        .to_parquet("data/dataset.parquet")
)
