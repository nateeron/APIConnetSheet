# Rount/routes.py

from flask import Blueprint,  jsonify,request
from models import  CRUD

rount_read_menu = Blueprint('rount_read_menu', __name__)


@rount_read_menu.route('/read', methods=['GET'])
def reads():
    data = request.json
    i = data['i']
    print("--------------------------------------------------- data  : ",i)
    result = CRUD.Menu_read_data(str(i))
    return jsonify(result)

