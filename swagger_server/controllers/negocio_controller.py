import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.negocio import Negocio  # noqa: E501
from swagger_server import util


def get_negocio_by_id(negocio_id):  # noqa: E501
    """Obtiene la información de un negocio particular

     # noqa: E501

    :param negocio_id: Identificador del negocio
    :type negocio_id: int

    :rtype: Negocio
    """
    return 'do some magic!'


def get_negocios(salto=None, limite=None, filtro=None):  # noqa: E501
    """Obtiene todos los negocios

    Obtiene todos los negocios # noqa: E501

    :param salto: La cantidad de registros a saltar en la respuesta
    :type salto: float
    :param limite: La cantidad de registros a obtener
    :type limite: float
    :param filtro: La expresion por la cual se van a filtrar los resultados.
    :type filtro: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def registrar_negocio(body=None):  # noqa: E501
    """Registra un negocio

    Registra un negocio # noqa: E501

    :param body: Objeto negocio a registrar
    :type body: dict | bytes

    :rtype: Negocio
    """
    if connexion.request.is_json:
        body = Negocio.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
