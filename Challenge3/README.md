# Challenge 3 – EICAR Antivirus Detection Test

## Description
This script is a safe and controlled antivirus verification tool designed to test whether a Windows system’s antivirus or EDR solution is functioning correctly.

It uses the EICAR standard antivirus test string which is completely harmless but intentionally detected by antivirus software.
The script creates a test file, waits for the security solution to react and then verifies whether the file has been removed, quarantined, or blocked.

⚠️ This script does NOT contain malware. 
It is intended strictly for educational and testing purposes.

---

## How the Script Works
1. Verifies that the script is running on **Windows**
2. Writes the EICAR test string to a file on the user’s Desktop
3. Waits a few seconds to allow the antivirus to scan the file
4. Checks if the file:
   - Has been deleted or quarantined by AV/EDR
   - Still exists and can be read
   - Has been altered or locked
5. Prints clear status messages indicating whether antivirus protection is active

---

## Requirements
- Windows operating system
- Python 3.x
- An active antivirus or EDR solution (like Windows Defender)

---

## Usage
1. Open a terminal (PowerShell or CMD)
2. Navigate to the directory containing the script
3. Run the script:

```

python script.py

