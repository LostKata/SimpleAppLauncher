import subprocess
import os

# Defining function
def open_app(app_path):
    try:
        if os.path.exists(app_path) or " --processStart " in app_path:
            subprocess.Popen(app_path.split())
            print(f"{app_path} opened succesfully.")
        else:
            print(f"Error: The path {app_path} does not exist.")
    except Exception as e:
        print(f"An error occured: {e}")
        
# Path to executables
steam_path = "C:\\Program Files (x86)\\Steam\\Steam.exe"
discord_path = "C:\\ProgramData\\purpl\\Discord\\Update.exe --processStart Discord.exe" # Change purpl to your name of the user
icue_path = "C:\\Program Files\\Corsair\\Corsair iCUE5 Software\\iCUE.exe"
open_app(steam_path) # Open Steam
open_app(discord_path) # Open Discord
open_app(icue_path) # Open iCUE