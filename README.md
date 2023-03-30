# Exif Maniac

**Post Exploitation Framework via Exif Data in images**

### Features

-> Insert payload in images as Exif data (bash reverse shell)

-> Upload image to <a href="https://transfer.sh">transfer.sh</a> (Files stored for 14 days)

-> Generate one liner to launch on victim machine (OSX, Linux) - running in RAM

-> Set up netcat listener (works also behind NAT)

##### Exif Maniac include <a href="https://github.com/D4Vinci/Cuteit">Cuteit</a> that make a malicious ip a bit cuter 😄

### Usage

`$ git clone https://github.com/CalfCrusher/Exif-Maniac/`

`$ cd Exif-Maniac && pip3 install -r requirements.txt`

`$ python3 ExifManiac.py`
 

## 
***Why Embed Payloads into Images?***

In most scenarios, hiding a payload inside an image file isn't required. In highly secure environments, however, where every domain is logged by firewall software, it may be beneficial to conceal the contents and origin of the payload. The usage of images to conceal payloads can make it difficult for sysadmins monitoring traffic to identify the activity as malicious or suspicious. Also, is sexy :D

### TODO

.Add EXIF data with pyexif2 library without using exiftool

##

*Please note that i'm not responsible for any damages and illegal use. Don't be a twat!*
