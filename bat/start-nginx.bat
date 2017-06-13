@ECHO OFF
REM Start Nginx
taskLIST /FI  "IMAGENAME eq nginx.exe" 2>NUL | find /I /N "nginx.exe" >NUL
IF NOT "%ERRORLEVEL%" == "0" (
	REM Nginx is Not running, so start it
	e: 
	cd E:\software\nginx-1.10.2
	start nginx.exe
	ECHO Nginx Started.
) ELSE (
	ECHO Nginx is already running
)