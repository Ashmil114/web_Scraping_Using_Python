import requests
from bs4 import BeautifulSoup
from csv import writer


url = 'https://in.jobrapido.com/?q=job&r=auto&utm_source=yahoo&utm_medium=cpc&utm_campaign=IN_GENERIC_SEARCH&r=auto&utm_agid=756670074&utm_kwid=kwd-12017287927:loc-90&ext=&int=&phy=143956&mt=e&dev=c&net=o&msclkid=c547cc19258a18d0727daa32766a8b00&utm_source=bing&utm_medium=cpc&utm_campaign=IN_GENERIC_SEARCH&utm_term=job&utm_content=Jobs'
page = requests.get(url)
print(page)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('div',class_='result-item__wrapper')

with open('job.csv','w',newline='',encoding='utf8') as f :
    thewriter = writer(f)
    header = ['Job Title','Company','Location']
    thewriter.writerow(header)

    for result in results :
        title = result.find('div',class_='result-item__title').text.replace('\n','').strip()
        location = result.find('div',class_='result-item__location').find('span').text.replace('\n','').strip()
        company= result.find('div',class_='result-item__company').find('span').text.replace('\n','').strip()
        job=[title,company,location]
        thewriter.writerow(job)
    print('Done')

