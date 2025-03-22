import csv

covid_count = 0

tweet_csv = open("tweets.csv", newline='', encoding='utf-8')

reader = csv.DictReader(tweet_csv)

for row in reader:
    text = row.get('text', '')
    if "covid" in text.lower():
        covid_count += 1

print(covid_count)
tweet_csv.close()