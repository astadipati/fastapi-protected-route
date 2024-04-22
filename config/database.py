import mysql.connector as mysql
from pymongo import MongoClient

class Config:
    def __init__(self, cfg):
        self.config = cfg
        
    def connectMongo(self):
        return MongoClient(self.config['URLMONGO'])