import requests
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from bs4 import BeautifulSoup
import time
import numpy
import calendar


#TODO:  Parse dates rather than first three letters of month

#right now just passing a month in - later a time range

def getMonthOfPosts(month, postCollection):
    monthOfPosts = []
    #append post data for posts with that month label
    for post in postCollection:)
        if(post[0] == month):
            monthOfPosts.append(post[1])
    return monthOfPosts

def getUserPostHistory(userId):
    
    #don't do this kids
    finished = False
    
    timeStampedPosts = []
    
    #get user postcount
    #we can store the user's posts so we don't have to do this again, if we were 
    #to set up an API users could do this through
    
    pageNum = 0
    pages = 2
    
    try:
        while(pages >  0):
            pages -= 1
            print("next")
            timeStampedPosts += processPostsPage(pageNum, userId)
            #print(nextPageOfPosts)
            time.sleep(1)
            print("next2")
            #timeStampedPosts = {**timeStampedPosts, **nextPageOfPosts}
            #print(timeSt)
            pageNum = pageNum+1
            
    except Exception as e:
        print(e)
        
    return timeStampedPosts
        
def illikiStopWordFilter(text):
     print("entering stopwordfilter")
     print(text)
     # until I get more sophisticated parsing going on I can add common words to the stopword filter
     stopwords = ["post","posts","Bitcoin", "one"]
     if(text != None):
         filteredText = " ".join([word for word in text.split() if word not in stopwords])
     else:
         filteredText = ""
        
     print(filteredText)
     print("exit stopwordfilter")
     return filteredText
     

def processPostsPage(pageNumber, userId):
    
    datePostPairs =  []
    
    data= getPageData(pageNumber, userId)
    
    print("enter")
    #python Beautiful soup library lets us search for and filter out html elemetns
    soup = BeautifulSoup(data)
    
    dates, postsOnPage = isolatePostDivs(soup)
    
    print(dates)
    print(postsOnPage)
    #mostly a C# programmer and would inject a filter using dependency injection
    #might get the stopwords list
    postsOnPage = list(map(illikiStopWordFilter, postsOnPage))
    
    datePostPairs = zip(dates,postsOnPage)
    print(datePostPairs)
    
    
    #nextCloud = WordCloud(width=1830, height=900).generate(alltext)
        
    #wordCloudsForPageOfPosts.append(nextCloud)
    print("exit")
    return datePostPairs
 
    
def parseDivsFromPosts(posts):
    for div in posts:
        allText += " " + div.get_text()
    
    


def getPageData(pageNumber, userId):
    pageUrl = "https://bitcointalk.org/index.php?action=profile;u=" + str(userId) + ";sa=showPosts;start="+str(pageNumber*20)
    print(pageUrl)
    response = requests.get(pageUrl)
    return response.content  
    
    
def isolatePostDivs(soup):
    
    print("enter isolatePostDivs")
    dates = []
    
    headersOnPage  = soup.findAll("td", {"class" : "middletext"})
    print(headersOnPage)
    count = 0;
    for header in headersOnPage:
        
        if(count % 2 == 1):
            
            date = str(header)[-43:-40]
            print(date)
            #don't feel like using a reg expression right now
            dates.append(date)
        count = count + 1
         
    postsOnPage = soup.findAll("div", { "class" : "post" })
    
    #remove quotes and quoteheaders
    for div in soup.find_all("div", {'class':'quote'}): 
        div.decompose()
    for div in soup.find_all("div", {'class':'quoteheader'}): 
        div.decompose()
    print(postsOnPage)
    postsOnPage = [str(post.text) for post in postsOnPage]
    print(postsOnPage)
    print(dates)
    print("exit isolatePostDivs")
    return dates, postsOnPage
    
    
#def builtPlotFromPosts(width, height, numberRows, numberColumns, texts):
#    fig = plt.figure(figsize=(width,height))
#    count = 1;
#    for text in texts:
#        subplot = fig.add_subplot(numberRows, numberColumns, count)
#        #hack to delete tick marks
#        for a in fig.get_axes():
#            a.set_xticks([])
#            a.set_yticks([])
#        count += 1
#        nextCloud = WordCloud(width=1830, height=900).generate(text)
#        plt.imshow(nextCloud)
#
#def buildPlot(userId, numberOfPosts):
#   
#
#    
#    currentPage = 0
#    
#    count = 0
#    
#    while(count < numberOfPosts):
#        
#        #sleep in between grabbing pages of posts for a stress free bitcointalk crawl
#        time.sleep(1)
#        
#        #grab the clouds for that page
#        clouds = processPostsPage(currentPage,userId)
#        
#        currentPage = currentPage + 1
#        #display the clouds until we reach the right number
#        for cloud in clouds:
#            count = count+1
#            if(count <= numberOfPosts):
#                a = fig.add_subplot(1,1,count)
#                
#                
#                #a.set_title("Page  " + str(count))
#                plt.imshow(cloud)
#            
    
def buildWordCloud(text):
    nextCloud = WordCloud(width=1600, height=900).generate(text)
    return nextCloud
            

def plotClouds(clouds, numberRows, numberCols, width, height):
    count = 1
    fig = plt.figure(figsize=(width,height))
    print(len(clouds))
    for cloud in clouds:
        subplot  = fig.add_subplot(numberRows,numberCols,count)
        for a in fig.get_axes():
            a.set_xticks([])
            a.set_yticks([])
            a.set_title("Post " + str(count))
        count = count + 1
        plt.imshow(cloud)
        
userID = 164822
userPosts = getUserPostHistory(userID)

decemberPosts = getMonthOfPosts('Dec', userPosts)

#decemberCloud = buildWordCloud(" ".join(decemberPosts))
#
#plotClouds([decemberCloud],1,1,500,500)

#plt.show()