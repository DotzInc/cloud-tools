from typing import Any

from google.cloud import storage


class Uploader:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.client = storage.Client(*args, **kwargs)

    def upload(self, bucket_name: str, destination_filename: str, source_filename: str) -> None:
        bucket = self.client.bucket(bucket_name)
        blob = bucket.blob(destination_filename)
        blob.upload_from_filename(source_filename)


class Downloader:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.client = storage.Client(*args, **kwargs)

    def download(self, bucket_name: str, source_filename: str, destination_filename: str) -> None:
        bucket = self.client.bucket(bucket_name)
        blob = bucket.blob(source_filename)
        blob.download_to_filename(destination_filename)
