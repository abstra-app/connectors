from ...utils.auth import Credentials
import uuid


class PixRecebimentosClient:
    """
    Cliente para a API Pix Recebimentos do Itaú.
    """

    def __init__(self, creds: Credentials, base_url: str = None, sandbox: bool = True):
        self.creds = creds
        if base_url:
            self.base_url = base_url
        else:
            if sandbox:
                self.base_url = "https://sandbox.devportal.itau.com.br/itau-ep9-gtw-pix-recebimentos-ext-v2/v2"
            else:
                self.base_url = "https://secure.api.itau/pix_recebimentos/v2"

    def _get_headers(self, correlation_id=None):
        return {
            "Authorization": f"Bearer {self.creds.get_token().access_token}",
            "x-itau-correlationid": correlation_id or str(uuid.uuid4()),
            "User-Agent": "Collection-by-itaú-for-developers",
            "Accept": "application/json",
        }

    # put cob/txid
    # patch cob/txid
    # get cob/txid
    # post cob
    # get cob
    # get cob/txid/qrcode
    # put cobv/txid
    # patch cobv/txid
    # get cobv/txid
    # get cobv
    # get cobv/txid/qrcode
    # put lotecobv/id
    # patch lotecobv/id
    # get lotecobv/id
    # get lotecobv
    # post loc
    # get loc
    # get loc/id
    # delete loc/id/txid
    # get pix/e2eid
    # get pix
    # put pix/e2eid/devolucao/id
    # get pix/e2eid/devolucao/id
    # put webhook/chave
    # get webhook/chave
    # delete webhook/chave
    # get webhook