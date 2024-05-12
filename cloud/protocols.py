from typing import Protocol, runtime_checkable


@runtime_checkable
class StorageUploader(Protocol):
    def upload(self, bucket_name: str, destination_filename: str, source_filename: str) -> None: ...
