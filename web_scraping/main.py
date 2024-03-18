#import the necessary modules request and beautiful soup
import requests
from requests import HTTPError
from bs4 import BeautifulSoup
import csv
import os

#prepare the base file 
current_dir=os.getcwd()
file_path=os.path.join(current_dir,'Top_Films_2023.csv')
csv_file=open(file_path,'w+')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['S.NO','Title','Genre','Summary','Rating','Votes','Gross'])





#get the request txt ffrom the url

try:

    res=requests.get('https://www.imdb.com/list/ls576754431/?sort=num_votes,desc&st_dt=&mode=detail&page=1')

    #print(res.text)
    #parse and get the necessary details by creating instance of BeautifulSoup
    soup=BeautifulSoup(res.text,'html.parser')

    content=soup.find('div',class_='lister-list').find_all('div',class_='lister-item mode-detail')
    #print(len(content))
    for movie in content:
        main_content=movie.find('div',class_='lister-item-content')
        
        s_no=main_content.h3.span.text.strip('.')
        title=main_content.h3.a.text
        genre=main_content.p.find('span',class_='genre').text.replace(',','-').strip()
        rating=main_content.div.div.find('span',class_='ipl-rating-star__rating').text.strip()
        summary=main_content.find('p',class_='').text.strip()
        votes=main_content.find('span',{'name':'nv','data-value':True}).text.strip()
        try:

            gross=main_content.find('span',{'name':'nv'},text=lambda x: x and '$' in x).text.strip()
        except:
            gross=None


        print(s_no,title,genre,rating,summary,votes,gross)

        print('Writing to the csv file ........Done')
        csv_writer.writerow([s_no,title,genre,summary,rating,votes,gross])

#write to the csv file and closing it .
    csv_file.close()
except HTTPError as e:
    print(e)



