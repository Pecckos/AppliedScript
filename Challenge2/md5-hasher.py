
#!/usr/bin/env python3

"""
Password and Hash Generator (Very UNsecure version)
Generates random numeric passwords and calculates their MD5 hashes.

Author: Jessica Bjurlerstam
Last Update: 2026-01-06

WARNING: MD5 is considered cryptographically broken and should not be used
for security-critical applications.
"""

import random
import hashlib

def generate_random_number_string():
    """
    Generates a random string consisting only of digits.
    The length is fixed to PWD_LGT constant.
    
    Returns:
        str: A random string containing only digits (0-9) with fixed length.
        
    Example:
        '4738291650'  # Random 10-digit string
    """
    # Uses random.choice to select digits
    # Creates a reasonably uniform distribution over all possible combinations
    return ''.join(random.choice("0123456789") for X in range(PWD_LGT))

def md5_hash(text):
    """
    Calculates the MD5 hash of a given string.
    
    Args:
        text (str): The input string to hash.
        
    Returns:
        str: The hexadecimal representation of the MD5 hash.
        
    Security Note:
        MD5 is cryptographically broken and vulnerable to collision attacks.
        It should not be used for password storage or security-sensitive applications.
        Consider using SHA-256 or bcrypt instead for real-world applications.
    """
    # encode() converts the string to bytes, required by hashlib
    # hexdigest() returns the hash value as a hexadecimal string
    return hashlib.md5(text.encode()).hexdigest()

def main():
    """
    Main function that orchestrates the password generation and hashing.
    
    Generates NO_PASS random passwords with fixed length PWD_LGT
    and displays them alongside their corresponding MD5 hashes.
    """
 
    
    # Generate and display passwords with their hash values
    for i in range(NO_PASS):
        # Generate a random password with fixed length
        password = generate_random_number_string()
        
        # Calculate the MD5 hash of the password
        hash_value = md5_hash(password)
        
        # Print the resulting hash
        print(f"{hash_value}")
    

# Fixed constants for the program (can be adjusted if needed)
PWD_LGT = 11
NO_PASS = 10

# Standard Python idiom to ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
