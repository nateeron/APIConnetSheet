from flask import Flask, request, jsonify, redirect, url_for
from google.oauth2 import service_account
from googleapiclient.discovery import build
import os
from flask_cors import CORS
from Route.sheetCreate import rount_create
from Route.sheetRead import rount_read
from Route.sheetUpdate import rount_update
from Route.sheetDelete import rount_delete

from Route_menuList.sheetCreate import rount_create_menu
from Route_menuList.sheetRead import rount_read_menu
from Route_menuList.sheetUpdate import rount_update_menu
from Route_menuList.sheetDelete import rount_delete_menu

app = Flask(__name__)
CORS(app) 

@app.route('/', methods=['GET'])
def run():
  
    return "OK Run..."

# app.register_blueprint(rount_bp, url_prefix='/rount')
app.register_blueprint(rount_create)
app.register_blueprint(rount_read)
app.register_blueprint(rount_update)
app.register_blueprint(rount_delete)

app.register_blueprint(rount_create_menu,url_prefix='/menu')
app.register_blueprint(rount_read_menu,url_prefix='/menu')
app.register_blueprint(rount_update_menu,url_prefix='/menu')
app.register_blueprint(rount_delete_menu,url_prefix='/menu')


if __name__ == '__main__':
    app.run(debug=True)
