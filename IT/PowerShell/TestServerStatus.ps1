Test-NetConnection -computername <IP>  

# To return just True or False 
Test-NetConnection -computername <IP>  -Quiet 

# To specify port number
Test-NetConnection -computername <IP>  -port <port #>
