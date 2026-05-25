#!/usr/bin/env python3
import os
import subprocess
import sys

def clear_screen():
    # Keeps your Termux screen looking crisp and clean
    os.system('clear')

def run_command(cmd):
    # Runs a shell command and waits for user to press Enter when done
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error running command: {e}")
    input("\nPress [Enter] to return to Menu...")

def main():
    while True:
        clear_screen()
        print("⚡ ================================== ⚡")
        print("       BUGSY'S TERMUX COMMAND CENTER   ")
        print("⚡ ================================== ⚡")
        print("1. 🐙 Check Public GitHub Profile Status")
        print("2. 📁 List Current Repositories (Local)")
        print("3. 🔑 Launch Password Generator Vault")
        print("4. 🛠️  View Installed Pkg & Pip Specs")
        print("5. 🚪 Exit Dashboard")
        print("----------------------------------------")
        
        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            print("\n🌐 Fetching live GitHub API data...")
            run_command("gh api user | grep -E '\"login\"|\"name\"|\"public_repos\"'")
            elif choice == '2':
            print("\n📁 Launching Local Project Sub-Menu...")
            print("1. Launch Python Guessing Game")
            print("2. Back to Main Menu")
            sub_choice = input("\nSelect an option: ").strip()
            if sub_choice == '1':
                # Jumps over and runs your guessing game script
                run_command("python ~/Python/guessing_game.py") 

        elif choice == '3':
            print("\n🔑 Switching contexts to Terminal Vault...")
            # Automatically jumps over and runs your vault script
            run_command("python ~/terminal-vault/main.py")
        elif choice == '4':
            print("\n🛠️  Checking core system specs...")
            run_command("python -V && pip -V")
        elif choice == '5':
            print("\n👋 Powering down Command Center. Catch ya later!")
            sys.exit(0)
        else:
            input("\n❌ Invalid choice! Press [Enter] to try again...")

if __name__ == '__main__':
    main()
