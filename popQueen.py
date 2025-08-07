import heapq
import requests
import yagmail
import os

from dotenv import load_dotenv

from emailList import emailList
from queenScore import queenScore
from getQueens import getQueens

yag = yagmail.SMTP("benjaminbradford43@gmail.com", f'{os.getenv("EMAIL_PASSWORD")}')

queens = getQueens()
topThree = heapq.nlargest(3, queens, key=lambda q:queenScore(q))

contents = 'The Top 3 Queens of the day are...\n'

for i in range(2, -1, -1): 
    contents += f'{i + 1} - {topThree[i]['name']}\n'

for email in emailList: 
    yag.send(to=email, subject="Queens of the Day", contents=contents)