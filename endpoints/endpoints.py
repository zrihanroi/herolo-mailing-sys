import json
from flask import Blueprint, request, Response
import os
from endpoints_utils.handlers import write, get_messages, get_message_by_id, delete

# General vars:
LOCAL_TEST_API_KEY = "RXEG4tF6LmTpW0Cw8gxq"
API_KEY = os.environ.get("API_KEY" , LOCAL_TEST_API_KEY)


endpoints = Blueprint('endpoints', __name__)

@endpoints.route('/handle-message' , methods = ['POST' , 'GET' , 'DELETE'])
def my_api():
    data = request.json
    api_key = data.get("api_key","")
    if api_key != API_KEY:
        return Response(status=403, response="Please provide a valid api_key parameter.")

    if request.method == 'POST':
        response_bundle = write(data)
        return Response(status= response_bundle.get("status",""), response=response_bundle.get("response",""))

    if request.method == 'DELETE':
        response_bundle = delete(data)
        return Response(status= response_bundle.get("status",""), response=response_bundle.get("response",""))

    if request.method == 'GET':
        if data.get("method","") == "GET ALL":
            response_bundle = get_messages(data)
            return Response(status=response_bundle.get("status",""),
                            response=json.dumps(response_bundle.get("response","")))

        if data.get("method","") == "GET UNREAD":
            response_bundle = get_messages(data, only_unread= True)
            return Response(status=response_bundle.get("status",""),
                            response=json.dumps(response_bundle.get("response","")))

        if data.get("method","") == "GET BY ID":
            response_bundle = get_message_by_id(data)
            return Response(status=response_bundle.get("status",""),
                            response=json.dumps(response_bundle.get("response","")))

