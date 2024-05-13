from typing import Any, Callable, Type

from cloud.protocols import MessagePublisher, StorageUploader

error_message = "%(class)s does not implement %(protocol)s protocol"


def storage_uploader(
    uploader_class: Type[StorageUploader], *args: Any, **kwargs: Any
) -> Callable[[], StorageUploader]:
    error = error_message % {"class": uploader_class.__name__, "protocol": "StorageUploader"}

    def maker() -> StorageUploader:
        uploader = uploader_class(*args, **kwargs)
        assert isinstance(uploader, StorageUploader), error
        return uploader

    return maker


def message_publisher(
    publisher_class: Type[MessagePublisher], *args: Any, **kwargs: Any
) -> Callable[[], MessagePublisher]:
    error = error_message % {"class": publisher_class.__name__, "protocol": "MessagePublisher"}

    def maker() -> MessagePublisher:
        publisher = publisher_class(*args, **kwargs)
        assert isinstance(publisher, MessagePublisher), error
        return publisher

    return maker
