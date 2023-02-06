from sklearn.preprocessing import StandardScaler, normalize
from app import model_kmeans,model_gmm

import logging
logging.basicConfig(filename='./app/log_info.log',level=logging.DEBUG,filemode='w',
                    format='%(asctime)s:%(levelname)s:%(message)s')

def predict_clusters(data2,ml_model):
    data = data2
    logging.info('data gathered')
    final_features = data[['Income','Relation','TotalAmtSpent']].astype('int64')
    sc = StandardScaler()
    scaled_features = sc.fit_transform(final_features)
    logging.info('data standardized')
    norm_features = normalize(scaled_features,norm='l2')
    logging.info('data normalized')
    if ml_model=="K-means":
        logging.info('using kmeans clustering')
        prediction = model_kmeans.predict(norm_features)
        logging.info('successfully predicted')
        data['Cluster'] = prediction
        data = data.replace({0:'Platinum',1:'Diamond',2:'Ace',3:'Gold'})
    elif ml_model=="Gaussian Mixtures":
        logging.info('using Gaussian Mixtures clustering')
        prediction = model_gmm.predict(norm_features)
        logging.info('successfully predicted')
        data['Cluster'] = prediction
        data = data.replace({0:'Platinum',1:'Diamond',2:'Gold',3:'Ace'})
    return data