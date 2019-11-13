import csv

with open("tweetV.csv") as cfile1:
  reader = csv.DictReader(cfile1)
  f = open("tweetV.txt", "w")
  for row in reader:
    if row.get("Tweets") != None:
      print row.get("Tweets")
      f.write(row.get("Tweets"))
      
with open("tweetE.csv") as cfile2:
  reader = csv.DictReader(cfile2)
  f = open("tweetE.txt", "w")
  for row in reader:
    if row.get("Tweets") != None:
      print row.get("Tweets")
      f.write(row.get("Tweets"))
