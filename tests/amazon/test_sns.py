import unittest
from unittest import mock

from cloud.amazon.sns import Publisher
from cloud.protocols import MessagePublisher


class TestMessagePublisher(unittest.TestCase):
    @mock.patch("boto3.client")
    def test_message_publisher(self, client_mock):
        publisher = Publisher()

        self.assertIsInstance(publisher, MessagePublisher)
        client_mock.assert_called_once_with("sns")

        topic = "arn:aws:sns:us-east-1:123456789012:test-topic"
        message = "test message"

        publisher.publish(topic, message)

        cli = client_mock.return_value
        cli.publish.assert_called_once_with(TargetArn=topic, Message=message)
