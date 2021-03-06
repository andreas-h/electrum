from ..trezor.client import trezor_client_class
from ..trezor.plugin import TrezorCompatiblePlugin, TrezorCompatibleWallet


class KeepKeyWallet(TrezorCompatibleWallet):
    wallet_type = 'keepkey'
    device = 'KeepKey'


class KeepKeyPlugin(TrezorCompatiblePlugin):
    firmware_URL = 'https://www.keepkey.com'
    libraries_URL = 'https://github.com/keepkey/python-keepkey'
    minimum_firmware = (1, 0, 0)
    wallet_class = KeepKeyWallet
    try:
        from keepkeylib.client import proto, BaseClient, ProtocolMixin
        client_class = trezor_client_class(ProtocolMixin, BaseClient, proto)
        import keepkeylib.ckd_public as ckd_public
        from keepkeylib.client import types
        from keepkeylib.transport_hid import HidTransport
        libraries_available = True
    except:
        libraries_available = False
