from flask import Blueprint,send_from_directory
from app import app

utils = Blueprint('utils', __name__)


import logging
logging.basicConfig(filename='./app/log_info.log',level=logging.DEBUG,filemode='w',
                    format='%(asctime)s:%(levelname)s:%(message)s')


@utils.route("/download_file/<path:filename>",methods=['GET','POST'])
def download_file(filename):
    uploads = app.root_path
    return send_from_directory(directory=uploads,path=filename)