import os
import time

def open_app(app_name):
    os.system(f"open -a '{app_name}'")

def open_chrome():
    os.system("open -a \"Google Chrome\" --args -n --profile-directory=\"Profile 4\"")

# Navigate to the next desktop space using AppleScript and the accessibility shortcut
def next_desktop_space():
    os.system("osascript -e 'tell application \"System Events\" to key code 124 using control down'")

# Open each app in a separate desktop space and navigate to the next space after opening each app
open_chrome()
time.sleep(10)
next_desktop_space()

open_app("Xcode")
time.sleep(60)
next_desktop_space()

open_app("Fork")
time.sleep(10)
next_desktop_space()

open_app("Microsoft Teams")
time.sleep(10)
next_desktop_space()

open_app("Microsoft Outlook")
time.sleep(10)