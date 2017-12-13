# bitcointalk-visualization
This is the main repository for the bitcointalk visualization project.  

Scope:

1.  To develop methods for 'benignly' crawling and extracting data from Bitcointalk user posts and ANN threads.
      Currently using:  Python,  Beautiful Soup
      
2.  To perform automated visualization and data analytics on this data which may including:

      -sentiment analysis and emotion detection (have our own working system)
      
      -word clouds, word trees, and other surface level text visualization 
      
      -deeper level analysis of meaning
      
      -time series analysis
      
      -machine learning and data mining to perform classification tasks (sklearn to start)
     
     On the following Possible tasks:
     
       -User Analysis
       
       -ICO Analysis
       
       -Scam/Scammer Detection
       
       -Shitpost/Shitposter Analyis and Detection
      
3. To develop a backend which will host an API

       -Some type of Database (both MySQL and Mongo would be fine for me) to store data.
       
       -Python Tornado (Async) for the API
       
       -A 'queue' for safe crawling.  One page/second.
       
       -Python for the visualization and analytics as discussed above.
       
       -Eventual login system. (PHP of Python.)
       
4.  To develop a front end.

       -I like Angular.js and Bootstrap but am open for suggestions.
       
       -Allows users to request visualizations.
       
       -Eventual login system.
       
Scaling Considerations:  A bottleneck will be the crawl delay, one page grab per second.  The user requests are asynchronously made and
then spawned into several processes on the Python side of things. Ideally page requests will be queued in an interlaced fashion so users won't
have to wait for some other user to finish his ANN visualization.   ALL post and thread data will be stored on the server.  When a request is
made we will look in a hash table (bloom table might be nice) to see if the page has already been added. If so we don't need to crawl. 
With continued usage crawling BCT should become minimal.  By providing an API others will no longer need to crawl old post history as well
whoever wants to build apps on top of the API.

