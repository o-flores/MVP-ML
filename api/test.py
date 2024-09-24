from pickle import load
import pandas as pd
import os
from sklearn.metrics import accuracy_score
from utils import transform_dataset

test_file_path = os.path.join('data', 'test.csv')
pipeline_path = os.path.join('data', 'pipeline.pkl')


def convert_column_to_numeric(column):
    return pd.to_numeric(column, errors='coerce')


def test_pipeline():
    raw_dataset = pd.read_csv(test_file_path, delimiter=',',  index_col=0)
    transformed_dataset = transform_dataset(raw_dataset)

    array = transformed_dataset.values
    
    X = array[:, :-1] 
    Y = array[:, -1]   

    loaded_pipeline = load(open(pipeline_path, 'rb'))
    predictions_pipeline = loaded_pipeline.predict(X)
    accuracy = accuracy_score(Y, predictions_pipeline)
    assert accuracy > 0.80


