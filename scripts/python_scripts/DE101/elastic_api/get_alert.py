#Created for during TCM Academy Detection Engineering 101 course
import requests
import os

#This script pulls certain alerts from elastic via an api get request.

url = "https://591f836b7e854b68a51f2db3db3999df.us-central1.gcp.cloud.es.io:9243/api/detection_engine/rules?rule_id="
id = "1dee0xxx-xxxx-44ca-b24b-4a285d7b6ba1"
full_path = url + id

api_key = os.environ['ELASTIC_KEY']
headers = {
    'Content-Type': 'application/json;charset=UTF-8' ,
    'kbn-xsrf': 'true', 
    'Authorization': 'ApiKey ' + api_key
}

elastic_data = requests.get(full_path, headers=headers).json()
print(elastic_data)