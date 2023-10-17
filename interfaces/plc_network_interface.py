<<<<<<< HEAD
from client_config import ClientSettings
from pylogix import PLC
import time
import logging


client_logger = logging.getLogger(__name__)


class PLCNetworkInterface:
    def __init__(self):
        self.comm = PLC()

    def discover_devices(self):
        found_devices = []
        devices = self.comm.Discover()

        for device in devices.Value:
            found_devices.append(device.IPAddress)

        return found_devices

    def find_plc(self, ip):
        if ClientSettings.debug:
            client_logger.warning('Forcing PLC write in debug.')
            return True

        while True:
            client_logger.info(f'Attempting to find plc: {ip}')
            found_devices = self.discover_devices()

            if ip in found_devices:
                client_logger.info(f'Found PLC: {ip}')
                return True

            time.sleep(3)
=======
from client_config import ClientSettings
from pylogix import PLC
import time
import logging


client_logger = logging.getLogger(__name__)


class PLCNetworkInterface:
    def __init__(self):
        self.comm = PLC()

    def discover_devices(self):
        found_devices = []
        devices = self.comm.Discover()

        for device in devices.Value:
            found_devices.append(device.IPAddress)

        return found_devices

    def find_plc(self, ip):
        if ClientSettings.debug:
            client_logger.warning('Forcing PLC write in debug.')
            return True

        while True:
            client_logger.info(f'Attempting to find plc: {ip}')
            found_devices = self.discover_devices()

            if ip in found_devices:
                client_logger.info(f'Found PLC: {ip}')
                return True

            time.sleep(3)
>>>>>>> 8619df6771e2bb89d06a8d802c282bf417d56805
