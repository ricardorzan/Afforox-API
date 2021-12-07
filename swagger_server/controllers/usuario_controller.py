from http import HTTPStatus

import connexion
import six
from flask import Response
from peewee import DoesNotExist

from swagger_server.data.dbmodel import (
    database,
    Usuario as UsuarioDB,
    Domicilio as DomicilioDB
)
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.token import Token  # noqa: E501
from swagger_server.models.usuario import Usuario  # noqa: E501
from swagger_server import util


def get_usuario(usuario_id):  # noqa: E501
    """Obtiene la información de un usuario particular

     # noqa: E501

    :param usuario_id: identificador del usuario
    :type usuario_id: str

    :rtype: Usuario
    """
    return 'do some magic!'


def login(username, password):  # noqa: E501
    """Iniciar sesión

    Iniciar sesión # noqa: E501

    :param username: El usuario que inicia sesión
    :type username: str
    :param password: La contraseña del usuario
    :type password: dict | bytes

    :rtype: Token
    """
    if connexion.request.is_json:
        password = str.from_dict(connexion.request.get_json())  # noqa: E501
    response = Response(status=HTTPStatus.NOT_FOUND.value)
    database.connect()
    try:
        user = UsuarioDB.get(UsuarioDB.correoelectronico == username)
        if (user.contrasenia == password):
            if (user.aceptadoid == 1):
                response = Response(status=HTTPStatus.OK.value)
        else:
            response = Response(status=HTTPStatus.UNAUTHORIZED.value)
    except DoesNotExist:
        response = Response(status=HTTPStatus.NOT_FOUND.value)
    finally:
        database.close()
    return response


def nuevo_token(username):  # noqa: E501
    """Genera un nuevo token de verificación

    Genera un nuevo token de verificación # noqa: E501

    :param username: El usuario que genera el nuevo token
    :type username: str

    :rtype: Token
    """
    return 'do some magic!'


def patch_usuario(body, usuario_id):  # noqa: E501
    """Modifica los datos del usuario

     # noqa: E501

    :param body: Independient user object to patch
    :type body: dict | bytes
    :param usuario_id: identificador del usuario
    :type usuario_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Usuario.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def registrar_usuario(body=None):  # noqa: E501
    """Registra un nuevo usuario

    Registra un nuevo usuario # noqa: E501

    :param body: Objeto usuario a registrar
    :type body: dict | bytes

    :rtype: Usuario
    """
    if connexion.request.is_json:
        body = Usuario.from_dict(connexion.request.get_json())  # noqa: E501
    response = Response(status=HTTPStatus.NOT_FOUND.value)
    list_accounts = UsuarioDB.select().where(UsuarioDB.correoelectronico == body.correo_electronico)
    if list_accounts.exists():
        return response
    else:
        postedDomicilio = DomicilioDB.create(
            calle=body.calle,
            ciudad=body.ciudad,
            colonia=body.colonia,
            estado=body.estado,
            municipio=body.municipio,
            numeroexterior=body.numero_exterior,
            numerointerior=body.numero_interior,
            pais=body.pais
        )
        postedDomicilio.save()
        '''Modificar el codigoautenticacion'''
        postedUser = UsuarioDB.create(
            aceptadoid=2,
            codigoautenticacion='XJ034',
            contrasenia=body.contrasenia,
            correoelectronico=body.correo_electronico,
            edad=body.edad,
            fechanacimiento=body.fecha_nacimiento,
            fotoperfil=body.foto_perfil,
            nombrecompleto=body.nombre_completo,
            telefono=body.telefono
        )
        postedUser.domicilioid = postedDomicilio
        postedUser.save()
        response = Response(status=HTTPStatus.CREATED.value)
    return response


def validar_usuario(username, token):  # noqa: E501
    """Validación del usuario mediante un token de verificación

     # noqa: E501

    :param username: Nombre del usuario a verificar
    :type username: str
    :param token: Token de verificación
    :type token: str

    :rtype: None
    """
    return 'do some magic!'
