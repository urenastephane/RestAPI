import flask
import time
from requests import post
import re, json, requests
url="http://localhost:50111/api"
#test data
d={'code':'A','place':'55673','sequence':'2','date':'2018-03-24 18:00:00'}
start_time = time.time()
data=json.dumps(d)
r= post(url,data)
print("EXECUTION TIME : ")
print("--- %s seconds ---" % (time.time() - start_time))
print("PREDICTION : ")
print(r.json())
