#make is sync time from a time server
#make it get the lists once a week or something from scraping the schedule website
#attach show picture to mp3
#look for "completed" text instead of just waiting 10 seconds
#recycle feature that removes show after x weeks at night or early morning (2am?)
import time
import threading
from RecordShow import recordShow

# big thanks to Jazzer on stackoverflow for this awesome solution (Recording the stream)
# https://stackoverflow.com/questions/4247248/record-streaming-and-saving-internet-radio-in-python

threads = []
shows = []
with open ("C:/Devtop/KPSUStreamRecorder/Schedule/" + time.strftime('%A') + ".txt") as f:
    for line in f:
        shows.append(line.rstrip())

if (shows[0] == "empty"):
    print ("No shows today.")#  Sleeping program until midnight.")
    #sleep((((24 if (time.strftime('%M') == "00") else 23) - (int(time.strftime('%H'))))*60*60) + ((60 - (int(time.strftime('%M'))))*60))

else:
    for show in shows:
        showDetails = show.split("::")
        delaySeconds = (((int(showDetails[1].split(":")[0]))*60*60 + (int(showDetails[1].split(":")[1]))*60)
                        - (((int(time.strftime("%H")))*60*60 + (int(time.strftime("%M")))*60) + (int(time.strftime('%S')))))
        threads.append(threading.Thread(target=recordShow, args=(showDetails[0], int(showDetails[2])*60, int(delaySeconds), showDetails[3])))
        threads[len(threads) - 1].start()

    for thread in threads:
        thread.join()

print ("Recording has ended for the day")
input()
#Not currently needed because Trime restarts at midnight
#print ("\n\nSYSTEM WILL SHUT DOWN IN 30 SECONDS")
#time.sleep(30)
#os.system("shutdown -t 0 -r -f")