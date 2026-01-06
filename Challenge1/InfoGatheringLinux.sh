#!/bin/bash
#
# Detta script samlar in systeminformation - RECON
#
# Kan användas för följande attacker:
# [Skriv möjliga attacker]
#
# Author: Jessica B
# Last Update: 2026/06/01


echo "Welcome to  RECON script to se how Linux enviroment is doing"

echo
echo "=== SYSTEMINFO ==="
uname -a
echo

echo "=== OS-RELEASE ==="
cat /etc/os-release 2>/dev/null
echo

echo "=== CURRENT USER ==="
whoami
echo

echo "=== LOGGED IN USER  ==="
who
echo

echo "=== USER WITH SHELL ==="
grep -E "sh$" /etc/passwd
echo

echo "=== HARDWARE ==="
lscpu 2>/dev/null | grep -E "Model name|CPU\(s\)"
echo

echo "=== SPACE  ==="
free -h
echo

echo "=== DISK ==="
lsblk
echo

echo
echo "=== NETWORK ==="
ip a | grep inet
echo

echo
echo "=== ROUTING ==="
ip route
echo

echo
echo "=== LISTENING PORTS ==="
ss -tuln
echo

echo "=== SERVICES ==="
command -v python3 && python3 --version
command -v git && git --version
echo 

echo "=== ACTIVE SERVICES ==="
systemctl list-units --type=service --state=running | head -n 10
echo
