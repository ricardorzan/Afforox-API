# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.negocio import Negocio  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSucursalController(BaseTestCase):
    """SucursalController integration test stubs"""

    def test_registrar_sucursal(self):
        """Test case for registrar_sucursal

        Registra una sucursal
        """
        body = Negocio()
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
