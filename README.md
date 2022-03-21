# GEoutlier_detection

The goal of this project is to detect outliers in transactions for the Old School Runescape (OSRS) economy in real-time. I use the Old School Runescape wiki API to pull new data and store it in a SQlite database. I would like to use this information to make a continuously updating list of items whos prices are being manipulated. 

## Data
The OSRS API provides two sets of data that I will use. The first is information about each item that currently exists in the game. This includes an item id, members item or not, in-game examine text, and name of the item. This data changes less often because items and updates occur less frequently than economy transactions. An example table can be found in the notebooks folder called latest_osrs_items.

The most interesting data is the five minute price updates. Querying the api will return all items that have been traded in the last five minutes so low volume items will not appear often. Each query for the prices returns an item id, avg high and low prices, high and low volumes, and a UNIX timestamp. Many examples of this data are in the prices folder in any one of the csv files.


## Data Management
When I started this project, I was storing new data in separate csv files. I quickly realized that this was the wrong way to do this. Next, I started up a MySQL database on another computer, but I didn't want to deal with making separate users for accessing the data. I also do not know how to set up access outside of my own network. I decided to switch to SQlite for the rest of the project.

### Tables
My database contains two tables. One is for all of the item data so that I can get the item names and examine text. The other contains all entries for item prices. The notebooks where I created these tables are called createitemdb.ipynb and createpricetable.ipynb.

First, I pull the price data from the API. Then, I format it into a pandas dataframe and change some datatypes. After that, I put each row into the prices table of the database.

*Note: Pandas datatypes cause issues when adding the data to the database. I explicitly cast each value as the correct type before adding the data.

I set up a notebook to add new data to the database every five minutes. This it the Task_scheduler notebook.

## Algorithm

I intend to implement a very simple algorithm just to get the whole project working. I am going to pull the last week of prices for each item and calculate an inter-quartile range (IQR), and 50th percentile for each item. Then, any price that falls outside of the IQR (i.e. plus or minus half the IQR from the 50th percentile) I will flag as an outlier.

### Problems
One big issue with this algorithm is that items with low volume may not have enough data in one week to accurately gauge outliers. I think I could fix this by adding a weight based on the trade volume and/or gather data from a longer time frame.

## Interface
After implementing the algorithm, I will make a simple website using streamlit or a similar package to display the items with potential manipulation.
