import logging

from unittest import TestCase
from SolarWattEnergyManagerAPI.SolarWatt import EnergyManagerAPI


class TestEnergyManagerAPI(TestCase):
    # energy manager host
    _HOST = 'energyManager'

    def test_set_host(self):
        api = EnergyManagerAPI()
        with self.assertRaises(ValueError):
            api.set_host('')
        with self.assertRaises(ValueError):
            api.set_log_level('INVALID_LOG_LEVEL')
        try:
            api.set_host(self._HOST)
        except ValueError:
            self.fail('set_host() raised unexpected ValueError')

    def test_set_log_level(self):
        api = EnergyManagerAPI()
        try:
            api.set_log_level('WARNING')
        except ValueError:
            self.fail('set_log_level(str) raised unexpected ValueError')
        try:
            api.set_log_level(10)
        except ValueError:
            self.fail('set_log_level(int) raised unexpected ValueError')

    def test_set_logger(self):
        api = EnergyManagerAPI()
        try:
            api.set_logger(logging.Logger)
        except Exception as e:
            self.fail(f'unexpected exception: {repr(e)}')

    def test_test_connection(self):
        # this test only works if you own a compatible device (change host below)
        api = EnergyManagerAPI()
        api.set_host(self._HOST)
        try:
            status, data = api.test_connection()
            if not status:
                self.fail(f'Connection to energy manager failed, error: {data}')
        except Exception as e:
            self.fail(f'Unexpected exception: {repr(e)}')

    def test_pull_data(self):
        # this test only works if you own a compatible device (change host below)
        api = EnergyManagerAPI()
        api.set_host(self._HOST)
        try:
            result = api.pull_data()
            # print(result)
        except Exception as e:
            self.fail(f'unexpected exception: {repr(e)}')
