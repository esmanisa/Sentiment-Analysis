import csv
from django.shortcuts import render
import snscrape.modules.twitter as sntwitter
from django.http import HttpResponse
import pandas as pd

# Create your views here.
def generatedataset(request):
    if request.method == "POST":
        expression = request.POST["expression"]
        hashtag = request.POST["hashtag"]
        account = request.POST["account"]
        sinceDay = request.POST["sinceDay"]
        sinceMonth = request.POST["sinceMonth"]
        sinceYear = request.POST["sinceYear"]
        untilDay = request.POST["untilDay"]
        untilMonth = request.POST["untilMonth"]
        untilYear = request.POST["untilYear"]

        query = f"{expression}  (#{hashtag}) (from:{account}) lang:tr until:{untilYear}-{untilMonth}-{untilDay} since:{sinceYear}-{sinceMonth}-{sinceDay}"

        tweets = []
        limit = 10
        get_tweets = sntwitter.TwitterSearchScraper(query).get_items()

        for tweet in get_tweets:
            if len(tweets) == limit:
                break
            else:
                tweets.append([tweet.date, tweet.id, tweet.content])
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="twitter_data.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['Date', 'Tweet Id', 'Tweets'])
        for tweet in tweets:
            writer.writerow(tweet)

        return response
    else:
        return render(request, 'generatedataset.html')



