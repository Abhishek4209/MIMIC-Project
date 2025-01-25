import pandas as pd
import numpy as np
import os 
import sys
from src.logger import logging 
from src.exception import CustomException
from dataclasses import dataclass

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder



## Data Transformation Config Class:
@dataclass
class DataTransformationConfig():
    preprocessing_obj_file_path=os.path.join('artifacts','preprocessing.pkl')
    
## Data Transformation Class:

class DataTransformation():
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        