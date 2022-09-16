# Snowflake Documentation

## Needed installs

### Before starting...

Verify python is installed into your computer and added to the **PATH**

The recommended approach in this case would be to download python manually if it is not installed in the computer.

![Snowflake logo](../img/logo.jpg)

For this task, direct to the link: https://www.python.org/downloads/

### First Step

Install Chocolatey into your computer:
1. Open Powershell with administrative privileges
2. Run the following code:
```bash
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

For more information about this package manager
