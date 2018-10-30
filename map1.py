#this is just to find the status of a location
import os
import googlemaps
api_key='use your API'
gm=googlemaps.Client(key=api_key)
geocode_result=gm.geocode('hosakerehalli')[0]
print(geocode_result)
