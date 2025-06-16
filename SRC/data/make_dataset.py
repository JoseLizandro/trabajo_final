# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 18:34:24 2025

@author: PC
"""
import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def clean_data(df):
    df = df.dropna()
    return df

