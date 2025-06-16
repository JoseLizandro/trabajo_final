# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 18:40:04 2025

@author: PC
"""

import matplotlib.pyplot as plt
import seaborn as sns

def plot_corr_matrix(df):
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Matriz de Correlación')
    plt.show()
