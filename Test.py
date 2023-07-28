import requests
<<<<<<< Updated upstream
print(requests.text.get("http://ip-api.com/line/24.48.0.1?fields=18032401"))
from csv import writer
response = requests.get("http://ip-api.com/csv/43.255.158.3 ?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response2 = requests.get("http://ip-api.com/csv/182.37.48.127?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response3 = requests.get("http://ip-api.com/csv/42.54.157.153?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response4 = requests.get("http://ip-api.com/csv/45.117.143.157?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response5 = requests.get("http://ip-api.com/csv/210.140.43.55?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response6 = requests.get("http://ip-api.com/csv/122.186.78.6?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response7 = requests.get("http://ip-api.com/csv/210.245.96.226?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response8 = requests.get("http://ip-api.com/csv/45.117.140.92?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response9 = requests.get("http://ip-api.com/csv/107.172.111.205?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response10 = requests.get("http://ip-api.com/csv/123.114.24.62?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response11 = requests.get("http://ip-api.com/csv/107.182.128.218?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response12 = requests.get("http://ip-api.com/csv/103.18.101.164?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response13 = requests.get("http://ip-api.com/csv/ 103.18.101.190?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response14 = requests.get("http://ip-api.com/csv/175.173.181.156?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response15 = requests.get("http://ip-api.com/csv/192.142.133.9?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response16 = requests.get("http://ip-api.com/csv/157.245.201.168?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response17 = requests.get("http://ip-api.com/csv/31.207.89.160?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response18 = requests.get("http://ip-api.com/csv/103.48.139.221?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response19 = requests.get("http://ip-api.com/csv/105.73.202.250?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response20 = requests.get("http://ip-api.com/csv/103.240.252.20?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response21 = requests.get("http://ip-api.com/csv/45.137.22.87?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response22 = requests.get("http://ip-api.com/csv/209.85.208.43?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response23 = requests.get("http://ip-api.com/csv/ 209.85.160.172?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response24 = requests.get("http://ip-api.com/csv/103.18.101.152?fields=status,continent,country,city,timezone,isp,org,proxy,query")
response25 = requests.get("http://ip-api.com/csv/103.18.101.181?fields=status,continent,country,city,timezone,isp,org,proxy,query")

print(response.text)
list = (response.text)
list = (response.text.split(","))

=======
from csv import writer
response = requests.get("http://ip-api.com/csv/24.48.0.1?fields=status,continent,country,city,timezone,isp,org,proxy,query")
#print(response.text)
#list = (response.text)
list = (response.text.split(","))
>>>>>>> Stashed changes
f = open('C:/Users/rami\Desktop/test/test.csv', 'a')
writer_object = writer(f)
writer_object.writerow(list)
f.close()

<<<<<<< Updated upstream
print(request.get("http://ip-api.com/line/24.48.0.1?fields=18032401"))
=======

>>>>>>> Stashed changes


print(list[1])
#print(requests.get("http://ip-api.com/csv/24.48.0.1?fields=status,continent,country,city,timezone,isp,org,proxy,query"))


