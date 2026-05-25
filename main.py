#!/usr/bin/env python3
import secrets
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    # Always start with lowercase letters
    characters = string.ascii_lowercase
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()-_=+"
        
    # Securely pick random characters using the secrets module
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    print("🔒 --- THE TERMINAL VAULT --- 🔒")
    print("Let's generate a secure password.\n")
    
    # Get password configuration from user
    try:
        length = int(input("🔑 Enter password length (e.g., 12, 16): "))
    except ValueError:
        print("❌ Invalid number. Defaulting to 12 characters.")
        length = 12
        
    include_upper = input("🔠 Include uppercase letters? (y/n): ").lower() == 'y'
    include_nums = input("🔢 Include numbers? (y/n): ").lower() == 'y'
    include_syms = input("🔣 Include special characters/symbols? (y/n): ").lower() == 'y'
    
    # Generate and display
    pwd = generate_password(length, include_upper, include_nums, include_syms)
    
    print("\n" + "="*30)
    print(f"✨ Your Secure Password:\n{pwd}")
    print("="*30)
    print("💡 Tip: Copy it directly from your terminal screen!")

if __name__ == '__main__':
    main()

