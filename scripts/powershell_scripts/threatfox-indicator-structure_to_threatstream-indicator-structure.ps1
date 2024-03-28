$recent_indicators = Get-Content .\14032024_212238_threatfox_recent.json | ConvertFrom-Json
#$recent_indicators.data[0]
$indicator_count = $recent_indicators.data | Measure-Object 
#$recent_data
$i_count = $indicator_count | Select-Object -Property Count | Select-Object -Expand Count
#$i_count
$recent_indicators.data[0..$i_count]
#foreach ($name) in ($names)
