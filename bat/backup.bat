@REM "moving older engough files to backup folder"
@ECHO OFF
forfiles /P "D:\Desktop\Work\�ĵ�\Mine Docs" /D -30 /C "cmd /C move @file D:\Desktop\Work\�ĵ�\���ڲ���"
echo "moving done"
pause