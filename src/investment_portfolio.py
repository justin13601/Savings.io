import os
import requests

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from yahoo_fin import stock_info as si
from pandas_datareader import DataReader
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')


def query_tickers(industry):
    ################# add in ticker interests based on major ################
    # load tickers
    tickers = si.tickers_dow()

    yahoo_recommendations = []

    # call request from yahoo
    for each_ticker in tickers:
        print("Now Querying Recommendation for: " + each_ticker)
        query_a = 'https://query2.finance.yahoo.com/v10/finance/quoteSummary/'
        query_b = '?formatted=true&crumb=swg7qs5y9UP&lang=en-US&region=US&' \
                  'modules=upgradeDowngradeHistory,recommendationTrend,' \
                  'financialData,earningsHistory,earningsTrend,industryTrend&' \
                  'corsDomain=finance.yahoo.com'

        request_url = query_a + each_ticker + query_b
        response = requests.get(request_url)

        # if response failed
        if not response.ok:
            recommendation = 0

        # response success
        try:
            result = response.json()['quoteSummary']['result'][0]
            recommendation = result['financialData']['recommendationMean']['fmt']
        except:
            recommendation = 0

        yahoo_recommendations.append(recommendation)

    # converting to a pandas dataframe
    data = {'Ticker': tickers, 'Recommendations': yahoo_recommendations}
    df = pd.DataFrame(data)
    df['Recommendations'] = pd.to_numeric(df['Recommendations'])

    # sort and filter dataframe
    df = df[df.Recommendations != 0]
    df.sort_values(by=['Recommendations'], ascending=True)

    ################# add in trading experience ################
    # filter based on recommendation value
    df_buy = df[df.Recommendations <= 1.5]
    df_sell = df[df.Recommendations >= 4.5]
    df_hold = df[df.Recommendations == 3]

    # combine dataframes (for experienced investor who understands buys/sells/holds)
    df_final = pd.concat([df_hold, df_buy, df_sell])
    df_final.reset_index(level=0, inplace=True)

    return df_final


def scrub_news(df_final):
    news = {}
    parsed_news = []
    columns = ['ticker', 'date', 'time', 'headlines']

    finviz = 'https://finviz.com/quote.ashx?t='

    # scrubs news from FinViz's site
    for each_ticker in df_final['Ticker']:

        print("Now Scraping News for: " + each_ticker)

        url = finviz + each_ticker
        header = {'user-agent': 'my-app/0.0.1'}

        request = Request(url=url, headers=header)
        response = urlopen(request)

        # html resposne returning news-table
        html = BeautifulSoup(response, features="lxml")
        result = html.find(id='news-table')

        news[each_ticker] = result

    # parses news table for headlines
    for name, table in news.items():
        # values return in <tr>
        for val in table.findAll('tr'):

            text = val.a.get_text()
            date_time = val.td.text.split()

            if len(date_time) == 1:
                time = date_time[0]
            else:
                date = date_time[0]
                time = date_time[1]

            each_ticker = name.split('_')[0]

            parsed_news.append([each_ticker, date, time, text])

    # convert and concatenate to dataframe
    scrubbed_news = pd.DataFrame(parsed_news, columns=columns)
    scrubbed_news['date'] = pd.to_datetime(scrubbed_news.date).dt.date
    scrubbed_news = scrubbed_news.groupby(
        ['ticker'], as_index=False).agg({'headlines': ''.join})
    scrubbed_news.insert(2, "Recommendation", df_final.Recommendations, True)
    scrubbed_news['Recommendation'] = pd.to_numeric(
        scrubbed_news['Recommendation'])

    return scrubbed_news


def sentiment_analysis(scrubbed_news):
    # compute VADER compound score
    scores = scrubbed_news['headlines'].apply(
        SentimentIntensityAnalyzer().polarity_scores).tolist()

    # combine into one dataframe and sort for results
    df_with_scores = pd.DataFrame(scores)
    df_results = scrubbed_news.join(df_with_scores, rsuffix='_right')
    df_results.sort_values(by='compound', ascending=False, inplace=True)
    df_results.reset_index(level=0, inplace=True)

    return df_results


def print_results(df_results):
    for i in range(0, len(df_results)):
        if df_results["Recommendation"][i] <= 1.5:
            print("Buy: " + df_results['ticker'][i])
        elif df_results["Recommendation"][i] >= 4.5:
            print("Sell: " + df_results['ticker'][i])
        elif df_results["Recommendation"][i] == 3:
            print("Hold: " + df_results['ticker'][i])
    return


'''
Business & Commerce
Healthcare Professions & Pharmacology Programs
Social Sciences & History
Biological & Biomedical Sciences
Engineering & Technology
Energy & Infrastructure
Communication, Journalism & Related Programs
'''
if __name__ == "__main__":
    tickers = query_tickers(None)
    news = scrub_news(tickers)
    results = sentiment_analysis(news)
    print_results(results)