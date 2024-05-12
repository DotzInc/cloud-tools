from typing import Any

from google.cloud import pubsub_v1


class Publisher:
    def __init__(self) -> None:
        self.client = pubsub_v1.PublisherClient()

    def publish(self, recipient: str, message: str, **attrs: Any) -> None:
        future = self.client.publish(recipient, data=message.encode(), **attrs)
        future.result()
