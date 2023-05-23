import requests
from bs4 import BeautifulSoup
import pandas as pd
import warnings 
warnings.filterwarnings("ignore")

#Dictionary that holds ESPN Cricinfo database team ids (Manually extracted)
webpage_team_id = { 
    
    "Royal Challengers Bangalore" : { "id" : 4340, 
                                     "participation" : [ x for x in range(2008,2023)] },
    
    "Chennai Super Kings" : { "id" : 4343,
                              "participation" : [x for x in range(2008,2016)] + [x for x in range(2018,2023)]},
    
    "Kolkata Knight Riders" : { "id" : 4341, 
                               "participation" : [ x for x in range(2008,2023)] },
    
    "Mumbai Indians" : { "id" : 4346, 
                        "participation" : [ x for x in range(2013,2023)] },
    
    "Sunrisers Hyderabad" : { "id" : 5143, 
                             "participation" : [ x for x in range(2008,2023)] },
    
    "Delhi Capitals" : { "id" : 4344, 
                        "participation" : [ x for x in range(2008,2023)] },
    
    "Rajasthan Royals" :  { "id" : 4345,
                           "participation" : [x for x in range(2008,2016)] + [x for x in range(2018,2023)]},
    
    "Punjab Kings" : { "id" : 4342, 
                      "participation" : [ x for x in range(2008,2023)] },
    
    "Gujarat Titans" : { "id" : 6904, 
                        "participation" : [2022] },
    
    "Lucknow Super Giants" : { "id" : 6903, 
                              "participation" : [2022] },
    
    "Rising Pune Supergiants": { "id" : 5843, 
                                "participation" : [2016, 2017] },
    
    "Gujarat Lions" : { "id" : 5845, 
                       "participation" : [2016, 2017] },
    
    "Decan Chargers" : { "id" : 4801, 
                        "participation" : [ x for x in range(2008,2013)] },
    
    "Pune Warriors India" : { "id" : 4787, 
                             "participation" : [ x for x in range(2011,2014)] },
    
    "Kochi Tuskers Kerala" : { "id" : 4788,
                              "participation" : [2011] }
    
}

#Dictionary that holds ESPN Cricinfo database year ids (Manually extracted)
webpage_year_id = {
    2008: 3519, 
    2009: 4801, 
    2010: 5319, 
    2011: 5969, 
    2012: 6680, 
    2013: 7720, 
    2014: 8827, 
    2015: 9657, 
    2016: 11001, 
    2017: 11701, 
    2018: 12210, 
    2019: 12741, 
    2020: 13533, 
    2021: 13840, 
    2022: 14452
}

#Function to request to espncricinfo stats teamwise, yearwise page and scrape relevant information and add to a temporary dataset.
#User defined function for scrapping IPL batting stats from ESPN cricinfo
def scrape_batting_stats_espn(url, team, year):
    try:
        # Sending a GET request to the URL
        response = requests.get(url)

        # Parsing the response HTML using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Finding the table with class 'engineTable' and extract its rows
        table = soup.find('table', class_='engineTable')
        rows = table.find_all('tr')

        # Initializing empty lists to store data
        player_name = []
        matches_played = []
        innings_batted = []
        not_outs = []
        runs_scored = []
        highest_score = []
        batting_average = []
        balls_faced = []
        batting_strike_rate = []
        hundreds_scored = []
        fifties_scored = []
        ducks_scored = []
        fours_scored = []
        sixes_scored = []
    
        # Iterating over each row in the table (excluding the header row)
        for row in rows[1:]:
            # Extracting data from each column in the row
            columns = row.find_all('td')
            player_name.append(columns[0].find('a').text.strip())
            matches_played.append(columns[1].text.strip())
            innings_batted.append(columns[2].text.strip())
            not_outs.append(columns[3].text.strip())
            runs_scored.append(columns[4].find('b').text.strip())
            highest_score.append(columns[5].text.strip())
            batting_average.append(columns[6].text.strip())
            balls_faced.append(columns[7].text.strip())
            batting_strike_rate.append(columns[8].text.strip())
            hundreds_scored.append(columns[9].text.strip())
            fifties_scored.append(columns[10].text.strip())
            ducks_scored.append(columns[11].text.strip())
            fours_scored.append(columns[12].text.strip())
            sixes_scored.append(columns[13].text.strip())

        #If there is no data scrapped due to some error
        if len(player_name)==0:
            return
        
        else:
            # Creating a dictionary to store the data
            data = {
                'player_name': player_name,
                'team' : team,
                'year' : year,
                'matches_played': matches_played,
                'innings_batted': innings_batted,
                'not_outs': not_outs,
                'runs_scored': runs_scored,
                'highest_score': highest_score,
                'batting_average': batting_average,
                'balls_faced': balls_faced,
                'batting_strike_rate': batting_strike_rate,
                'hundreds_scored': hundreds_scored,
                'fifties_scored': fifties_scored,
                'ducks_scored': ducks_scored,
                'fours_scored': fours_scored,
                'sixes_scored': sixes_scored
            }

            # Converting the dictionary to a Pandas DataFrame and return it
            return pd.DataFrame(data)
        
    
    #Incase an error is thrown while scrapping
    except:
        return
    
