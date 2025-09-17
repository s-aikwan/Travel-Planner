import requests
import json
from datetime import datetime
import os
class MapCalculator:

    def __init__(self):
        pass

    def get_flight_data(self):
        if os.path.exists("flight_data.json"):
            with open("flight_data.json","r", encoding="utf-8") as f:
                last_date = datetime.fromisoformat(json.loads(f.read())["timestamp"])
                cur_time = datetime.now()
                time_dif = cur_time-last_date
                total_hours = time_dif.total_seconds()/3600
                if total_hours < 6:
                    print("No need to update")
                    return
        url = "https://api.aviationstack.com/v1/flights?access_key=98c7847be4c43b70b1feac7b16cdf705"
        response = requests.get(url)
        if response.status_code == 200:
            saved_data = {
                "timestamp": datetime.now().isoformat(),
                "flight_data": response.json()
            }
            
            with open("flight_data.json","w") as f:
                json.dump(saved_data, f, indent=4)
            
        else:
            return None

class node:
    def __init__(self,name,location):
        self.name:str = name
        self.location: tuple[float,float] = location
        self.edges:set = set()

class edges:
    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost