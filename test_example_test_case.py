import pytest

device_count = 100
api_count = 100

class TestSampleCase:

    def test_device_count(self):
        assert device_count == api_count
