---

# URL Adjustments being made for Web-Scrapping (scrape_espn_cricinfo.py)

#### Sample ESPN CRICINFO URL
**Year: 2008<br> Team: Royal Challengers Bangalore**<br>
- Batting: https://stats.espncricinfo.com/ci/engine/records/batting/most_runs_career.html?id=3519;team=4340;type=tournament
- Bowling:https://stats.espncricinfo.com/ci/engine/records/bowling/most_wickets_career.html?id=3519;team=4340;type=tournament

### Note: Exceptions
These following teams are either new entrants, defunct, or were suspended in between seasons, so upon trying to webscrape the following, we will be thrown an error or will receive an empty dataset.<br>
1. **Decan Chargers**
2. **Pune Warriors India** 
3. **Kochi Tuskers Kerala**
4. **Gujarat Lions**
5. **Rising Pune Supergiants**
6. **Lucknow Super Giants**
7. **Gujarat Titans**
8. **Chennai Super Kings**
9. **Rajasthan Royals**


![team_timelines](https://github.com/shreyansh-2003/IPL-Team-Finishing-Position-Prediction-Project/assets/105413094/6659fbda-9d8a-4366-bb91-1fb2e4266ae2)

To handle this abnormality, we created nested dictionaries in the ```scrape_espn_cricinfo.py``` webscrapping file that hold the team's id assigned in the ESPN Cricinfo database and the years they have participated in the IPL in. These years will then be iterated through to avoid discrepencies

---
## Scrapping IPL batting stats from ESPN cricinfo

### 1. scrape_batting_stats_espn()
Function to request to espncricinfo stats teamwise, yearwise page and scrape relevant information and add to a temporary dataset.<br>
__Screenshot of a sample page to be web-scrapped:__

![batting_scrape_sample.png](attachment:batting_scrape_sample.png)

**Year: 2008<br> Team: Royal Challengers Bangalore**<br>
https://stats.espncricinfo.com/ci/engine/records/batting/most_runs_career.html?id=3519;team=4340;type=tournament

### 1. scrape_batting_stats_espn()
Function to request to espncricinfo stats teamwise, yearwise page and scrape relevant information and add to a temporary dataset.<br>
__Screenshot of a sample page to be web-scrapped:__<br>

<img width="1438" alt="batting_scrape_sample" src="https://github.com/shreyansh-2003/IPL-Team-Finishing-Position-Prediction-Project/assets/105413094/13ea6500-bd24-4ec1-884b-e0ae8f181739">

**Year: 2008<br> Team: Royal Challengers Bangalore**<br>
https://stats.espncricinfo.com/ci/engine/records/batting/most_runs_career.html?id=3519;team=4340;type=tournament


### 2. create_batting_stats_dataset()
Function to iterate through all the teams and years, and create the batting dataset by calling the "scrape_batting_stats_espn()" function created earlier.

---

## Scrapping IPL bowling stats from ESPN cricinfo

### 1. scrape_bowling_stats_espn()
Function to request to espncricinfo stats teamwise, yearwise page and scrape relevant information and add to a temporary dataset.<br>
__Screenshot of a sample page to be web-scrapped:__

<img width="1430" alt="bowling_scrape_sample" src="https://github.com/shreyansh-2003/IPL-Team-Finishing-Position-Prediction-Project/assets/105413094/30357b24-9d1b-4b0c-aa11-a395a5f9f096">


**Year: 2008<br> Team: Royal Challengers Bangalore**<br>
https://stats.espncricinfo.com/ci/engine/records/bowling/most_wickets_career.html?id=3519;team=4340;type=tournament

### 2. create_bowling_stats_dataset()
Function to iterate through all the teams and years, and create the batting dataset by calling the "scrape_bowling_stats_espn()" function created earlier.
