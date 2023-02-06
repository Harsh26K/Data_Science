from flask import Blueprint, render_template,request
from app.predict_association.forms import AssociationForm
from app import model_association

association = Blueprint('association', __name__)


import logging
logging.basicConfig(filename='./app/log_info.log',level=logging.DEBUG,filemode='w',
                    format='%(asctime)s:%(levelname)s:%(message)s')

@association.route("/predict_association",methods=['GET','POST'])
def predict_association():
    form = AssociationForm()
    if request.method == 'GET':
        return render_template('association.html',title='predict association',form=form,v = False)
    if form.validate_on_submit():
        product = form.product.data
        segment = form.segment.data
        logging.info('input successful')
        target = '{\'%s_seg_%s\'}' %(product,segment)
        output = model_association[model_association['consequents'].astype(str).str.contains(target, na=False)].sort_values(by='confidence', ascending=False)
        logging.info('creating output')
        first,second = segment.split(' ')
        filename = product +'_'+ first + '_' + second + '.xlsx'
        output.to_excel('./app/static/files/'+filename,index=False)
        logging.info('output file created successfully')
        return render_template('association.html',title='predict association',form=form,v=True,file=filename)