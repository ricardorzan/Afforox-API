import json
from http import HTTPStatus

import connexion
import six
from flask import Response
from peewee import DoesNotExist

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models import Negocio, Sucursal, Domicilio  # noqa: E501
from swagger_server import util
from flask_jwt_extended import jwt_required, get_jwt_identity

from swagger_server.data.dbmodel import (
    database,
    Usuario as UsuarioDB,
    Domicilio as DomicilioDB,
    Negocio as NegocioDB,
    Sucursal as SucursalDB,
    Horario as HorarioDB,
    Tiponegocio as TiponegocioDB,
    Dia as DiaDB
)


def get_negocio_by_id(negocio_id):  # noqa: E501
    """Obtiene la información de un negocio particular

     # noqa: E501

    :param negocio_id: Identificador del negocio
    :type negocio_id: int

    :rtype: Negocio
    """
    response = Response(status=HTTPStatus.NOT_FOUND.value)
    database.connect()
    try:
        negocio = NegocioDB.get(NegocioDB.negocioid == negocio_id)
        print(negocio)
        negocio_aux = Negocio()
        negocio_aux.tipo_negocio = TiponegocioDB.get(TiponegocioDB.tiponegocioid == negocio.tiponegocioid).tiponegocio
        negocio_aux.nombre_completo = negocio.nombrenegocio
        negocio_aux.correo_electronico = negocio.correoelectronico
        negocio_aux.usuario_correo = negocio.correoelectronicousuario.correoelectronico
        print(negocio_aux.usuario_correo)
        negocio_aux.facebook = negocio.facebook
        negocio_aux.instagram = negocio.instagram
        negocio_aux.telefono = negocio.telefono
        negocio_aux.whatsapp = negocio.whatsapp

        retrive_sucursal_list = SucursalDB.select().where(SucursalDB.negocioid == negocio_id)
        if retrive_sucursal_list.exists():
            sucursal_list = []
            for sucursal in retrive_sucursal_list:
                sucursal_aux = Sucursal()
                sucursal_aux.sucursal_id = sucursal.sucursalid
                sucursal_aux.nombre_sucursal = sucursal.nombresucursal
                sucursal_aux.domicilio = Domicilio(
                    calle=sucursal.domicilioid.calle,
                    ciudad=sucursal.domicilioid.ciudad,
                    colonia=sucursal.domicilioid.colonia,
                    estado=sucursal.domicilioid.estado,
                    municipio=sucursal.domicilioid.municipio,
                    numero_exterior=sucursal.domicilioid.numeroexterior,
                    numero_interior=sucursal.domicilioid.numerointerior,
                    pais=sucursal.domicilioid.pais,
                )
                sucursal_aux.telefono = sucursal.telefono
                sucursal_aux.aforo_total = sucursal.aforototal
                sucursal_aux.aforo_actual = sucursal.aforoactual
                sucursal_list.append(sucursal_aux)
            negocio_aux.sucursales = sucursal_list

        negocio_json = Negocio.to_dict(negocio_aux)
        print(negocio_json)
        response = Response(json.dumps(negocio_json), status=HTTPStatus.OK.value, mimetype="application/json")
    except DoesNotExist:
        response = Response(status=HTTPStatus.NOT_FOUND.value)
    finally:
        database.close()
    return response


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
    database.connect()
    try:
        business_list = NegocioDB.select().paginate(1, limite)
        business_objects = []
        for business in business_list:
            negocio_aux = Negocio()
            '''negocio_aux.foto_perfil = business.fotoperfil'''
            negocio_aux.negocio_id = business.negocioid
            negocio_aux.nombre_completo = business.nombrenegocio
            business_objects.append(negocio_aux)
    except DoesNotExist:
        response = Response(status=HTTPStatus.NOT_FOUND.value)
    finally:
        database.close()
    if business_objects:
        business_json = []
        for business in business_objects:
            business_json.append(Negocio.to_dict(business))
        print(business_json)
        response = Response(json.dumps(business_json), status=HTTPStatus.OK.value)
    else:
        response = Response(status=HTTPStatus.NOT_FOUND.value)
    return response


@jwt_required()
def registrar_negocio(body=None):  # noqa: E501
    """Registra un negocio

    Registra un negocio # noqa: E501

    :param body: Objeto negocio a registrar
    :type body: dict | bytes

    :rtype: Negocio
    """
    current_user = get_jwt_identity()
    if connexion.request.is_json:
        body = Negocio.from_dict(connexion.request.get_json())  # noqa: E501
    print(current_user)
    print(body)

    postedHorario = HorarioDB.create(
        diaid=DiaDB.get(DiaDB.dia == body.sucursales[0].horarios[0].dia),
        horarioapertura=body.sucursales[0].horarios[0].horario_apertura,
        horariocierre=body.sucursales[0].horarios[0].horario_cierre,
        sucursalid=SucursalDB.create(
            aforoactual=0,
            aforototal=body.sucursales[0].aforo_total,
            domicilioid=DomicilioDB.create(
                calle=body.sucursales[0].domicilio.calle,
                ciudad=body.sucursales[0].domicilio.ciudad,
                colonia=body.sucursales[0].domicilio.colonia,
                estado=body.sucursales[0].domicilio.estado,
                municipio=body.sucursales[0].domicilio.municipio,
                numeroexterior=body.sucursales[0].domicilio.numero_exterior,
                numerointerior=body.sucursales[0].domicilio.numero_interior,
                pais=body.sucursales[0].domicilio.pais
            ),
            negocioid=NegocioDB.create(
                correoelectronico=body.correo_electronico,
                correoelectronicousuario=current_user,
                facebook=body.facebook,
                fotoperfil=body.foto_perfil,
                instagram=body.instagram,
                nombrenegocio=body.nombre_completo,
                telefono=body.telefono,
                tiponegocioid=TiponegocioDB.get(TiponegocioDB.tiponegocio == body.tipo_negocio),
                whatsapp=body.whatsapp
            ),
            nombresucursal=body.nombre_completo,
            telefono=body.telefono
        )
    )
    response = Response(status=HTTPStatus.CREATED.value)
    return response
