import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.negocio import Negocio  # noqa: E501
from swagger_server import util


def registrar_sucursal(negocio_id, body=None):  # noqa: E501
    """Registra una sucursal

    Registra una sucursal # noqa: E501

    :param negocio_id: Unique identifier of the user
    :type negocio_id: str
    :param body: Objeto negocio a registrar
    :type body: dict | bytes

    :rtype: Negocio
    """
    if connexion.request.is_json:
        body = Negocio.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
