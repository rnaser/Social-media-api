import csv
import requests

#Enter your search word
search_term = 'Social Media'

#Make a request to the Twitter API
url = 'https://api.twitter.com/1.1/search/tweets.json?q=' + search_term
r = requests.get(url)

#Create a csv file to store the data
csv_file = open('social_media_data.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(csv_file)

#Write the headers of the csv file
csv_writer.writerow(['User', 'Username', 'Tweet'])

#Write the data to the csv file
for tweet in r.json()['statuses']:
    csv_writer.writerow([tweet['user']['name'], tweet['user']['screen_name'], tweet['text']])
    
csv_file.close()
 
