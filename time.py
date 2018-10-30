#this shows the time required from one place to another
import os
import googlemaps
from datetime import datetime
api_key='Your API Key'
FROM='Avenue Road, Bengaluru, KA 560002'
TO='kerekodi, Bengaluru, KA 560085'
gm=googlemaps.Client(key=api_key)
now=datetime.now()
direction_res=gm.directions(FROM,TO,mode="driving",departure_time=now)
time_to_home =  direction_res[0]['legs'][0]['duration_in_traffic']['text']
print(time_to_home)
