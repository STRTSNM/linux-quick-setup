import os
import time

def first():
        os.system("clear")
        print("""

        ██╗░░░░░██╗███╗░░██╗██╗░░░██╗██╗░░██╗    ░██████╗██╗░░░██╗
        ██║░░░░░██║████╗░██║██║░░░██║╚██╗██╔╝    ██╔════╝██║░░░██║
        ██║░░░░░██║██╔██╗██║██║░░░██║░╚███╔╝░    ╚█████╗░██║░░░██║
        ██║░░░░░██║██║╚████║██║░░░██║░██╔██╗░    ░╚═══██╗██║░░░██║
        ███████╗██║██║░╚███║╚██████╔╝██╔╝╚██╗    ██████╔╝╚██████╔╝
        ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝    ╚═════╝░░╚═════╝░

                """)
        time.sleep(3)

first()

print("Taking care of Wallpapers....")
os.system("sudo cp wp1.png /home/Pictures")
time.sleep(1)
first()
print("Installing user themes")
os.system("git clone https://github.com/vinceliuice/WhiteSur-gtk-theme")
os.system("cd WhiteSur-gtk-theme && ls && chmod +x install.sh && ./install.sh")
time.sleep(1)
print("Setup has been successfully completed. Enjoy !!")
