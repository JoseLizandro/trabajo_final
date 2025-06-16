# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 18:37:29 2025

@author: PC
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(X, y, output_path='model.pkl'):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    joblib.dump(model, output_path)
    return model
