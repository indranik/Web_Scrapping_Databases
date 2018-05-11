
# coding: utf-8

# In[280]:


# Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
from selenium import webdriver
import requests



# In[281]:

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)


# In[282]:

def scrape():
    browser = init_browser()
    FinalResults = {}
    # NASA Mars News
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    
    
    # In[283]:
    
    
    #html = requests.get(url)
    #soup = bs(html.text, 'html.parser')
    html = browser.html
    soup = bs(html, 'html.parser')
    
    
    # In[284]:
    
    
    results = soup.find_all('li',class_="slide")
    
    
    # In[285]:
    
    
    Latest_Title = results[0].find(class_="content_title").text
    Latest_Title_Para = results[0].find(class_="article_teaser_body").text
    #print(Latest_Title)
    #print(Latest_Title_Para)
    
    
    # In[286]:
    
    
    # JPL Mars Space Images
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)
    image_html = browser.html
    image_soup = bs(image_html, 'html.parser')
    results = image_soup.find_all('a',class_="button fancybox")
    #print(results)
    #Image Location : Features Image
    image_loc = results[0].attrs['data-fancybox-href']
    image_loc = 'https://www.jpl.nasa.gov' + image_loc
    
    #print(image_loc)
    #Latest_Title_Para = results[0].find(class_="article_teaser_body").text
    
    
    # In[287]:
    
    
    #Mars Weather
    Twitter_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(Twitter_url)
    twitter_html = browser.html
    twitter_soup = bs(twitter_html, 'html.parser')
    #print(twitter_soup)
    results = twitter_soup.find_all('ol',{"id": "stream-items-id"})
    weatherTweetFound = False
    cnt = 0
    
    while (weatherTweetFound == False):
        mars_weather = results[0].find_all('p',class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")[cnt].text
        if (mars_weather.split()[0]) == "Sol":
            weatherTweetFound = True
        else:
            weatherTweetFound = False
            cnt = cnt+1
    #print(mars_weather)
    
    
    # In[288]:
    
    
    #Mars Facts
    MarsFacts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(MarsFacts_url)
    #print(type(tables))
    MarsFactdf = tables[0]
    
    #To change the column maps...first convert the column name data type to string
    MarsFactdf.columns = MarsFactdf.columns.map(str)
    MarsFactdf = MarsFactdf.rename( columns={"0": "Decscription", "1": "Value"})
    MarsFactdf.set_index('Decscription',inplace=True)
   
   # MarsFacts_html_table = MarsFactdf.to_html(escape = False).strip()
    MarsFacts_html_table = MarsFactdf.to_html()
    #MarsFacts_html_table = MarsFacts_html_table.replace("\n", "")
    #MarsFactdf.to_html('MarsFacts_html_table')
    
    
    # In[339]:
    
    
    #Mars Hemispheres
    MarsHemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(MarsHemispheres_url)
    MarsHemispheres_html = browser.html
    MarsHemispheres_soup = bs(MarsHemispheres_html, 'html.parser')
    
    results = MarsHemispheres_soup.find_all(class_="item")
    #print(results)
    hemisphere_image_urls = []
    HemisphereURL = "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/"
    for result in results:
        #image_url= 'https://astrogeology.usgs.gov'+result.a['href']+'.tif/full.jpg'
        title = result.a.img['alt']
        title_Splt = title.split()
        
        if(len(title_Splt) ==4):
            title1 = title_Splt[0].lower() + "_" + title_Splt[2].lower()
            title = title_Splt[0] + " " + title_Splt[1]
        else:
            title1 = title_Splt[0].lower() + "_"  +title_Splt[1].lower() + "_" + title_Splt[3].lower()
            title = title_Splt[0] + " " + title_Splt[1] + " " + title_Splt[2]   
        
        image_url= HemisphereURL+ title1 +'.tif/full.jpg'
        hemisphere_image_urls.append({'title' : title ,'image_url' : image_url})
        
    finalresults = {
        "latesttitle": Latest_Title,
        "latesttitlepara": Latest_Title_Para,
        "featimageLoc": image_loc,
        "marsweather": mars_weather,
        "marsfactshtmltable" : MarsFacts_html_table,
        "hemisphereimageurls" : hemisphere_image_urls
        
    }
   # print(hemisphere_image_urls[0]["image_url"])
    
   
    return finalresults


