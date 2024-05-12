import unittest
from unittest import mock

from cloud.google.pubsub import Publisher
from cloud.protocols import MessagePublisher


class TestMessagePublisher(unittest.TestCase):
    @mock.patch("google.cloud.pubsub_v1.PublisherClient")
    def test_message_publisher(self, client_mock):
        publisher = Publisher()

        self.assertIsInstance(publisher, MessagePublisher)

        topic = "projects/test-project/topics/test-topic"
        message = "test message"

        publisher.publish(topic, message)

        cli = client_mock.return_value
        cli.publish.assert_called_once_with(topic, data=message.encode())
