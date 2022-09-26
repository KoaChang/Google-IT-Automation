import os
import requests

path = 'data/feedback'
keys = ['title','name','date','feedback']
for filename in os.listdir(path):
    dic = {}
    with open(os.path.join(path,filename)) as file:
        index = 0
        for line in file:
            line = line.strip()
            key = keys[index]
            dic[key] = line
            index+=1
    response = requests.post("http://34.134.156.225/feedback/", data=dic)
    if response.status_code == 201:
        print("success")
    else:
        print('failure')
