import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()
host=os.getenv('host')
user=os.getenv('user')
password=os.getenv('password')
db=os.getenv('db')

def read_sql_data():
    logging.info("Reading Sql database started")
    
    try:
        mydb= pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connected with db", mydb)
        df = pd.read_sql_query('select * from students', mydb)
    except Exception as e:
        raise CustomException(ex)
    