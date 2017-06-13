@REM "moving older engough files to backup folder"
@ECHO OFF
forfiles /P "D:\Desktop\Work\文档\Mine Docs" /D -30 /C "com /C move @file D:\Desktop\Work\文档\近期不用"
echo "moving done"
pause