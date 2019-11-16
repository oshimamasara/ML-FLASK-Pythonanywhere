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
