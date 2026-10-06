Get-Content "lists.txt" | ForEach-Object { Start-Process $_ python.exe }
