import urllib.request,json,datetime,sys
sys.path.append("/home/pi/pythonscripts")#append the directory where the transmission.py lives
from transmission import Email

#use gmail's smtp server to send out the email
email = Email("gmail")
#create a request object
req = urllib.request.Request(url="https://api.ipify.org/?format=json")

#current ip address
file = open("/home/pi/resources/ip.dat")#make a connection to the file
local_data = json.loads(file.read()) #read and parsed the json data
file.close() #close the file

#get the last ip from ipfy
response = urllib.request.urlopen(req) #open the url
data = response.read() #read the data
parsed_data = json.loads(data.decode()) #parse the json data

if parsed_data["ip"] != local_data["ip"]: #check if it's equal to the previously saved ip
    file = open("/home/pi/resources/ip.dat","w") #make a writeable connection to a file
    local_data["ip"] = parsed_data["ip"]#save the current ip inplace of the previous ip
    local_data["last_update"] = datetime.datetime.now().isoformat()
    json_local_data = json.dumps(local_data) #convert to json
    file.write(json_local_data)#write the json
    file.close()#close the file to flush the file stream
    #email it out
    email.sendEmail(From="pi@raspberrypi",To="The.Lawrence.Khan@gmail.com",Subject="IP ADDRESS",Message = parsed_data["ip"])

#print("Last Update: {0}".format( datetime.datetime.now().isoformat() ) )
