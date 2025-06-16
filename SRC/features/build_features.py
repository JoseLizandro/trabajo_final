# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 18:35:40 2025

@author: PC
"""

def build_features(df):
    # Aquí podrías normalizar o transformar columnas si fuera necesario
    return df[['edad', 'ingresos', 'deuda', 'historia_credito', 'score_buro']]
