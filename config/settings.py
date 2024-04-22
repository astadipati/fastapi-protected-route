from dotenv import find_dotenv, dotenv_values
from typing import List
from datetime import timedelta
from pymongo import MongoClient

env_path = find_dotenv()

config = dotenv_values(env_path)

class Config:
    def __init__(self, cfg):
        self.config = cfg
        
    DB_URL: str = config['DB_URL']
    DB_MODELS: List[str] = ['models.user']
    SECRET: str='ce98bfa084c9afe1b2b121e7c028607e0e5883878f08f57fa67f0f667b39c6e0'
    ALGORITHM: str='HS256'
    JWT_ACCESS_EXP: timedelta = timedelta(days=1)
    JWT_REFRESH_EXP: timedelta = timedelta(days=365)
    
    # def connectMongo(self):
    #     return MongoClient(self.config['URLMONGO'])
    MONGO_URL: str = config['URLMONGO']
    
    
    