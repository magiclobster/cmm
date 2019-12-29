#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from flask import Flask
from configobj import ConfigObj
from cmm.api import api

app = Flask(__name__)

app.register_blueprint(api, url_prefix="/api")


def run_server():
    config = ConfigObj('config/main.config', configspec='config/main.config.spec')
    app.config_obj = config
    app.run(host=os.getenv('BIND_IP', '127.0.0.1'), port=int(os.getenv('BIND_PORT', 8199)), debug=True)


if __name__ == '__main__':
    run_server()
