•	To know .Net framework 
Get-ChildItem 'HKLM:\SOFTWARE\conectMicrosoft\NET Framework Setup\NDP' -Recurse | Get-ItemProperty -Name version -EA 0 | Where { $_.PSChildName -Match '^(?!S)\p{L}'} | Select PSChildName, version
