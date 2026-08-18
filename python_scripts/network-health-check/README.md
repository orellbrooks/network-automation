# Network Device Health Check Tool

A light Python automation script that SSHs into Cisco IOS network devices using **Netmiko**, pulls operational data, and parses CLI output using native Python string manipulation.

## Features
- **Pure Python Parsing**: Parses `show ip interface brief` using `.splitlines()` and `.split()` string methods without external dependencies like Genie or TextFSM.
- **Dynamic Status Extraction**: Correctly handles single-word (`down`) and multi-word (`administratively down`) statuses using list slicing (`parts[4:-1]`).
- **Secure Authentication**: Uses `getpass` to prompt for SSH credentials, avoiding hardcoded passwords.
- **Error Handling**: Gracefully catches SSH timeout (`NetmikoTimeoutException`) and auth failure (`NetmikoAuthenticationException`).

## Prerequisites & Installation
1. Python 3.8+ installed
2. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/network-health-check.git](https://github.com/YOUR_USERNAME/network-health-check.git)
   cd network-health-check