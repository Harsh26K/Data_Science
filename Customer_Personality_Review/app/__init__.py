from flask import Flask
import pickle

app = Flask(__name__)
app.config['SECRET_KEY'] = '5073a7594ddec9d863ecc03aa8edc161'

with open(f'./app/cpr_gmm.pkl', 'rb') as f:
    model_gmm = pickle.load(f)


with open(f'./app/cpr_kmeans.pkl', 'rb') as f:
    model_kmeans = pickle.load(f)

with open(f'./app/association.pkl','rb') as f:
    model_association = pickle.load(f)

from app.main.routes import main
from app.predict_cluster.routes import clusters
from app.predict_association.routes import association
from app.utils.utils import utils

app.register_blueprint(main)
app.register_blueprint(clusters)
app.register_blueprint(association)
app.register_blueprint(utils)