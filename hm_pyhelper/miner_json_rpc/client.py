import requests
from jsonrpcclient import request
from hm_pyhelper.miner_json_rpc.exceptions import MinerConnectionError
from hm_pyhelper.miner_json_rpc.exceptions import MinerMalformedURL
from hm_pyhelper.miner_json_rpc.exceptions import MinerRegionUnset

from hm_pyhelper.logger import get_logger

LOGGER = get_logger(__name__)

class Client(object):

    def __init__(self, url='http://helium-miner:4467'):
        self.url = url

    def __fetch_data(self, method, **kwargs):
        try:
            response = request(self.url, method, **kwargs)
            LOGGER.info("=============================")
            LOGGER.info(response.data.result)
            LOGGER.info("=============================")
            return response.data.result
        except requests.exceptions.ConnectionError as e:
            LOGGER.exception(e)
            return str(e)
        except requests.exceptions.MissingSchema as e:
            LOGGER.exception(e)
            return str(e)

    def get_height(self):
        return self.__fetch_data('info_height')

    def get_region(self):
        region = self.__fetch_data('info_region')
        if not region.get('region'):
            raise MinerRegionUnset(
                "Miner at %s does not have an asserted region"
                % self.url
            )
        return region

    def get_summary(self):
        return self.__fetch_data('info_summary')

    def get_peer_addr(self):
        return self.__fetch_data('peer_addr')

    def get_peer_book(self):
        return self.__fetch_data('peer_book', addr='self')

    def get_firmware_version(self):
        summary = self.get_summary()
        return summary.get('firmware_version')
