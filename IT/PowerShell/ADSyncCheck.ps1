<#
This is AD Sync check script.
No Details, only important commands and what they do (or expected output)
#>

# Get summary of AD Replication across AD forest: Fast & Easy
repadmin /replsummary

# Apply Force Replication of AD
repadmin /syncall /e

# Get Online/Offline status of DCs
Get-ADDomainController -Filter * | Select hostname, site

# Testing Connection Status
$DC = Get-ADDomainController -Filter *
foreach ($DomainController in $DC){
$DcName = $DomainController.Name
$Status = Test-Connection -ComputerName $DomainController.Hostname -Count 1 -Quiet
if ($Status){
$StatusText = "Online"
}else{
$StatusText = "Offline"
}

Write-Output "$DcName is $StatusText"
}

# Time Sync Check

## Get NTP Server
w32tm /query /source

## Last time Sync Check
w32tm /query /status

## Time offset - last 3 sample check
w32tm /stripchart /computer:<ip> /dataonly samples:3

# Adjust time
Set-Date -Adjust (New-TimeSpan -Seconds 3) # to add 3 seconds (put -3 for reducing 3 seconds)
Set-Date -Adjust (New-TimeSpan -Minutes 2 -Seconds 3) # to add specific minutes and seconds

# To completely rediscover time/date
w32tm /resync /rediscover
