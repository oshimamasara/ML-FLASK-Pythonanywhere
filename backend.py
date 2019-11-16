import pickle
from sklearn.preprocessing import PolynomialFeatures
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
saved_model = os.path.join(THIS_FOLDER, 'model3.pkl')

def days_feet(day):
    #model = pickle.load(open('model3.pkl','rb'))
    model = pickle.load(open(saved_model,'rb'))
    poly_reg = PolynomialFeatures(degree = 6)
    test_data = poly_reg.fit_transform([[day]])
    output = model.predict(test_data)
    return int(output)
