# Rount/routes.py

from flask import Blueprint,  jsonify,request
from models import  CRUD

rount_update_menu = Blueprint('rount_update_menu', __name__)


def remove_key(d, key):
        return {k: v for k, v in d.items() if k != key}
    
@rount_update_menu.route('/update', methods=['POST'])
def updates():
    data = request.json
    i = data['i']
    range_name = data.pop('range')
    values = [list(remove_key(data, 'i').values())]
    body = {
        'values': values
    }
    
    result = CRUD.Menu_update_data(i,range_name,body)
    return jsonify(result)

