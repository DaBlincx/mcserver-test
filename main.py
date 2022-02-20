from mcstatus import MinecraftServer
import time
import serverconfig

respconf = 0

def minute(min):
    m = 60*min
    return m

def getSvInfo(sv):
    year = str(time.localtime().tm_year)
    month = str(time.localtime().tm_mon)
    day = str(time.localtime().tm_mday)
    hour = str(time.localtime().tm_hour)
    min = str(time.localtime().tm_min)
    sec = str(time.localtime().tm_sec)
    if len(month) == 1:
        month = "0"+month
    if len(day) == 1:
        day = "0"+day
    if len(hour) == 1:
        hour = "0"+hour
    if len(min) == 1:
        min = "0"+min
    if len(sec) == 1:
        sec = "0"+sec
    formatted_time =  "< "+year+"/"+month+"/"+day+" "+hour+":"+min+":"+sec+" >"
    
    server = MinecraftServer.lookup(sv)
    status = server.status()
    fmsg = "\n================================================================\n\n{0}\nPlayers: {1}\nMOTD: {2}".format(formatted_time, status.players.online, status.description.replace("\n"," "))
    f = open(sv+'_log.txt', 'a')
    f.write(fmsg)
    f.close()
    pllg = open(sv+'_playercount.txt','a')
    pllg.write(str(status.players.online) + "/" + str(status.players.max) + " - " + formatted_time + "\n")
    pllg.close()
    print(fmsg+"\n")
    time.sleep(minute(2.5))

while True:
    try:
        getSvInfo(serverconfig.server)
    except TimeoutError:
        print("Timed out\nRetrying in 2 seconds.")
        time.sleep(2)
    except IOError:
        respconf + 1
        if respconf == 32:
            print("didnt respind after 32 requests. retrying in one minute!")
            time.sleep(2)
            mine = 60
            for i in range(0,60):
                print(str(mine)+" seconds")
                mine-=1
                time.sleep(1)
            print("\n\nRetrying now!\n\n")
