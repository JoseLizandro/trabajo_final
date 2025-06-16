# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 18:40:58 2025

@author: PC
"""

import joblib

def predict_model(X, model_path='model.pkl'):
    model = joblib.load(model_path)
    return model.predict(X)
