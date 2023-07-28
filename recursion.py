import requests
from csv import writer
f = open('C:/Users/rami/Desktop/test/test.txt', 'a')
writer_object = writer(f)

APIcalls = ["http://ip-api.com/line/43.255.158.3 ?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/182.37.48.127?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/42.54.157.153?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/45.117.143.157?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/210.140.43.55?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/122.186.78.6?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/210.245.96.226?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/45.117.140.92?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/107.172.111.205?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/123.114.24.62?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/107.182.128.218?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/103.18.101.164?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/ 103.18.101.190?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/175.173.181.156?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/192.142.133.9?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/157.245.201.168?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/31.207.89.160?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/103.48.139.221?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/105.73.202.250?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/103.240.252.20?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/45.137.22.87?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/209.85.208.43?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/ 209.85.160.172?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/103.18.101.152?fields=status,continent,country,city,timezone,isp,org,proxy,query",
"http://ip-api.com/line/103.18.101.181?fields=status,continent,country,city,timezone,isp,org,proxy,query"]

i= 0
for x in APIcalls:
    
    data = requests.get(x)
    rawdata = str(data.text)
    list = (rawdata.split("/n"))
    #print(list)
    writer_object.writerow(list)
    #print(data.text)
    #print (rawdata)

f.close()
f = open('C:/Users/rami/Desktop/test/test.txt', 'r')
ExportedTxt = f.readlines()
counter1 = 0
for p in ExportedTxt:
    #if int(len(ExportedTxt)) < 2 :
    #ExportedTxt.remove[counter1]
    print(ExportedTxt[counter1])
    print(len(ExportedTxt[counter1]))
    counter1= counter1 +1 
    #print(counter1)
print('done')

# try to get rid of string as indici error by checking value of ExportedTxt[p].len