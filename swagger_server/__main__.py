#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from swagger_server.data.extensions import jwt


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')

    app.app.config["JWT_SECRET_KEY"] = "Blah!"
    jwt.init_app(app.app)

    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Afforox'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
