# Rount/routes.py

from flask import Blueprint,  jsonify,request
from models import  CRUD

rount_update = Blueprint('rount_update', __name__)

datatest = {
    "range": "Sheet1!A2:B2",
    "name": "John Doe",
    "email": "john.doe@example.com"
}

@rount_update.route('/update', methods=['POST'])
def updates():
    data = request.json
    range_name = data.pop('range')
    values = [list(data.values())]
    body = {
        'values': values
    }
    result = CRUD.update_data(range_name,body)
    return jsonify(result)

