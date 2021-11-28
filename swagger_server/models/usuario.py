# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Usuario(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, foto_perfil: str=None, nombre_completo: str=None, correo_electronico: str=None, fecha_nacimiento: date=None, contrasenia: str=None, edad: str=None, telefono: str=None, pais: str=None, estado: str=None, ciudad: str=None, municipio: str=None, calle: str=None, numero_interior: str=None, numero_exterior: str=None, colonia: str=None, aceptado: str=None, token: str=None):  # noqa: E501
        """Usuario - a model defined in Swagger

        :param foto_perfil: The foto_perfil of this Usuario.  # noqa: E501
        :type foto_perfil: str
        :param nombre_completo: The nombre_completo of this Usuario.  # noqa: E501
        :type nombre_completo: str
        :param correo_electronico: The correo_electronico of this Usuario.  # noqa: E501
        :type correo_electronico: str
        :param fecha_nacimiento: The fecha_nacimiento of this Usuario.  # noqa: E501
        :type fecha_nacimiento: date
        :param contrasenia: The contrasenia of this Usuario.  # noqa: E501
        :type contrasenia: str
        :param edad: The edad of this Usuario.  # noqa: E501
        :type edad: str
        :param telefono: The telefono of this Usuario.  # noqa: E501
        :type telefono: str
        :param pais: The pais of this Usuario.  # noqa: E501
        :type pais: str
        :param estado: The estado of this Usuario.  # noqa: E501
        :type estado: str
        :param ciudad: The ciudad of this Usuario.  # noqa: E501
        :type ciudad: str
        :param municipio: The municipio of this Usuario.  # noqa: E501
        :type municipio: str
        :param calle: The calle of this Usuario.  # noqa: E501
        :type calle: str
        :param numero_interior: The numero_interior of this Usuario.  # noqa: E501
        :type numero_interior: str
        :param numero_exterior: The numero_exterior of this Usuario.  # noqa: E501
        :type numero_exterior: str
        :param colonia: The colonia of this Usuario.  # noqa: E501
        :type colonia: str
        :param aceptado: The aceptado of this Usuario.  # noqa: E501
        :type aceptado: str
        :param token: The token of this Usuario.  # noqa: E501
        :type token: str
        """
        self.swagger_types = {
            'foto_perfil': str,
            'nombre_completo': str,
            'correo_electronico': str,
            'fecha_nacimiento': date,
            'contrasenia': str,
            'edad': str,
            'telefono': str,
            'pais': str,
            'estado': str,
            'ciudad': str,
            'municipio': str,
            'calle': str,
            'numero_interior': str,
            'numero_exterior': str,
            'colonia': str,
            'aceptado': str,
            'token': str
        }

        self.attribute_map = {
            'foto_perfil': 'fotoPerfil',
            'nombre_completo': 'nombreCompleto',
            'correo_electronico': 'correoElectronico',
            'fecha_nacimiento': 'fechaNacimiento',
            'contrasenia': 'contrasenia',
            'edad': 'edad',
            'telefono': 'telefono',
            'pais': 'pais',
            'estado': 'estado',
            'ciudad': 'ciudad',
            'municipio': 'municipio',
            'calle': 'calle',
            'numero_interior': 'numeroInterior',
            'numero_exterior': 'numeroExterior',
            'colonia': 'colonia',
            'aceptado': 'aceptado',
            'token': 'token'
        }
        self._foto_perfil = foto_perfil
        self._nombre_completo = nombre_completo
        self._correo_electronico = correo_electronico
        self._fecha_nacimiento = fecha_nacimiento
        self._contrasenia = contrasenia
        self._edad = edad
        self._telefono = telefono
        self._pais = pais
        self._estado = estado
        self._ciudad = ciudad
        self._municipio = municipio
        self._calle = calle
        self._numero_interior = numero_interior
        self._numero_exterior = numero_exterior
        self._colonia = colonia
        self._aceptado = aceptado
        self._token = token

    @classmethod
    def from_dict(cls, dikt) -> 'Usuario':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The usuario of this Usuario.  # noqa: E501
        :rtype: Usuario
        """
        return util.deserialize_model(dikt, cls)

    @property
    def foto_perfil(self) -> str:
        """Gets the foto_perfil of this Usuario.

        Binary data of the media file  # noqa: E501

        :return: The foto_perfil of this Usuario.
        :rtype: str
        """
        return self._foto_perfil

    @foto_perfil.setter
    def foto_perfil(self, foto_perfil: str):
        """Sets the foto_perfil of this Usuario.

        Binary data of the media file  # noqa: E501

        :param foto_perfil: The foto_perfil of this Usuario.
        :type foto_perfil: str
        """

        self._foto_perfil = foto_perfil

    @property
    def nombre_completo(self) -> str:
        """Gets the nombre_completo of this Usuario.

        El **nombre** de la persona registrada  # noqa: E501

        :return: The nombre_completo of this Usuario.
        :rtype: str
        """
        return self._nombre_completo

    @nombre_completo.setter
    def nombre_completo(self, nombre_completo: str):
        """Sets the nombre_completo of this Usuario.

        El **nombre** de la persona registrada  # noqa: E501

        :param nombre_completo: The nombre_completo of this Usuario.
        :type nombre_completo: str
        """
        if nombre_completo is None:
            raise ValueError("Invalid value for `nombre_completo`, must not be `None`")  # noqa: E501

        self._nombre_completo = nombre_completo

    @property
    def correo_electronico(self) -> str:
        """Gets the correo_electronico of this Usuario.

        El **correoElectronico** del usuario que se busca registrar  # noqa: E501

        :return: The correo_electronico of this Usuario.
        :rtype: str
        """
        return self._correo_electronico

    @correo_electronico.setter
    def correo_electronico(self, correo_electronico: str):
        """Sets the correo_electronico of this Usuario.

        El **correoElectronico** del usuario que se busca registrar  # noqa: E501

        :param correo_electronico: The correo_electronico of this Usuario.
        :type correo_electronico: str
        """
        if correo_electronico is None:
            raise ValueError("Invalid value for `correo_electronico`, must not be `None`")  # noqa: E501

        self._correo_electronico = correo_electronico

    @property
    def fecha_nacimiento(self) -> date:
        """Gets the fecha_nacimiento of this Usuario.

        La **fechaNacimiento** del usuario que se busca registrar  # noqa: E501

        :return: The fecha_nacimiento of this Usuario.
        :rtype: date
        """
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento: date):
        """Sets the fecha_nacimiento of this Usuario.

        La **fechaNacimiento** del usuario que se busca registrar  # noqa: E501

        :param fecha_nacimiento: The fecha_nacimiento of this Usuario.
        :type fecha_nacimiento: date
        """

        self._fecha_nacimiento = fecha_nacimiento

    @property
    def contrasenia(self) -> str:
        """Gets the contrasenia of this Usuario.

        La **contrasena** es con la cual iniciara sesión el usuario, debe de tener una _longitud_ entre _8_ y _32_ y por lo menos debe de tener _una letra mayuscula_, _una letra minuscula_ y _un digito_  # noqa: E501

        :return: The contrasenia of this Usuario.
        :rtype: str
        """
        return self._contrasenia

    @contrasenia.setter
    def contrasenia(self, contrasenia: str):
        """Sets the contrasenia of this Usuario.

        La **contrasena** es con la cual iniciara sesión el usuario, debe de tener una _longitud_ entre _8_ y _32_ y por lo menos debe de tener _una letra mayuscula_, _una letra minuscula_ y _un digito_  # noqa: E501

        :param contrasenia: The contrasenia of this Usuario.
        :type contrasenia: str
        """
        if contrasenia is None:
            raise ValueError("Invalid value for `contrasenia`, must not be `None`")  # noqa: E501

        self._contrasenia = contrasenia

    @property
    def edad(self) -> str:
        """Gets the edad of this Usuario.

        La **edad** del usuario  # noqa: E501

        :return: The edad of this Usuario.
        :rtype: str
        """
        return self._edad

    @edad.setter
    def edad(self, edad: str):
        """Sets the edad of this Usuario.

        La **edad** del usuario  # noqa: E501

        :param edad: The edad of this Usuario.
        :type edad: str
        """

        self._edad = edad

    @property
    def telefono(self) -> str:
        """Gets the telefono of this Usuario.

        El **telefono** del usuario  # noqa: E501

        :return: The telefono of this Usuario.
        :rtype: str
        """
        return self._telefono

    @telefono.setter
    def telefono(self, telefono: str):
        """Sets the telefono of this Usuario.

        El **telefono** del usuario  # noqa: E501

        :param telefono: The telefono of this Usuario.
        :type telefono: str
        """
        if telefono is None:
            raise ValueError("Invalid value for `telefono`, must not be `None`")  # noqa: E501

        self._telefono = telefono

    @property
    def pais(self) -> str:
        """Gets the pais of this Usuario.

        El nombre del **pais** del usuario  # noqa: E501

        :return: The pais of this Usuario.
        :rtype: str
        """
        return self._pais

    @pais.setter
    def pais(self, pais: str):
        """Sets the pais of this Usuario.

        El nombre del **pais** del usuario  # noqa: E501

        :param pais: The pais of this Usuario.
        :type pais: str
        """
        if pais is None:
            raise ValueError("Invalid value for `pais`, must not be `None`")  # noqa: E501

        self._pais = pais

    @property
    def estado(self) -> str:
        """Gets the estado of this Usuario.

        El nombre del **estado** dentro del país en donde se encuentra el usuario  # noqa: E501

        :return: The estado of this Usuario.
        :rtype: str
        """
        return self._estado

    @estado.setter
    def estado(self, estado: str):
        """Sets the estado of this Usuario.

        El nombre del **estado** dentro del país en donde se encuentra el usuario  # noqa: E501

        :param estado: The estado of this Usuario.
        :type estado: str
        """
        if estado is None:
            raise ValueError("Invalid value for `estado`, must not be `None`")  # noqa: E501

        self._estado = estado

    @property
    def ciudad(self) -> str:
        """Gets the ciudad of this Usuario.

        El nombre de la **ciudad** en donde se encuentra el usuario  # noqa: E501

        :return: The ciudad of this Usuario.
        :rtype: str
        """
        return self._ciudad

    @ciudad.setter
    def ciudad(self, ciudad: str):
        """Sets the ciudad of this Usuario.

        El nombre de la **ciudad** en donde se encuentra el usuario  # noqa: E501

        :param ciudad: The ciudad of this Usuario.
        :type ciudad: str
        """

        self._ciudad = ciudad

    @property
    def municipio(self) -> str:
        """Gets the municipio of this Usuario.

        El nombre del **municipio** en donde se encuentra el usuario  # noqa: E501

        :return: The municipio of this Usuario.
        :rtype: str
        """
        return self._municipio

    @municipio.setter
    def municipio(self, municipio: str):
        """Sets the municipio of this Usuario.

        El nombre del **municipio** en donde se encuentra el usuario  # noqa: E501

        :param municipio: The municipio of this Usuario.
        :type municipio: str
        """

        self._municipio = municipio

    @property
    def calle(self) -> str:
        """Gets the calle of this Usuario.

        La **calle** del usuario  # noqa: E501

        :return: The calle of this Usuario.
        :rtype: str
        """
        return self._calle

    @calle.setter
    def calle(self, calle: str):
        """Sets the calle of this Usuario.

        La **calle** del usuario  # noqa: E501

        :param calle: The calle of this Usuario.
        :type calle: str
        """

        self._calle = calle

    @property
    def numero_interior(self) -> str:
        """Gets the numero_interior of this Usuario.

        El **numeroInterior** del usuario  # noqa: E501

        :return: The numero_interior of this Usuario.
        :rtype: str
        """
        return self._numero_interior

    @numero_interior.setter
    def numero_interior(self, numero_interior: str):
        """Sets the numero_interior of this Usuario.

        El **numeroInterior** del usuario  # noqa: E501

        :param numero_interior: The numero_interior of this Usuario.
        :type numero_interior: str
        """

        self._numero_interior = numero_interior

    @property
    def numero_exterior(self) -> str:
        """Gets the numero_exterior of this Usuario.

        El **numeroExterior** del usuario  # noqa: E501

        :return: The numero_exterior of this Usuario.
        :rtype: str
        """
        return self._numero_exterior

    @numero_exterior.setter
    def numero_exterior(self, numero_exterior: str):
        """Sets the numero_exterior of this Usuario.

        El **numeroExterior** del usuario  # noqa: E501

        :param numero_exterior: The numero_exterior of this Usuario.
        :type numero_exterior: str
        """

        self._numero_exterior = numero_exterior

    @property
    def colonia(self) -> str:
        """Gets the colonia of this Usuario.

        La **coloina** del usuario  # noqa: E501

        :return: The colonia of this Usuario.
        :rtype: str
        """
        return self._colonia

    @colonia.setter
    def colonia(self, colonia: str):
        """Sets the colonia of this Usuario.

        La **coloina** del usuario  # noqa: E501

        :param colonia: The colonia of this Usuario.
        :type colonia: str
        """

        self._colonia = colonia

    @property
    def aceptado(self) -> str:
        """Gets the aceptado of this Usuario.

        El campo **aceptado** es un Enum el cual indica si el usuario ha sido aceptado por el administrador del sistema y puede acceder al sistema. Los posibles valores para el enum son: ACEPTADO, RECHAZADO y EN_ESPERA  # noqa: E501

        :return: The aceptado of this Usuario.
        :rtype: str
        """
        return self._aceptado

    @aceptado.setter
    def aceptado(self, aceptado: str):
        """Sets the aceptado of this Usuario.

        El campo **aceptado** es un Enum el cual indica si el usuario ha sido aceptado por el administrador del sistema y puede acceder al sistema. Los posibles valores para el enum son: ACEPTADO, RECHAZADO y EN_ESPERA  # noqa: E501

        :param aceptado: The aceptado of this Usuario.
        :type aceptado: str
        """

        self._aceptado = aceptado

    @property
    def token(self) -> str:
        """Gets the token of this Usuario.

        El **token** requeriddo para la autenticación del usuario  # noqa: E501

        :return: The token of this Usuario.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this Usuario.

        El **token** requeriddo para la autenticación del usuario  # noqa: E501

        :param token: The token of this Usuario.
        :type token: str
        """

        self._token = token
