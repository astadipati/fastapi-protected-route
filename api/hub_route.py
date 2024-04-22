from fastapi.routing import APIRouter
from config.auth import verified_user, authorize, pwd_context, create_access_jwt, create_refresh_token
from schemas.user import User, UserGet, UserPost, UserLogin
from fastapi import Depends, status, HTTPException
from config.settings import Config
from datetime import datetime, timedelta
import statistics
import pandas as pd
from pymongo import MongoClient


hub_router = APIRouter(prefix='/api/v1', tags=['Hub Capacity'])

@hub_router.get('/hub_capacity')
async def refresh(token_data:dict = Depends(verified_user)):
    return "hub capacity"

@hub_router.get('/pump-internet/{state}/{interface}')
async def oss_pump_internet( state: str, interface:str, data : dict = Depends(verified_user)):
    try:
        date = datetime.now()
        st = date.replace(hour=0, minute=0, microsecond=0)
        db = MongoClient(Config.MONGO_URL)
        col = db['N3']['data_hub_capacity_ansible']
        data_dict=[]
        for x in col.find({"state":state,"interface":interface,"date_created": {"$gte": st}}).sort("_id", -1):
            data_dict.append(x)
        df = pd.DataFrame(data_dict)
        
        limit = int(len(df))-1

        val_tx = []
        val_rx = []
        for i in range(limit):
            # tx = round(
            #     (((df["tx"][i]-df["tx"][i+1])*8)/60/1024/1024), 4)
            # val_tx.append(tx)
            rx = round(
                (((df["rx"][i]-df["rx"][i+1])*8)/60/1024/1024), 4)
            val_rx.append(rx)
        # print(val_tx)
        # temp_do = [x for x in val_tx[0:5]]
        temp_up = [x for x in val_rx[0:5]]
        # print (temp_do)
        tot_capacity = 5010
        # mean_do = statistics.mean(temp_do)
        # print(int(mean_do))
        mean_up = statistics.mean(temp_up)
        # print(int(mean_up))
        # pump_tx = int(tot_capacity-mean_do)
        pump_rx = int(tot_capacity-mean_up)
        # print(pump_tx)
        # print(pump_rx)
        data_log = {
            "state":"upload",
            "value": pump_rx,
            "date":date
        }
        return data_log
        
        # print(conn)
    except Exception as e:
        raise e