import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from http import HTTPStatus
import random
from smtplib import SMTP

import connexion
import six
from flask import Response
from flask_jwt_extended import create_access_token
from peewee import DoesNotExist

from swagger_server.data.dbmodel import (
    database,
    Usuario as UsuarioDB,
    Domicilio as DomicilioDB,
    Aceptado as AceptadoDB
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
    response = Response(status=HTTPStatus.NOT_FOUND.value)
    database.connect()
    try:
        user = UsuarioDB.get(UsuarioDB.correoelectronico == username)
        if (user.contrasenia == password):
            if (user.aceptadoid == AceptadoDB.get_by_id(1)):
                acces_token = create_access_token(identity=username)
                response = Response(acces_token, status=HTTPStatus.OK.value)
            else:
                response = Response(status=HTTPStatus.UNAUTHORIZED.value)
        else:
            response = Response(status=HTTPStatus.FORBIDDEN.value)
    except DoesNotExist:
        response = Response(status=HTTPStatus.NOT_FOUND.value)
    finally:
        database.close()
    return response


def send_validationToken_email(username, nombrecompleto, token):
    afforoxEmail = "afforox@gmail.com"
    message = MIMEMultipart("plain")
    message["From"] = "afforox@gmail.com"
    message["To"] = username
    message["Subject"] = "Codigo de verificación Afforox"
    body = "Bienvenido a Afforox " + nombrecompleto + ", su código de verificacion es: " + token
    body = MIMEText(body)
    message.attach(body)

    smtp = SMTP("smtp.gmail.com")
    smtp.starttls()
    smtp.login(afforoxEmail, "Jinchuriki2k")
    smtp.sendmail(afforoxEmail, username, message.as_string())
    smtp.quit()


def tokenGenerator():
    token = ''
    for x in range(0, 3):
        token = token + random.choice(string.digits)
        token = token + random.choice(string.ascii_uppercase)
    return token


def nuevo_token(username):  # noqa: E501
    """Genera un nuevo token de verificación

    Genera un nuevo token de verificación # noqa: E501

    :param username: El usuario que genera el nuevo token
    :type username: str

    :rtype: Token
    """
    database.connect()
    try:
        user = UsuarioDB.get(UsuarioDB.correoelectronico == username)
        token = tokenGenerator()
        user.codigoautenticacion = token
        user.save()
        send_validationToken_email(username, user.nombrecompleto, token)
        response = Response(status=HTTPStatus.OK)
    except DoesNotExist:
        response = Response(status=HTTPStatus.NOT_FOUND.value)
    finally:
        database.close()
    return response


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
        postedUser = UsuarioDB.create(
            aceptadoid=3,
            codigoautenticacion=tokenGenerator(),
            contrasenia=body.contrasenia,
            correoelectronico=body.correo_electronico,
            edad=body.edad,
            fechanacimiento=body.fecha_nacimiento,
            fotoperfil=body.foto_perfil,
            nombrecompleto=body.nombre_completo,
            telefono=body.telefono,
            domicilioid=DomicilioDB.create(
                calle=body.domicilio.calle,
                ciudad=body.domicilio.ciudad,
                colonia=body.domicilio.colonia,
                estado=body.domicilio.estado,
                municipio=body.domicilio.municipio,
                numeroexterior=body.domicilio.numero_exterior,
                numerointerior=body.domicilio.numero_interior,
                pais=body.domicilio.pais
            )
        )
        send_validationToken_email(postedUser.correoelectronico, postedUser.nombrecompleto,
                                   postedUser.codigoautenticacion)
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
    database.connect()
    try:
        user = UsuarioDB.get_by_id(username)
        if user.aceptadoid == AceptadoDB.get_by_id(3):
            if (user.codigoautenticacion == token):
                (UsuarioDB.update({UsuarioDB.aceptadoid: 1}).where(UsuarioDB.correoelectronico == username)).execute()
                response = Response(status=HTTPStatus.OK.value)
            else:
                response = Response(status=HTTPStatus.UNAUTHORIZED.value)
        else:
            response = Response(status=HTTPStatus.FORBIDDEN.value)
    except DoesNotExist:
        response = Response(status=HTTPStatus.NOT_FOUND.value)
    finally:
        database.close()
    return response
