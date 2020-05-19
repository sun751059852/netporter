# -*- coding: utf-8 -*-
#ep
import json

from flask import Blueprint, request

from service.endpoints_service import Endpoints

ep = Blueprint('ep',__name__)

endpoints = Endpoints()


@ep.route('/', methods=['POST'])
def add_endpoint():
    body = str(request.data, encoding = "utf-8")
    json_body = json.loads(body)
    endpoints.add_endpoint((json_body['ip'], json_body['port'], json_body['name'], '2020-5-16'))
    return '添加端点'
