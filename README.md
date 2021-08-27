# Exif-Maniac <img src="https://upload.wikimedia.org/wikipedia/commons/8/8c/Blue_Python_3.6%2B_Shield_Badge.svg" />

**A Remote Code Execution Framework via Exif Data in images**

-> Insert payload in images as Exif data

-> Upload image to <a href="https://transfer.sh">transfer.sh</a> (Files stored for 14 days)

-> Generate one liner to launch on victim machine (OSX, Linux)

Exif Maniac include <a href="https://github.com/D4Vinci/Cuteit">Cuteit</a> that make a malicious ip a bit cuter 😄

### Usage

`$ git clone https://github.com/CalfCrusher/Exif-Maniac/`

`$ cd Exif-Maniac && pip3 install -r requirements.txt`

`$ python3 exifmaniac.py`
 

## 
***Why Embed Payloads into Images?***

In most scenarios, hiding a payload inside an image file isn't required. In highly secure environments, however, where every domain is logged by firewall software, it may be beneficial to conceal the contents and origin of the payload. The usage of images to conceal payloads can make it difficult for sysadmins monitoring traffic to identify the activity as malicious or suspicious.
