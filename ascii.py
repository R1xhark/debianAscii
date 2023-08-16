import pyfiglet
import subprocess

def generate_ascii_art(text):
    ascii_art = pyfiglet.figlet_format(text, font='slant')
    return ascii_art

def add_to_startup(script_path):
    desktop_entry = f"""[Desktop Entry]
Type=Application
Exec=python3 "{script_path}"
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_US]=ASCII Art Script
Name=ASCII Art Script
Comment[en_US]=ASCII art generator script
Comment=ASCII art generator script
"""
    startup_dir = f"$HOME/.config/autostart/ascii_art_script.desktop"
    subprocess.run(['mkdir', '-p', '$HOME/.config/autostart'])
    with open(startup_dir, 'w') as desktop_file:
        desktop_file.write(desktop_entry)

user_input = input("Enter text for ASCII art: ")
ascii_art = generate_ascii_art(user_input)
print(ascii_art)

add_startup = input("Do you want to add this script to startup? (yes/no): ").lower()
if add_startup == 'yes':
    script_path = __file__
    add_to_startup(script_path)
    print("Script added to startup!")

