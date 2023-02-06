from flask import render_template, Blueprint

main = Blueprint('main', __name__)


import logging
logging.basicConfig(filename='./app/log_info.log',level=logging.DEBUG,filemode='w',
                    format='%(asctime)s:%(levelname)s:%(message)s')

@main.route('/')
@main.route('/landing')
def landing():
    logging.info('starting landing page')
    return render_template('landing.html',title='landing_page')

@main.route('/home')
def home():
    logging.info('starting home page')
    return render_template('home.html',title='home')

@main.route("/about")
def about():
    return render_template('about.html', title='about')