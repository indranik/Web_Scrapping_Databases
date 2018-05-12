The goal of this assignment was building a web application that scrapes various websites for data related to the Mission to Mars and displaying the information in a single HTML page. 

Initial scraping was done using Jupyter Notebook(mission_to_mars.ipynb), BeautifulSoup, Pandas, and Requests/Splinter.

Data Scrapped: 

1. Latest News title and text from Nasa Mars News Site - https://mars.nasa.gov/news/
2. Featured image from the Caltech/Nasa's Jet Proplusion Lab - https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
3. Latest Weather conditions from the Mars Weather twitter account. 
4. Facts about the planet including Diameter, Mass, etc. from the Mars Facts webpage - https://space-facts.com/mars/
5. Images of the Mars Hemispheres from USGS Astrogeology site - https://astrogeology.usgs.gov/

Note: Mars Weather twitter account might have re-tweets that do not contain the weather report. Weather reports start with word "Sol". While scrapping tweet stream, non weather related tweets were ignored.

HTML/webpage creation :

Using MongoDB with Flask templating creted a new HTML page (\templates\index.html) that displays all of the information that was scraped from the URLs above following the steps below:

1. Converted the Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that executes all the scraping code from above and return one Python dictionary containing all of the scraped data.
2. Created a route called /scrape that imports scrape_mars.py script and call the scrape function.
3. Stored the return value in Mongo as a Python dictionary.
4. Created a root route / that queries the Mongo database and passes the mars data into HTML template (index.html) to display the data.
