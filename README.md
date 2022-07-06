# Raspberry Pi
#### All scripts are currently running on my Raspberry Pi
___
## DDNS CLIENT
#### Email yourself your WAN IP address whenever it changes
1. Clone the project
  ```console 
    pi@raspberry:~$ git clone git@github.com:ltekengineering/Raspberrypi.git .
  ```  
2. Clean up
  ```console
    pi@raspberry:~$ rm LICENSE README.md
    pi@raspberry:~$ rm -rf .git*
  ```
3. Edit resources/config.ini
  * username = your.email.address@gmail.com 
  * password = _change this to app password generated at accounts.google.com_
4. Schedule this in crontab
  ```console
    pi@raspberry:~$ crontab -e
    #add the following to run the script every hour
    0 */1 * * * python /home/pi/Raspberrypi/pythonscripts/ipupdate.py >/dev/null 2>&1
  ```
