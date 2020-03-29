'''
Retrieves highscore data from Old School Runescape 'Leagues' Highscores. 
'''

from bs4 import BeautifulSoup
import requests
import os 
import os.path
import time 
import pandas as pd
from database.db import *

from dotenv import load_dotenv
load_dotenv()

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m_%d_%Y", named_tuple)
datab = Database()

def writerows(rows, filename):
    highScore_df = pd.DataFrame.from_dict(rows)
    highScore_df.to_csv(filename, index = False, header = True, mode='a')
 
def getHighScores(listingurl):
    # prepare headers
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}

    # fetching the url, raising error if operation fails
    try:
        response = requests.get(listingurl, headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
        exit()

    # Store the web page on disc.
    f = open("saved_logs/osrs_league_hiscores_" + time_string, "w")
    f.write(response.text)
    f.close()

    # BS object
    soup = BeautifulSoup(response.text, "html.parser")

    hiscores = {}
    listings = []

    # loop through the table, get data from the columns
    for rows in soup.find_all("tr", class_="personal-hiscores__row"):
        hiscores = {}
        hiscores["rank"] = int(rows.findChildren()[0].text.replace('\n', ""))
        hiscores["name"] = rows.findChildren()[1].a.text.replace('\n', "").replace(u'\xa0', u' ')
        hiscores["level"] = int(rows.findChildren()[3].text.replace('\n', "").replace(',', ""))
        hiscores["exp"] = int(rows.findChildren()[4].text.replace('\n', "").replace(',', ""))
        datab.connect_set(hiscores, "leaderboard_stats_league_hiscores")
        listings.append(hiscores)
            

    return listings

def getNextPage():
    return "test"

if __name__ == "__main__":
    page = 1
    baseurl = "https://secure.runescape.com/m=hiscore_oldschool_seasonal/overall?table=0&page="
    
    # scrap all pages
    while page < 5:
        listings = getHighScores(baseurl + str(page))
        # write to CSV        
        writerows(listings, "saved_logs/osrs_league_hiscores_" + time_string + ".csv")
        # take a break
        time.sleep(3)

        page += 1
