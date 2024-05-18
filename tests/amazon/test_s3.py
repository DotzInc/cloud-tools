import unittest
from unittest import mock

from cloud.amazon.s3 import Downloader, Uploader
from cloud.protocols import StorageDownloader, StorageUploader


class TestStorageUploader(unittest.TestCase):
    @mock.patch("boto3.client")
    def test_storage_upload(self, client_mock):
        uploader = Uploader()

        self.assertIsInstance(uploader, StorageUploader)
        client_mock.assert_called_once_with("s3")

        bucket_name = "test-bucket"
        object_name = "test.txt"
        source_path = "/tmp/test.txt"

        uploader.upload(bucket_name, object_name, source_path)

        cli = client_mock.return_value
        cli.upload_file.assert_called_once_with(source_path, bucket_name, object_name)


class TestStorageDownloader(unittest.TestCase):
    @mock.patch("boto3.client")
    def test_storage_download(self, client_mock):
        downloader = Downloader()

        self.assertIsInstance(downloader, StorageDownloader)
        client_mock.assert_called_once_with("s3")

        bucket_name = "test-bucket"
        object_name = "test.txt"
        destination = "/tmp/test.txt"

        downloader.download(bucket_name, object_name, destination)

        cli = client_mock.return_value
        cli.download_file.assert_called_once_with(bucket_name, object_name, destination)
