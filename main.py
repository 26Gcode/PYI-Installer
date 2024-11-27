import time
import pyautogui

def install_package():
    """Function to handle package installation via pyautogui."""
    while True:
        print("")
        print("remember that you only need to type which python library you want to install, don't type pip install. everything else will be done for you.")
        print("")
        package = input("PYI INSTALLER: ").strip()
        pyautogui.hotkey('win', 'r')
        pyautogui.typewrite('powershell')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.typewrite('pip install ' + package)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.press('enter')
        pyautogui.typewrite('exit')
        pyautogui.press('enter')
        print("")
        print("If the installation did not work, check if you misspelled it.")

def install_pyautogui_instructions():
    """Guide user to install pyautogui if not installed."""
    print("To install pyautogui:")
    print("1. Press the Windows Key + R to open Run.")
    print("2. Type 'powershell' and press Enter.")
    print("3. In PowerShell, run: pip install pyautogui")
    done_install = input("Once installed, type Y to run the PYI installer: ").strip().upper()
    if done_install == "Y":
        install_package()

def main():
    """Main function for the PYI installer."""
    print("Welcome to the PYI Installer", "\u00A9", "2024 26gbush")
    print("")
    print("The PYI installer uses 'pip' to install apps and is an EXTENSION of pip.")
    print("pyautogui is needed to install apps.")
    print("")
    
    pyautoinstalled = input("Do you have pyautogui installed (Y/N)? ").strip().upper()
    
    if pyautoinstalled == "Y":
        install_package()
    elif pyautoinstalled == "N":
        install_pyautogui_instructions()
    else:
        print("Invalid input. Please restart the installer and type 'Y' or 'N'.")

if __name__ == "__main__":
    main()

