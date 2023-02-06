import pandas as pd
from flask import Blueprint, render_template,request
from app.predict_cluster.forms import PredictForm
from app.predict_cluster.utils import predict_clusters


clusters = Blueprint('clusters', __name__)


import logging
logging.basicConfig(filename='./app/log_info.log',level=logging.DEBUG,filemode='w',
                    format='%(asctime)s:%(levelname)s:%(message)s')

@clusters.route('/predict_cluster', methods=['GET', 'POST'])
def predict_cluster():
    form = PredictForm()
    if  request.method == 'GET':
        return render_template('predict_cluster.html',title='predict clusters',form=form,v=False)
    if form.validate_on_submit():
        file_input=request.files['input_file']
        ml_model = form.cluster_model.data
        logging.info('input successful')
        data= pd.read_csv(file_input)
        logging.info('converted to csv')
        output_data = predict_clusters(data,ml_model)
        output_data.to_csv('./app/static/files/predicted_clusters.csv')
        logging.info('output csv file successfully created')
        filename = 'predicted_clusters.csv'
        return render_template('predict_cluster.html',title='predict clusters',form=form,v=True,filename=filename)