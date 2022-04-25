import os
from uuid import uuid4

from flask import Flask

app = Flask(__name__)

HOSTNAME = f'replicatedApi-{uuid4()}'


@app.route('/', methods=['GET'])
def index():
    return f'Hello - I am {HOSTNAME}'


if __name__ == '__main__':
    app.run()
