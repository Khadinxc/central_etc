#below is the curl version of the request, curl is just an alias for Invoke-WebRequest it's better to use Invoke-RestMethod since it's an API we're interacting with
# curl -Method POST https://threatfox-api.abuse.ch/api/v1/ -Body $Body
#
#below is a list of bodies to replace the below script with or build your own queries
#
#Query recent IOCs
# { "query": "get_iocs", "days": 7 }
#
#Query an IOC by ID
# { "query": "ioc", "id": 41 }
# Search an IOC
# { "query": "search_ioc", "search_term": "139.180.203.104" }
#
# Search for IOCs by file hash
# { "query": "search_hash", "hash": "2151c4b970eff0071948dbbc19066aa4" }
#
# Query tag
# { "query": "taginfo", "tag": "Magecart", "limit": 10 }
#
# Query malware
# { "query": "malwareinfo", "malware": "Cobalt Strike", "limit": 10 }
#
#I've rewritten the curl command provided by threatfox to work for powershell as I've been unable to find it online.
$Body = '{ "query": "get_iocs", "days": 7 }'
$Time = Get-Date -Format "ddMMyyyy_HHmmss"

Invoke-RestMethod -Method 'POST' -Uri https://threatfox-api.abuse.ch/api/v1/ -Body $Body | ConvertTo-Json | Out-File -FilePath ".\$($Time)_threatfox_recent.json"


