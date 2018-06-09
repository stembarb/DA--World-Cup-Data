
# import Request library, which allows to send HTTP requests
import requests
# import BeautifulSoup library for pulling data out of HTML
from bs4 import BeautifulSoup
# import Pandas library to store data as dataframe
import pandas as pd

# What do we plan to do?
# 1) make a GET request to the FIFA Tournaments page, using the Request library
# 2) save content (HTML) of FIFA Tournaments page in a Beautiful Soup format 
# 3) find URLs to all FIFA World Cup editions, slice URLs to add '/groups', save new URLs in a list
# 4) make a GET request to all FIFA World Cup pages, one by one, and save group's data in a list
# 5) concatanate data from all FIFA World Cup pages into a one Pandas' dataframe 
# 6) export dataframe to Excel for further manipulation

url = "http://www.fifa.com/fifa-tournaments/statistics-and-records/worldcup/index.html"
# Set url variable to FIFA Tournaments page

try:
# Use try/except block to check if page is accessible and handle exceptions 
    page_response = requests.get(url, timeout=5)
    # Query the website (GET request, requests library), timeout is set to 5 secodns, store HTTP status code in variable page_response
    
    if page_response.status_code == 200:
    # If page is accessible (200 is a standard response for successful HTTP requests), save its content to page_content variable using BeautifulSoup format
        
        page_content = BeautifulSoup(page_response.content,'lxml')
        # Now that he have page content saved in the page_content variable, we can use BeautifulSoup methods to find links to all FIFA Word Cup editions
        tournaments = page_content.find(attrs={'id':'alleditions'})
        # Find an HTML element that contains links to all World Cup editions

        link_list = []
        for link in tournaments.find_all('a'):
        # Find all anchor elements in the tournaments, iterate trough them
            group_link = 'http://www.fifa.com' + link.get('href').replace('index.html','groups/index.html')
            # Extract url, add domain (http://www.fifa.com) and groups page (groups/)
            link_list.append(group_link)
            # Store new URLs in a list
        link_list = link_list[0:6]
        # We want stats only from 1994 - 2014, thus we take first 6 links

    else:
    # If page is not accessible, print page status to console
        print(page_response.status_code)

except requests.Timeout as e:
# If timeout occurred, print notification to console
        print('Timeout occurred for requested page: ' + url)
        print(str(e))

append_data = []
# Create empty list where we will store group data
counter = 0
# Set counter for while loop

while counter < len(link_list) and len(link_list) > 0:
# Iterate trought the link_list if list is not empty

    url = link_list[counter]
    # Set url variable to link from the link_list

    try:
    # Use try/except block to check if page is accessible and handle exceptions 
        page_response = requests.get(url, timeout=5)
        # Query the website (GET request, requests library), timeout is set to 5 secodns, store HTTP status code in variable page_response
        
        if page_response.status_code == 200:
        # If page is accessible (200 is a standard response for successful HTTP requests), save its content to page_content variable using BeautifulSoup format
            
            page_content = BeautifulSoup(page_response.content,'lxml')
            # Now that he have page content saved in the page_content variable, we can use BeautifulSoup methods to find groups data
            
            page_title = page_content.title.text
            # take page title, which contains info on World Cup edition e.g. 2014 FIFA World Cup Brazil™
            world_cup = page_title.split(' ')[0]
            # split title, and take first element which is a year e.g. take 2014 from 2014 FIFA World Cup Brazil™

            standings_table = page_content.find('div', attrs={'id':'standings'})
            # Find html element which contains statistics for all groups

            group_letters = [gl.get_text() for gl in standings_table.select('.group-wrap .caption-nolink')]
            # Find (select) all html elements which contain group letter, extract text from each element, save in list
            group_letter = [gl for gl in group_letters for i in range(4)]
            # On the FIFA page group letter is listed only once, but  we need to repeat it for each row

            teams = [tn.get_text() for tn in standings_table.select('.group-wrap .teamname-nolink span.t-nText')]
            # Find (select) all html elements which contain team name, extract text for each element, save in list

            match_played = [mp.get_text() for mp in standings_table.select('.group-wrap .tbl-matchplayed span.text')]
            # Find (select) all html elements which contain number of match played, extract text for each element, save in list

            match_won = [mw.get_text() for mw in standings_table.select('.group-wrap .tbl-win span.text')]
            # Find (select) all html elements which contain number of match won, extract text for each element, save in list

            draw = [d.get_text() for d in standings_table.select('.group-wrap .tbl-draw span.text')]
            # Find (select) all html elements which contain number of draws, extract text for each element, save in list

            lost = [l.get_text() for l in standings_table.select('.group-wrap .tbl-lost span.text')]
            # Find (select) all html elements which contain number of match lost, extract text for each element, save in list

            goals_for = [gf.get_text() for gf in standings_table.select('.group-wrap .tbl-goalfor span.text')]
            # Find (select) all html elements which contain number of goals for, extract text for each element, save in list

            goals_against = [ga.get_text() for ga in standings_table.select('.group-wrap .tbl-goalagainst span.text')]
            # Find (select) all html elements which contain number of goals agains, extract text for each element, save in list

            goals_difference = [gd.get_text() for gd in standings_table.select('.group-wrap .tbl-diffgoal span.text')]
            # Find (select) all html elements which contain goals difference, extract text for each element, save in list

            points = [p.get_text() for p in standings_table.select('.group-wrap .tbl-pts span.text')]
            # Find (select) all html elements which contain number of points, extract text for each element, save in list

            group_tables = pd.DataFrame({
            # Save data in the pandas dataframe
                "Fifa World Cup": world_cup,
                "Group": group_letter, 
                "Teams": teams, 
                "Match played": match_played, 
                "Match won": match_won,
                "Draw": draw,
                "Lost": lost,
                "Goals for": goals_for,
                "Goals against": goals_against,
                "Goals difference": goals_difference,
                "Points": points
            })

            append_data.append(group_tables)
            # Append dataframe to a list; as a result we will have a list of dataframes
        else:
        # If page is not accessible, print page status to console
            print(page_response.status_code)

    except requests.Timeout as e:
    # If timeout occurred, print notification to console
        print('Timeout occurred for requested page: ' + url)
        print(str(e))

    counter += 1
    # Increase counter to move to the next link in the link_list

append_data = pd.concat(append_data, axis=0, ignore_index=True)
# Concatanate all elements (dataframes) in the append_data list to receive one dataframe

append_data.to_excel('WorldCupData2.xlsx')
# Export dataframe to excel file