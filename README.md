# Raspberry Pi
#### All scripts are currently running on my Raspberry Pi
___
## DDNS CLIENT
#### Email yourself your WAN IP address whenever it changes
1. Clone the project
  ```console 
    pi@raspberry:~$ git clone git@github.com:thelawrencekhan/Raspberrypi.git .
  ```  
2. Clean up
  ```console
    pi@raspberry:~$ rm README.md
    pi@raspberry:~$ rm LICENSE
  ```
3. Edit resources/config.ini
  * username = your.email.address@gmail.com _#Your email here_
  * password = yvrenpwaqoqjwfql _#change this to app password generated at accounts.google.com_
4. Schedule this in crontab
  ```console
    pi@raspberry:~$ crontab -e
  ``` 
