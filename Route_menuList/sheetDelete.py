# Rount/routes.py

from flask import Blueprint,  jsonify,request
from models import  CRUD

rount_delete_menu = Blueprint('rount_delete_menu', __name__)


@rount_delete_menu.route('/delete', methods=['POST'])
def reads():
    data = request.json
    range_name = data.pop('range')
    i = data['i']
    result = CRUD.Menu_delete_data(i,range_name)
    return jsonify(result)

