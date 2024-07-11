from flask import Blueprint,  jsonify,request
from models import  CRUD

rount_create_menu = Blueprint('rount_create_menu', __name__)

def remove_key(d, key):
        return {k: v for k, v in d.items() if k != key}


@rount_create_menu.route('/create', methods=['POST'])
def creates():
    data = request.json
    print("********************** DATA *************************")
    print(data)
    print(type(data) )
    values = []
    i = 0
    if isinstance(data, list):
        values = [list(remove_key(item, 'i').values()) for item in data]
        i = data[0]['i']
    else:
        values = [list(remove_key(data, 'i').values())]
        i = data['i']
    body = {
        'values': values
    }
    
    result = CRUD.Menu_create_data(body,str(i))
    return jsonify(result)