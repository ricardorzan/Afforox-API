import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.sucursal import Sucursal  # noqa: E501
from swagger_server import util


def obtener_sucursal(negocio_id, sucursal_id):  # noqa: E501
    """Obtiene una sucursal

    Obtiene una sucursal # noqa: E501

    :param negocio_id: 
    :type negocio_id: int
    :param sucursal_id: 
    :type sucursal_id: int

    :rtype: Sucursal
    """
    return 'do some magic!'


def registrar_sucursal(negocio_id, body=None):  # noqa: E501
    """Registra una sucursal

    Registra una sucursal # noqa: E501

    :param negocio_id: Unique identifier of the user
    :type negocio_id: str
    :param body: Objeto negocio a registrar
    :type body: dict | bytes

    :rtype: Sucursal
    """
    if connexion.request.is_json:
        body = Sucursal.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
