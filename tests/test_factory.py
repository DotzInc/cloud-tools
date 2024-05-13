import unittest
from unittest import mock

from cloud import factory
from cloud.amazon import s3
from cloud.google import storage
from cloud.protocols import StorageUploader


class NotStorageUploader:
    def upload_file(self):
        pass


class TestStorageUploaderFactory(unittest.TestCase):
    @mock.patch("google.cloud.storage.Client")
    def test_google_uploader(self, _):
        FileUploader = factory.storage_uploader(storage.Uploader)
        self.assertIsInstance(FileUploader(), StorageUploader)

    @mock.patch("boto3.client")
    def test_amazon_uploader(self, _):
        FileUploader = factory.storage_uploader(s3.Uploader)
        self.assertIsInstance(FileUploader(), StorageUploader)

    def test_uploader_protocol_validation(self):
        FileUploader = factory.storage_uploader(NotStorageUploader)  # type: ignore
        error = f"{NotStorageUploader.__name__} does not implement StorageUploader protocol"

        with self.assertRaisesRegex(AssertionError, error):
            FileUploader()
