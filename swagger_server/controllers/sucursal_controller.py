from http import HTTPStatus

import connexion
import six
from flask import Response
from peewee import DoesNotExist

from swagger_server.data.dbmodel import (
    database,
    Sucursal as SucursalDB
)
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


def update_aforo(sucursal_id, action):
    database.connect()
    try:
        sucursal = SucursalDB.get_by_id(sucursal_id)
        if action == 'plus':
            print(sucursal.aforoactual)
            sucursal.aforoactual = sucursal.aforoactual + 1
            print(sucursal.aforoactual)
        else:
            sucursal.aforoactual = sucursal.aforoactual - 1
        sucursal.save()
        response = Response(status=HTTPStatus.OK.value)
    except DoesNotExist:
        response = Response(status=HTTPStatus.NOT_FOUND.value)
    finally:
        database.close()
    return response
