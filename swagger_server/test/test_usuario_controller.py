# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.token import Token  # noqa: E501
from swagger_server.models.usuario import Usuario  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUsuarioController(BaseTestCase):
    """UsuarioController integration test stubs"""

    def test_get_usuario(self):
        """Test case for get_usuario

        Obtiene la información de un usuario particular
        """
        response = self.client.open(
            '/Afforox//usuarios/{usuarioId}'.format(usuario_id='usuario_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_login(self):
        """Test case for login

        Iniciar sesión
        """
        query_string = [('username', 'username_example'),
                        ('password', 'password_example')]
        response = self.client.open(
            '/Afforox//usuarios/login',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_nuevo_token(self):
        """Test case for nuevo_token

        Genera un nuevo token de verificación
        """
        query_string = [('username', 'username_example')]
        response = self.client.open(
            '/Afforox//usuarios/nuevo-token',
            method='PATCH',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_usuario(self):
        """Test case for patch_usuario

        Modifica los datos del usuario
        """
        body = Usuario()
        response = self.client.open(
            '/Afforox//usuarios/{usuarioId}'.format(usuario_id='usuario_id_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_registrar_usuario(self):
        """Test case for registrar_usuario

        Registra un nuevo usuario
        """
        body = Usuario()
        response = self.client.open(
            '/Afforox//usuarios',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_validar_usuario(self):
        """Test case for validar_usuario

        Validación del usuario mediante un token de verificación
        """
        query_string = [('username', 'username_example'),
                        ('token', 'token_example')]
        response = self.client.open(
            '/Afforox//usuarios/validacion',
            method='PATCH',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
