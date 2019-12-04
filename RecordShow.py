import requests
import time
from time import sleep
from SendDrive import sendDrive

def recordShow(showName, lengthSecs, delaySecs, emailTo):
    print("Starting recording for " + showName + " in " + str(delaySecs) + " seconds")
    sleep(delaySecs)

    print ("Now recording: " + showName + time.strftime(' %H:%M:%S'))
    endTime = time.time() + float(lengthSecs-1)

    showDir = "Streams/"
    fileName = showName.replace(" ","")  + time.strftime('%b-%d-%Y') + ".mp3"

    r = requests.get('http://173.255.221.48:8000/stream', stream=True)
    with open(showDir + fileName, 'wb') as f:
        # try:
        for block in r.iter_content(1024):
            if (time.time() >= endTime):
                break
            else:
                f.write(block)

    print("File written to " + showDir + fileName)
    #sendEmail(showName, fileName)
    sendDrive(fileName, showName, emailTo)