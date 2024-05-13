import unittest
from unittest import mock

from cloud.amazon.sqs import Publisher
from cloud.protocols import MessagePublisher


class TestMessagePublisher(unittest.TestCase):
    @mock.patch("boto3.client")
    def test_message_publisher(self, client_mock):
        publisher = Publisher()

        self.assertIsInstance(publisher, MessagePublisher)
        client_mock.assert_called_once_with("sqs")

        queue = "https://sqs.us-east-1.amazonaws.com/123456789012/test-queue"
        message = "test message"

        publisher.publish(queue, message)

        cli = client_mock.return_value
        cli.send_message.assert_called_once_with(QueueUrl=queue, MessageBody=message)
