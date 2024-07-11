# Rount/routes.py

from flask import Blueprint,  jsonify,request
from models import  CRUD

rount_delete = Blueprint('rount_delete', __name__)


@rount_delete.route('/delete', methods=['POST'])
def reads():
    data = request.json
    range_name = data.pop('range')
    result = CRUD.delete_data(range_name)
    return jsonify(result)

