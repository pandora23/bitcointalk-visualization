

bitcointalk-visualization

OUR DIRECTION IN TERMS OF VISION AND DEVELOPMENT IS STILL BEING RESOLVED.  WAITING ON MORE TEAM MEMBERS TO DISCUSS FURTHER.

This is the main repository for the bitcointalk visualization project.
Trello: https://trello.com/b/fBefa8LD/bct-visualization-project-iteration-1

Scope:

1. To develop methods for 'benignly' crawling and extracting data from Bitcointalk user posts and ANN threads. Currently using: Python, Beautiful Soup

2. To perform automated visualization and data analytics on this data which may including:

       -sentiment analysis and emotion detection (have our own working system)

       -word clouds, word trees, and other surface level text visualization

       -deeper level analysis of meaning

       -time series analysis and prediction

       -machine learning and data mining to perform classification tasks (sklearn to start)
       
       -topic modeling
       

On the following Possible tasks:

       -ICO and coin analysis (via ANN threads) in general

       -User Analysis

       -Shilling detection
       
       -Topic modeling and visualization to show themes and keywords for different new coins.


3. To develop a backend which will host an API

       -Some type of Database (both MySQL and Mongo would be fine for me) to store data.

       -Python Tornado (Async) for the API

       -A 'queue' for safe crawling.  One page/second.

       -Python for the visualization and analytics as discussed above.

       -Eventual login system. (maybe)

4. To develop a front end.

       -I like Angular.js and Bootstrap but am open for suggestions.

       -Allows users to request visualizations.


Scaling Considerations: A bottleneck will be the crawl delay, one page grab per second. ALL post and thread data will be stored on the server. When a request is made we will look in a hash table (bloom table might be nice) to see if the page has already been added. If so we don't need to crawl. With continued usage crawling BCT should become minimal. By providing an API others will no longer need to crawl old post history as well whoever wants to build apps on top of the API.
