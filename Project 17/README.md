# Port Scanner

A simple Python-based multithreaded port scanner that scans all ports (1-65535) on a given target. This tool is helpful for testing network security and checking open ports.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [Notes](#notes)


## Overview
This project is a lightweight port scanner built with Python. It utilizes threading to scan multiple ports concurrently, significantly speeding up the scanning process.

## Features
- Scans all TCP ports (1-65535)
- Multithreaded approach for faster scanning
- Provides clear output indicating which ports are open
- Handles common exceptions and errors gracefully

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/n4itr0-07/Python-Projects.git
   cd Project 17
   ```

2. **Ensure Python 3 is installed**:
   Check if Python 3 is installed by running:
   ```bash
   python3 --version
   ```

3. **Install necessary Python modules**:
   This script uses only built-in Python libraries (`socket`, `sys`, `datetime`, `threading`). No additional packages are needed.

## Usage
Run the script with the following command:
```bash
python3 scanner.py <target>
```
- `<target>`: The hostname or IP address of the system you want to scan.

### Example
```bash
python3 scanner.py example.com
```

## Example Output
```
--------------------------------------------------
Scanning target 93.184.216.34
Time started: 2024-11-05 14:30:00
--------------------------------------------------
Port 80 is open
Port 443 is open

Scan completed successfully!
```

## Notes
- **Disclaimer**: Ensure that you have permission to scan the target. Unauthorized scanning of systems may violate local, state, or international laws.
- The scan may take some time depending on the network and target system's response.
- Ports that are not open or do not respond within a timeout are ignored silently.



---  

*Happy scanning and stay secure!*

