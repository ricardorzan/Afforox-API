# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.negocio import Negocio  # noqa: E501
from swagger_server.test import BaseTestCase


class TestNegocioController(BaseTestCase):
    """NegocioController integration test stubs"""

    def test_get_negocio_by_id(self):
        """Test case for get_negocio_by_id

        Obtiene la información de un negocio particular
        """
        response = self.client.open(
            '/Afforox//negocios/{negocioId}'.format(negocio_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_negocios(self):
        """Test case for get_negocios

        Obtiene todos los negocios
        """
        query_string = [('salto', 0),
                        ('limite', 25),
                        ('filtro', 'filtro_example')]
        response = self.client.open(
            '/Afforox//negocios',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_registrar_negocio(self):
        """Test case for registrar_negocio

        Registra un negocio
        """
        body = Negocio()
        response = self.client.open(
            '/Afforox//negocios',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
