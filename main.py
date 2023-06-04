import os
import io
import googleapiclient.discovery
import googleapiclient.errors
import psycopg2
import datetime
from datetime import datetime, time, date
start_time = datetime.now()
def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
parapam = str
numberalliddb = int(0)
databaseid=(str)
kount = int(0)
connection = psycopg2.connect(user="",
                                  password="",
                                  host="",
                                  port="",
                                  database="")


cur = connection.cursor()
cur.execute('SELECT COUNT (youtube_code) from "clips_youtube_codes"') 
answer = cur.fetchall()
cur.close()
connection.close()
joki = str(answer)
jf = joki.strip ('([\']),')
lk = int(jf)
cifra = int(0)
while numberalliddb<lk:
    connection = psycopg2.connect(user="",
                                  password="",
                                  host="",
                                  port="",
                                  database="")


    cur = connection.cursor()
    cur.execute('SELECT (youtube_code) from "clips_youtube_codes" ORDER BY clip_id LIMIT 1 OFFSET %s', [cifra]) 
    answer = cur.fetchall()
    cifra +=1 
    numberalliddb +=1
    stranswer = str(answer)
    desymbol = stranswer.strip ('([\']),')
    parapam=str(parapam)+(desymbol)
    if kount<lk-1:
        parapam=str(parapam)+','
        parapam=parapam.lstrip("<class 'str'>")
        kount+=1
    else:
        parapam=parapam.lstrip("<class 'str'>")
    cur.close()
    connection.close()




  
idytvideos = parapam
splitarrid = idytvideos.split(',')
countallid = len(idytvideos.split(',')),
countid1 = int(''.join(map(str, countallid)))
oneindex = int(0)
twoindex = int(1)
justind = int(0)
justind2 = int(1)
firstindex = int(0)
lastindex = int(50)
currentids = splitarrid[firstindex:lastindex]
oneid = str(currentids[oneindex:twoindex])
copyidvideothere = (','.join(map(str, currentids)))
countbutuple = len(copyidvideothere.split(',')),
countid = int(''.join(map(str, countbutuple)))
vivod = [list]
grabid = [list]
i = int(0)
tui = int(1)
per= int(tui-1)
oneun=int(1)
while  countid1-50 > firstindex:
        currentids = splitarrid[firstindex:lastindex]
        print (currentids)
        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = ""
        youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)
        request = youtube.videos().list(
        part="status",
        id=currentids
        
    )
        
        response = request.execute()
        print('Проверил 50 id')
        with open("output.txt","a", encoding="utf-8") as f:
                print(response, file=f)
                vivod.append(response)
                try1=response.get('items')
                firstindex += 50
                lastindex += 50
                gih = len(try1)
                for i in range(gih):
                    try2=try1[oneindex:twoindex]
                                                  
                    iddostup = try2[0]['id']         
                    h=open("Exportid.txt",'a', encoding="utf-8")
                    h.write (iddostup)
                    h.write (' Доступен\n')
                    h.close
                    oneindex +=1
                    twoindex +=1
                else: 
                    
                    oneindex = int(0)
                    twoindex = int(1)
                    
                               
      
else:
    firstindex = countid1-(countid1-firstindex)
    lastindex = countid1+1
    
    currentids = splitarrid[firstindex:lastindex]
    print (currentids)    
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = ""
youtube = googleapiclient.discovery.build(
		api_service_name, api_version, developerKey = DEVELOPER_KEY)
request = youtube.videos().list(
		part="status",
		id=currentids
	)
		
response = request.execute()
with open("output.txt","a", encoding="utf-8") as f:
				print(response, file=f)
				vivod.append(response)
				
try1=response.get('items')
gih = len(try1)
for i in range(gih):
                    try2=try1[oneindex:twoindex]
                                  
                    iddostup = try2[0]['id']           
                    h=open("Exportid.txt",'a', encoding="utf-8")
                    h.write (iddostup)
                    h.write (' Доступен\n')
                    h.close
                    oneindex +=1
                    twoindex +=1 
else: 
    
        oneindex = int(0)
        twoindex = int(1)
        
for o in range(lk):
    oneid = str(splitarrid[justind:justind2])
    jf = oneid.strip ('[\']')
    f=open("Exportid.txt",'r', encoding="utf-8")
    if jf+" Доступен" not in f.read():
                     
                    h=open("Exportid.txt",'a', encoding="utf-8")
                    h.write (jf)
                    h.write (' Недоступен\n')
                    h.close
                    connection = psycopg2.connect(user="",
                                  password="",
                                  host="",
                                  port="",
                                  database="")
                    cur = connection.cursor()
                    cur.execute("INSERT INTO clips_unavailable (id, unavailable, uniqueid) VALUES (%s, %s, %s)",(jf, oneun, tui))
                    connection.commit()
                    cur.close()
                    connection.close()
                    tui+=1
                    justind +=1
                    justind2 +=1
                    
    else:
        justind2 +=1
        justind +=1

if __name__ == "__main__":
    main()

print(datetime.now() - start_time)
