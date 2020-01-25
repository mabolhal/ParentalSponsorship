from bs4 import BeautifulSoup
import smtplib
import requests
import os

email_add = os.environ.get('gmailUser')
email_pass = os.environ.get('gmailPassword')

url1 = 'https://www.canada.ca/en/immigration-refugees-citizenship/news/notices/parents-grandparents-2020-update.html'
url2 = 'https://www.canada.ca/en/immigration-refugees-citizenship/news/notices/details-parents-grandparents-coming-soon.html'
r = requests.get(url1)
s = requests.get(url2)

soup1 = BeautifulSoup(r.content)
soup2 = BeautifulSoup(s.content)

for link in soup1.find_all('p'):
    print(link.text)
    
for link in soup2.find_all('p'):
    print(link.text)

file1 = open('immigrationDaily.txt', 'w')
for link in soup1.find_all('p'):
    file1.write(link.text)
    file1.write('\n')
file1.write('*'*25)
file1.write('\n')
for link in soup2.find_all('p'):
    file1.write(link.text)
    file1.write('\n')
file1.write('END End EnD eND')
file1.close()

with open('immigrationDaily.txt', 'r') as file1:
    with open('immigration1.txt', 'r') as file2:
        diff = set(file1).difference(file2)


if len(diff) == 0:
    with open('immigrationDaily.txt', 'w') as file1:
        file1.truncate()
else:
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo() #Identify with mail server we're using
    smtp.starttls()
    smtp.ehlo()
    
    smtp.login(email_add, email_pass)
    subject = 'Fill out the forms!'
    body = 'https://www.canada.ca/en/immigration-refugees-citizenship/news/notices/parents-grandparents-2020-update.html \nhttps://www.canada.ca/en/immigration-refugees-citizenship/news/notices/details-parents-grandparents-coming-soon.html'
    msg = f'Subject: {subject}\n\n{body}'
    
    smtp.sendmail('amusicated@gmail.com', 'amusicated@gmail.com', msg)
    
    
        




