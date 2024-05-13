# Run PS as Admin
Write-EventLog -LogName System -Source User32 -EventId 1076 -Message "logged off" -Category 0 (none)
