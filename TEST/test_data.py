# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 18:43:54 2025

@author: PC
"""

from src.data.make_dataset import load_data

def test_load_data():
    df = load_data("data/raw/credit_data.csv")
    assert not df.empty
