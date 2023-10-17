from config import PLCSettings
from plc_interfaces.plc_network_interface import PLCNetworkInterface
from plc_interfaces.plc_interface import PLCInterface
from tag_models.tag_data import get_all_tags
from clients.first_client_process import FirstClient

if __name__ == '__main__':
    plc_network = PLCNetworkInterface()
    plc_found = plc_network.find_plc(PLCSettings.ip)

    if plc_found:
        all_tags = get_all_tags()

        plc_interface = PLCInterface(
            ip=PLCSettings.ip,
            slot=0,
            timeout=.5,
            tags=all_tags
        )

        first_client = FirstClient(plc_interface)
        first_client.run()
    else:
        print('PLC not found')
