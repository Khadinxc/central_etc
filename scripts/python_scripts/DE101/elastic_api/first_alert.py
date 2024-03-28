#Created for during TCM Academy Detection Engineering 101 course
import requests
import os

url = "https://591f836b7e854b68a51f2db3db3999df.us-central1.gcp.cloud.es.io:9243/api/detection_engine/rules"
api_key = os.environ['ELASTIC_KEY']
headers = {
    'Content-Type': 'application/json;charset=UTF-8' ,
    'kbn-xsrf': 'true', 
    'Authorization': 'ApiKey ' + api_key
}

data = """
{
  "rule_id": "process_started_by_ms_office_program",
  "risk_score": 50,
  "description": "Process started by MS Office program - possible payload",
  "interval": "1h", 
  "name": "Khadinxc Test Rule",
  "severity": "low",
  "tags": [
   "child process",
   "ms office"
   ],
  "type": "query",
  "from": "now-70m", 
  "query": "process.parent.name:EXCEL.EXE or process.parent.name:MSPUB.EXE or process.parent.name:OUTLOOK.EXE or process.parent.name:POWERPNT.EXE or process.parent.name:VISIO.EXE or process.parent.name:WINWORD.EXE",
  "language": "kuery",
  "filters": [
     {
      "query": {
         "match": {
            "event.action": {
               "query": "Process Create (rule: ProcessCreate)",
               "type": "phrase"
            }
         }
      }
     }
  ],
  "enabled": true
}
"""

elastic_data = requests.post(url, headers=headers, data=data).json()
print(elastic_data)