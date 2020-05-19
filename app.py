# coding:utf-8
from flask import Flask

from api.endpoints_api import ep

app=Flask(__name__)
app.register_blueprint(ep,url_prefix='/ep')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)