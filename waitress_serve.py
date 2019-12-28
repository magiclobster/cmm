#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import signal

from waitress import serve
from backup_status import app


def receive_signal(sig_number, frame):
    print(f'received signal: {sig_number}, shutting down server')
    os.kill(1, signal.SIGINT)
    return


if __name__ == '__main__':
    signal.signal(signal.SIGTERM, receive_signal)
    serve(app, host=os.getenv('BIND_IP', '127.0.0.1'), port=int(os.getenv('BIND_PORT', 8199)))
