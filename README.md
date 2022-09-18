# GEoutlier_detection

The goal of this project is to explore OldSchool Runescape market data. Some things I am interested in are:
  - Different market indices and the differences in calculation (dow/sp500)
  - How might increasing trade volume affect complementary items (seeds->potions)
  - 

## Data
The OSRS API provides two sets of data that I will use. The first is information about each item that currently exists in the game. This includes an item id, members item or not, in-game examine text, and name of the item. This data changes less often because items and updates occur less frequently than economy transactions. An example table can be found in the notebooks folder called latest_osrs_items.

The most interesting data is the five minute price updates. Querying the api will return all items that have been traded in the last five minutes so low volume items will not appear often. Each query for the prices returns an item id, avg high and low prices, high and low volumes, and a UNIX timestamp. Many examples of this data are in the prices folder in any one of the csv files.


## Data Management
When I started this project, I was storing new data in separate csv files. I quickly realized that this was the wrong way to do this. Next, I started up a MySQL database on another computer, but I didn't want to deal with making separate users for accessing the data. I also do not know how to set up access outside of my own network. I decided to switch to SQlite for the rest of the project. 

I have finished collecting past data starting from March 08, 2021 1:35:00 until September 2022. I have a few scripts that can run to keep the database updated. The first script is Get_LatestPriceCSVs() that keeps track of the latest timestamp of data requested, gets the new data, increments the timestamp by five minutes (300 sec), and saves the csv to a Data_CSVs folder. The next script is called runTableAdder(). It iterates through the CSVs in the Data_CSVs folder and adds each to the database and moves them to the Imported folder after they are added. I need to add some method for deleting the oldest X files. A script called Update-DB.py runs both of these in sequence. It can be run at any time to get the database caught up to the current date. 

### Tables
My database contains two tables. One is for all of the item data so that I can get the item names and examine text. The other contains all entries for item prices. The notebooks where I created these tables are called createitemdb.ipynb and createpricetable.ipynb.

First, I pull the price data from the API. Then, I format it into a pandas dataframe and change some datatypes. After that, I put each row into the prices table of the database.

*Note: Pandas datatypes cause issues when adding the data to the database. I explicitly cast each value as the correct type before adding the data.


