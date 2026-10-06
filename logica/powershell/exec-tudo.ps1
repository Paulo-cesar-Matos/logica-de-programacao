Get-Content "lists.txt" | ForEach-Object { Start-Process $_ }
