# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class NegocioArray(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, negocio_id: int=None, foto_perfil: str=None):  # noqa: E501
        """NegocioArray - a model defined in Swagger

        :param negocio_id: The negocio_id of this NegocioArray.  # noqa: E501
        :type negocio_id: int
        :param foto_perfil: The foto_perfil of this NegocioArray.  # noqa: E501
        :type foto_perfil: str
        """
        self.swagger_types = {
            'negocio_id': int,
            'foto_perfil': str
        }

        self.attribute_map = {
            'negocio_id': 'negocioId',
            'foto_perfil': 'fotoPerfil'
        }
        self._negocio_id = negocio_id
        self._foto_perfil = foto_perfil

    @classmethod
    def from_dict(cls, dikt) -> 'NegocioArray':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The negocio-array of this NegocioArray.  # noqa: E501
        :rtype: NegocioArray
        """
        return util.deserialize_model(dikt, cls)

    @property
    def negocio_id(self) -> int:
        """Gets the negocio_id of this NegocioArray.


        :return: The negocio_id of this NegocioArray.
        :rtype: int
        """
        return self._negocio_id

    @negocio_id.setter
    def negocio_id(self, negocio_id: int):
        """Sets the negocio_id of this NegocioArray.


        :param negocio_id: The negocio_id of this NegocioArray.
        :type negocio_id: int
        """

        self._negocio_id = negocio_id

    @property
    def foto_perfil(self) -> str:
        """Gets the foto_perfil of this NegocioArray.

        Binary data of the media file  # noqa: E501

        :return: The foto_perfil of this NegocioArray.
        :rtype: str
        """
        return self._foto_perfil

    @foto_perfil.setter
    def foto_perfil(self, foto_perfil: str):
        """Sets the foto_perfil of this NegocioArray.

        Binary data of the media file  # noqa: E501

        :param foto_perfil: The foto_perfil of this NegocioArray.
        :type foto_perfil: str
        """

        self._foto_perfil = foto_perfil
