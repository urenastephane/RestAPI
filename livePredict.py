import flask
import time
from requests import post
import re, json, requests
#define route
url="http://localhost:50111/api"
#test data instance
d={'code':'A','place':'55673','sequence':'2','date':'2018-03-24 18:00:00'}
#measure speed of execution for real time applications constraints
start_time = time.time()
#put data into json format and make a POST request with the url defined and the json
data=json.dumps(d)
r= post(url,data)
print("EXECUTION TIME : ")
print("--- %s seconds ---" % (time.time() - start_time))
print("PREDICTION : ")
print(r.json())
