from src.logger import logging
from src.exceptions import CustomException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
import pandas as pd
import os 
import sys


@dataclass
## Data Ingestion Config class:
class DataingestionConfig():
    raw_data_path=os.path.join('artifacts','raw.csv')
    train_data_path=os.path.join('artifacts','train.csv')
    test_data_path=os.path.join('artifacts','test.csv')


## Data Ingestion Class:
class Dataingestion():
    def __init__(self):
        self.data_ingestion_config=DataingestionConfig()
    
    
    def initiate_data_ingestion(self):
        logging.info('Data Ingestion class is Started')
        
        try:
            df=pd.read_csv(os.path.join('notebooks/data','.csv'))
            logging.info('Datasets read as pandas DataFrame')
            
            
            os.makedir(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info('Train test split')
            
            train_set,test_set=train_test_split(df,test_size=0.25,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False)
            test_set.to_Csv(self.ingestion_config.test_data_path,index=False)
            
            logging.info('Ingestion of Data is Completed')
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )

        except Exception as e:
            logging.info('Some Error Occured into Data Ingestion class')
            raise CustomException(e,sys)
            