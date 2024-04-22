from dotenv import find_dotenv, dotenv_values
from typing import List
from datetime import timedelta
from pymongo import MongoClient

env_path = find_dotenv()

config = dotenv_values(env_path)

class Config:
    
    DB_URL: str = config['DB_URL']
    DB_MODELS: List[str] = ['models.user']
    SECRET: str='1cb4debd82fcf0c6f31d1cccfce4f1c9117a0cad21b71d5c2eab1c050e878701'
    ALGORITHM: str='HS256'
    JWT_ACCESS_EXP: timedelta = timedelta(days=1)
    JWT_REFRESH_EXP: timedelta = timedelta(days=365)
    
    MONGO_URL: str = config['URLMONGO']
    
    
    