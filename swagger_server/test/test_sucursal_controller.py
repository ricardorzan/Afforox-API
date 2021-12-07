# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.sucursal import Sucursal  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSucursalController(BaseTestCase):
    """SucursalController integration test stubs"""

    def test_obtener_sucursal(self):
        """Test case for obtener_sucursal

        Obtiene una sucursal
        """
        response = self.client.open(
            '/Afforox//negocios/{negocioId}/sucursales/{sucursalId}'.format(negocio_id=56, sucursal_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_registrar_sucursal(self):
        """Test case for registrar_sucursal

        Registra una sucursal
        """
        body = Sucursal()
        response = self.client.open(
            '/Afforox//negocios/{negocioId}/sucursales'.format(negocio_id='negocio_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
