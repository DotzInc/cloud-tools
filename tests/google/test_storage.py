import unittest
from unittest import mock

from cloud.google.storage import Uploader
from cloud.protocols import StorageUploader


class TestStorageUploader(unittest.TestCase):
    @mock.patch("google.cloud.storage.Client")
    def test_storage_uploader(self, client_mock):
        uploader = Uploader()

        self.assertIsInstance(uploader, StorageUploader)
        client_mock.assert_called_once_with()

        bucket_name = "test-bucket"
        object_name = "test.txt"
        source_path = "/tmp/test.txt"

        uploader.upload(bucket_name, object_name, source_path)

        cli = client_mock.return_value
        cli.bucket.assert_called_once_with(bucket_name)

        bucket = cli.bucket.return_value
        bucket.blob.assert_called_once_with(object_name)

        blob = bucket.blob.return_value
        blob.upload_from_filename.assert_called_once_with(source_path)
