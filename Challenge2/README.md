
## MD5 Hash Challenge

This challenge demonstrates how MD5 hashes can be generated and cracked using a mask-based attack.

## Files

md5-hasher.py
Generates random numeric passwords with sufficient length to make rainbow table attacks impractical, and outputs a list of 10 MD5 hashes.

md5-hashcat.sh
Bash script that runs Hashcat against a hash file using a configurable mask attack.

## Usage

## Generate hashes and save them to a file:

python3 md5-hasher.py > output.txt 


## Crack hashes with Hashcat:

chmod +x md5-hashcat.sh

./md5-hashcat.sh output.txt

## Purpose

Educational use only.
Demonstrates why MD5 and weak password schemes are insecure.
