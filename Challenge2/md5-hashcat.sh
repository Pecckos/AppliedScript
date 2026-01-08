#!/bin/bash


# Check if hashcat is installed
if ! command -v hashcat &> /dev/null; then
    echo "ERROR: hashcat is not installed!"
    echo "Install it with: sudo apt install hashcat"
    exit 1
fi

echo "=== Hashcat MD5 Cracker ==="
hashcat --version | head -n 1
echo "==========================="

# Default settings
HASH_FILE="${1:-mina_hashar.txt}"
MASK="${2:-?d?d?d?d?d?d?d?d?d?d?d}"  			# Number of digits to try
HASH_TYPE="0"    				# 0=MD5 hash mode
ATTACK_MODE="3"  				# Mask attack mode

echo "Starting  hashcat ..."
echo "=================="

# Kör hashcat
hashcat -m "$HASH_TYPE" -a "$ATTACK_MODE" "$HASH_FILE" "$MASK" -O -w 3 --force

echo ""
echo "=================="
echo "Hashcat run completed successfully!"
