#import numpy as np
#from flask import Flask, request, jsonify
import pickle
from sklearn.preprocessing import PolynomialFeatures

def days_feet(day):
    model = pickle.load(open('model3.pkl','rb'))
    poly_reg = PolynomialFeatures(degree = 6)
    test_data = poly_reg.fit_transform([[day]])
    output = model.predict(test_data)
    return int(output)

#model = pickle.load(open('model.pkl','rb'))
#
#def meters_feet(meter, coefficient = 3.28084):
#    prediction = model.predict([[np.array(data[meter])]])
#    output = prediction[0]
#    return output
    #return meters * coefficient


#def predict():
#    data = request.get_json(force=True)
#    prediction = model.predict([[np.array(data['exp'])]])
#    output = prediction[0]
#    return jsonify(output)