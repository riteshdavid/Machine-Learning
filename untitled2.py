# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sLnoNnJp6vyugx9H-9h0biQMPqaFULdw
"""

from transformers import pipeline

import csv
import pandas as pd

import requests

from bs4 import BeautifulSoup

feed=requests.get('https://news.google.com/rss/search?q=green+hydrogen&qsearchterm=green+hydrogen&hl=en-IN&gl=IN&ceid=IN:en ')

soup=BeautifulSoup(feed.text,'html.parser')

title_tags=soup.find_all('title')

with open('sentiment-1.csv','w') as sent:
  csvwriter=csv.writer(sent)
  csvwriter.writerow(['headings']) 
  for i in title_tags:
    print(i.text)
    csvwriter.writerow([i.text.strip()])

df = pd.read_csv("sentiment-1.csv",sep=",")
print(df.head())

classifier=pipeline("sentiment-analysis")

for i,j in df.iterrows():
  df["Score"][i]=float(classifier(df["headings"][i])[0]['score'])

df



