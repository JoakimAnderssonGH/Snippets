
# Define the process ID you want to check
$strInput = Read-Host -Prompt "Enter the process you want to check"

$processes = Get-Process $strInput -ErrorAction SilentlyContinue
if(!$processes){
    Write-Host "No ID found with name: $strInput"
    return
}

$processes | ForEach-Object{
    $processID = $_.Id
    $processName = $_.Name    

    # Get the TCP connections for the specified process ID
    $connections = Get-NetTCPConnection | Where-Object { $_.OwningProcess -eq $processID }

    # Display the results
    if ($connections) {
        Write-Host "TCP Connections for Process ID $processID, Process Name: $processName"
        $connections | Format-Table -Property LocalAddress, LocalPort, RemoteAddress, RemotePort, State
    }
}

