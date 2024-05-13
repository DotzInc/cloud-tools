from typing import Any, Callable, Type

from cloud.protocols import StorageUploader


def storage_uploader(
    uploader_class: Type[StorageUploader], *args: Any, **kwargs: Any
) -> Callable[[], StorageUploader]:
    error = f"{uploader_class.__name__} does not implement StorageUploader protocol"

    def maker() -> StorageUploader:
        uploader = uploader_class(*args, **kwargs)
        assert isinstance(uploader, StorageUploader), error
        return uploader

    return maker
