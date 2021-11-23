:: This Batch file will run the sortDownloads.py simply by typing "Win + R" then "sortDownloads"
@py.exe "C:/Users/liami/Automation Scripts/sortDownloads.py"

:: Adds "Press any key to continue...", prevents window from disappearing too quickly
@pause

:: Scheduling Tasks
:: EX, 'security script' to run every 20 mins: schtasks /create /sc minute /mo 20 /tn "Security Script" /tr \\central\data\scripts\sec.vbs
:: To delete a scheduled task: schtasks /delete /tn {TaskName | *} 