# r6_stat_scrape
 # r6_stat_scrape
 Within these files is web scrapper used for the site R6 Stats - R6 Tracker, Leaderboards, & More! 
The spider used for scraping can be found in r6/r6/spiders/r6Spider_spider.py. My friends and I play a popular game called Rainbow 6 Siege and are quite competitive when it comes to our statistics for the game. Our problem was there was no way for us to quickly compare each of our stats together on a common list as on this site you can only few one player at a time.
This web scraper works by taking in a user input of a list of players and cycles through each of them scraping for their stats. After scraping for the user selected stats it will output them to a CSV allowing the user to view all of the players information in a single formatted doc.
To use this program run the file located here: r6/main.py
This will open a PySimpleGui that allows the user to enter in the names of the players and select the stats they wish to pull from the site. 
The scrappy package was downloaded and used in a WSL virtual environment as using a Linux terminal simplified this process. 
 User Steps: 
1.	Run main.py and enter in desired information into the displayed GUI, separating player names with a space. 
 ![image](https://github.com/ajonto/r6_stat_scrape/assets/78171517/f4bd9b19-af9b-413e-b413-5f43d76c928f)
 ![image](https://github.com/ajonto/r6_stat_scrape/assets/78171517/d65b83ad-7df2-4c76-9a8d-f2883841eb09)


 


2.	Select stats you want to see for each of the players and click okay:
 ![image](https://github.com/ajonto/r6_stat_scrape/assets/78171517/4734968c-fcf5-4d8a-963d-8ac402e99396)

3.	Open the spider.csv that has been generated and view stats: 
![image](https://github.com/ajonto/r6_stat_scrape/assets/78171517/99db2850-bc43-4fac-a69e-7961438a38e9)

