#IMPORTING BACKEND SERVERS AND MODULES / LIBRARIES
from flask import Flask , render_template
from newsapi import NewsApiClient

app=Flask(__name__)


@app.route('/')
def Index():
    newsapi=NewsApiClient(api_key="c8d1dc60b88e4546be78180c73ab99ef")
    topheadlines=newsapi.get_top_headlines(sources="al-jazeera-english")

    articles=topheadlines['articles']
    
    #APPEND DATA TO LIST 
    desc=[]
    news=[]
    img=[]

    for i in range(len(articles)):
        my_articles=articles[i]
        
        news.append(my_articles['title'])
        desc.append(my_articles['description'])
        img.append(my_articles['urlToImage'])
    
    #DATA WHICH IS TO BE SENT 
    my_list=zip(news,desc,img)

    return render_template("index.html",context=my_list)


@app.route('/bbc')
def bbc():
    newsapi=NewsApiClient(api_key="c8d1dc60b88e4546be78180c73ab99ef")
    topheadlines=newsapi.get_top_headlines(sources="bbc-news")

    articles=topheadlines['articles']
    
    #APPEND DATA TO LIST 
    desc=[]
    news=[]
    img=[]

    for i in range(len(articles)):
        my_articles=articles[i]
        
        news.append(my_articles['title'])
        desc.append(my_articles['description'])
        img.append(my_articles['urlToImage'])
    
    #DATA WHICH IS TO BE SENT 
    my_list=zip(news,desc,img)

    return render_template("bbc.html",context=my_list)


@app.route('/ars_technica')
def ars_technica():
    newsapi=NewsApiClient(api_key="c8d1dc60b88e4546be78180c73ab99ef")
    topheadlines=newsapi.get_top_headlines(sources="ars-technica")

    articles=topheadlines['articles']
    
    #APPEND DATA TO LIST 
    desc=[]
    news=[]
    img=[]

    for i in range(len(articles)):
        my_articles=articles[i]
        
        news.append(my_articles['title'])
        desc.append(my_articles['description'])
        img.append(my_articles['urlToImage'])
    
    #DATA WHICH IS TO BE SENT 
    my_list=zip(news,desc,img)

    return render_template("ars_technica.html",context=my_list)



@app.route('/ansa')
def ansa():
    newsapi=NewsApiClient(api_key="c8d1dc60b88e4546be78180c73ab99ef")
    topheadlines=newsapi.get_top_headlines(sources="ansa")

    articles=topheadlines['articles']
    
    #APPEND DATA TO LIST 
    desc=[]
    news=[]
    img=[]

    for i in range(len(articles)):
        my_articles=articles[i]
        
        news.append(my_articles['title'])
        desc.append(my_articles['description'])
        img.append(my_articles['urlToImage'])
    
    #DATA WHICH IS TO BE SENT 
    my_list=zip(news,desc,img)

    return render_template("ansa.html",context=my_list)

@app.route('/blasting_news')
def blasting_news():
    newsapi=NewsApiClient(api_key="c8d1dc60b88e4546be78180c73ab99ef")
    topheadlines=newsapi.get_top_headlines(sources="blasting-news-br")

    articles=topheadlines['articles']
    
    #APPEND DATA TO LIST 
    desc=[]
    news=[]
    img=[]

    for i in range(len(articles)):
        my_articles=articles[i]
        
        news.append(my_articles['title'])
        desc.append(my_articles['description'])
        img.append(my_articles['urlToImage'])
    
    #DATA WHICH IS TO BE SENT 
    my_list=zip(news,desc,img)

    return render_template("blasting_news.html",context=my_list)


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)