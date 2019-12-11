Analysis of twitter feed: Brand Comparison for fashion magazines :smile: Yue:star: Liu :girl:
=========================

User Instructions
-------------------

Fill in your `Twitter Consumer API keys and Access token & access token secret` in twitter_credentials.py 

Product Mission
-----------------
For women, 
Who want to know the latest news about fashion,
The Brand Comparing is a recommendation system,
That need to know the differences between the two magazines,
Unlike a blog written by an editor,
Our product makes a through comparison via social media.  

### Target Users
Our target users are young female, and their friends.
### Users' Story
As a twitter user, I want to know the like and follow of the different brands, so that I can find the topic I like, with correct hashtag. As a twitterer likes the topic of fashion(content consumer), I want to get the products I like in the coming quarter/ year.
### MVP
* sentiment analysis
* get the tweets 

System Design(address users stories)
-------------------------------------
* Streaming
* Get the published tweets
* Analyze the tweet data
* Sentiment Analysis 
![ALT Text](https://github.com/yueyue4737/EC601MiniProject1_YueLiu/blob/master/data/system_design.png)

How to build the system
------------------------
Testing
-------
### Error Condition
* 401 Error
401 Unauthorized (RFC 7235)Similar to 403 Forbidden, but specifically for use when authentication is required and has failed or has not yet been provided. 
* debug
The error messages cannot give us exact line sometimes. If you are in the terminal, the print function will help you a lot. If you are in the IDE, you can build your own test function. If the program contains so many lines, please add breakpoints. 
### What is in my own API?
* get tweets(livetweets, published tweets, removing irrelevant colunms)
* sentiment analysis in two different ways
### Text Document
* tweet_live.txt(streaming), tweet.txt(public)
* tweetE.csv, tweetV.csv
### Results
![Alt Text](https://github.com/yueyue4737/EC601MiniProject1_YueLiu/blob/master/data/V_SENT1.png)
![Alt Text](https://github.com/yueyue4737/EC601MiniProject1_YueLiu/blob/master/data/e_sent1.png)
Lesson Learned
-----------------
### what's better to do?
I also want to compare the outcomes of visualization by using R and Python separately, which is mentioned in the “what’s better part”. 
### what to avoid?
<p>(1) wait for a teamwork, assuming everything need to do by myself;
(2) NEVER TRUST THE SHOW-OFF WORDS<p>
  
More Markdown Files
----------------------
### avoidErrors.md
### 2writeAPI.md

LINKS
---------------------
### Coursework in different sprints: 
<p> https://drive.google.com/file/d/1DtGXmL6IyaYiw6_5DZkvbMIYlrg1Xbxq/view?usp=sharing <p>  

### Mini Project 1 REPORT(full text): 
<p> https://docs.google.com/document/d/1B0dwUrllNpGTK2wGcTIFWn-VMFJm3Vs1_x9pHlwsm8I/edit?usp=sharing <p> 

### Mini Project 1 Prsentation(Multiple ways& comparison in two brands): 
<p> https://docs.google.com/presentation/d/14EmqOZQLUaHza7neDxxgbtlM6KUs0xONT0W19ziohVU/edit?usp=sharing <p>
