from flask import Blueprint,  jsonify,request
from models import  CRUD

rount_create = Blueprint('rount_create', __name__)

@rount_create.route('/create', methods=['POST'])
def creates():
    data = request.json
    print("********************** DATA *************************")
    print(data)
    print(type(data) )
    values = []
    if isinstance(data, list):
        values = [list(item.values()) for item in data]
    else:
        values = [list(data.values())]
    body = {
        'values': values
    }
    
  
    result = CRUD.create_data(body)
    return jsonify(result)