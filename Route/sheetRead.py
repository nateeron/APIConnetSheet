# Rount/routes.py

from flask import Blueprint,  jsonify
from models import  CRUD

rount_read = Blueprint('rount_read', __name__)


@rount_read.route('/read', methods=['GET'])
def reads():
    result = CRUD.read_data()
    return jsonify(result)