#Function to iterate through all the teams and years, and create the batting dataset by calling the "scrape_batting_stats_espn()" function created earlier.
#User Defined Function to create batting stats dataset
def create_batting_stats_dataset():
    #Scrapping the year-wise and team-wise batting stats
    df_batting = pd.DataFrame()

    #Iterating through the teams id dictionary
    for team in webpage_team_id.keys():

        #Finding the value of the team id and the participated years for team 'i' from the created dictionary
        team_id = webpage_team_id[team]["id"]
        years_participated_arr = webpage_team_id[team]["participation"]

        #Iterating through the years id dictionary
        for year in years_participated_arr:

            #Finding the value of the year id from the manually created "webpage_year_id" dictionary 
            year_id = webpage_year_id[year]

            #Creating a URL using the ids, for web-scrapping
            url = f"https://stats.espncricinfo.com/ci/engine/records/batting/most_runs_career.html?id={year_id};team={team_id};type=tournament"

            #Using the created user defined function and iterated url to generate the datasets
            df_i = scrape_batting_stats_espn(url, team, year)

            df_batting = df_batting.append(df_i, ignore_index = True)

    return df_batting


#User defined function for scrapping IPL bowling stats from ESPN cricinfo
def scrape_bowling_stats_espn(url, team, year):
    
    try:
        # Sending a GET request to the URL
        response = requests.get(url)

        # Parsing the response HTML using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Finding the table with class 'engineTable' and extract its rows
        table = soup.find('table', class_='engineTable')
        rows = table.find_all('tr')

        # Initialing empty lists to store data
        player_name = []
        matches_played = []
        innings_bowled = []
        overs_bowled = []
        maidens_earned = []
        runs_conceded = []
        wickets_taken = []
        best_innings_bowling = []
        bowling_average = []
        economy_rate = []
        bowling_strike_rate = []
        four_wickets = []
        five_wickets = []
    
    
        # Iterating over each row in the table (excluding the header row)
        for row in rows[1:]:
            # Extracting data from each column in the row
            columns = row.find_all('td')
            player_name.append(columns[0].find('a').text.strip())
            matches_played.append(columns[1].text.strip())
            innings_bowled.append(columns[2].text.strip())
            overs_bowled.append(columns[3].text.strip())
            maidens_earned.append(columns[4].text.strip())
            runs_conceded.append(columns[5].text.strip())
            wickets_taken.append(columns[6].find('b').text.strip())
            best_innings_bowling.append(columns[7].text.strip())
            bowling_average.append(columns[8].text.strip())
            economy_rate.append(columns[9].text.strip())
            bowling_strike_rate.append(columns[10].text.strip())
            four_wickets.append(columns[11].text.strip())
            five_wickets.append(columns[12].text.strip())
            
        #If there is no data scrapped due to some error
        if len(player_name)==0:
            return
        
        else:
            # Creating a dictionary to store the data
            data = {
                'player_name': player_name,
                'team' : team,
                'year' : year,
                'matches_played': matches_played,
                'innings_bowled': innings_bowled,
                'overs_bowled': overs_bowled,
                'maidens_earned': maidens_earned,
                'runs_conceded': runs_conceded,
                'wickets_taken': wickets_taken,
                'best_innings_bowling': best_innings_bowling,
                'bowling_average': bowling_average,
                'economy_rate': economy_rate,
                'bowling_strike_rate': bowling_strike_rate,
                'four_wickets': four_wickets,
                'five_wickets': five_wickets
            }

            # Converting the dictionary to a Pandas DataFrame and return it
            return pd.DataFrame(data)
    
    #Incase an error is thrown while scrapping
    except:
        return 

#User defined function to create bowling stats dataset
def create_bowling_stats_dataset():
    #Scrapping the year-wise and team-wise batting stats
    df_bowling = pd.DataFrame()

    #Iterating through the teams id dictionary
    for team in webpage_team_id.keys():

        #Finding the value of the team id and the participated years for team 'i' from the created dictionary
        team_id = webpage_team_id[team]["id"]
        years_participated_arr = webpage_team_id[team]["participation"]

        #Iterating through the years id dictionary
        for year in years_participated_arr:

            #Finding the value of the year id from the manually created "webpage_year_id" dictionary 
            year_id = webpage_year_id[year]

            #Creating a URL using the ids, for web-scrapping
            url = f"https://stats.espncricinfo.com/ci/engine/records/bowling/most_wickets_career.html?id={year_id};team={team_id};type=tournament"
                
            #Using the created user defined function and iterated url to generate the datasets
            df_i = scrape_bowling_stats_espn(url, team, year)

            df_bowling = df_bowling.append(df_i, ignore_index = True)

    return df_bowling

