# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 18:44:22 2025

@author: PC
"""

from src.models.train_model import train_model
import pandas as pd

def test_model_training():
    df = pd.read_csv(DATA/credit_data.csv)
    X = df[['edad', 'ingresos', 'deuda', 'historia_credito', 'score_buro']]
    y = df['default']
    model = train_model(X, y, output_path="model_test.pkl")
    assert model is not None
