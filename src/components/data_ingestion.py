import os
import sys
from src.exception import CustomExeption
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self) -> None:
        self.Ingestion_Config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info('Entered Data Ingestion method or componenent')
        try:
            df=pd.read_csv('notebook\Data\Stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.Ingestion_Config.train_data_path),exist_ok=True)

            df.to_csv(self.Ingestion_Config.raw_data_path,index=False,header=True)

            logging.info('Train test split Initiated')
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.Ingestion_Config.train_data_path,index=False,header=True)
            test_set.to_csv(self.Ingestion_Config.test_data_path,index=False,header=True)

            logging.info('Data Ingestion complited')
            return(
                self.Ingestion_Config.train_data_path,
                self.Ingestion_Config.test_data_path
            ) 
        except Exception as e:
            raise CustomExeption(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()