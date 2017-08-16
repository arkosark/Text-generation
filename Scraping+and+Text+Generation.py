
# coding: utf-8

# In[33]:

import bs4 as bs
import nltk
import urllib.request
import pandas as pd
import random

df_urls = pd.read_excel('Url_List.xlsx')
list_article_text = []
article = ''


# In[35]:

for index,rows in df_urls.iterrows():
    source = urllib.request.urlopen(df_urls.iloc[index]['URL'])
    soup = bs.BeautifulSoup(source,'lxml')
    i=1
    length= len(soup.find_all('p'))-13
    for i in range(1,length):
        article += (soup.find_all('p')[i].text + '')
        i+=1
    #list_article_text.append(article) 
    #article = '' 
#list_article_text


# In[12]:

class A(object):

    def __init__ (self, order):
        self.order = order
        self.group_size = self.order + 1
        self.text = None
        self.graph = {}
        return

    def train (self, text):
        #self.text = file (filename).read ().split ()
        self.text = nltk.word_tokenize(text) #self.text + self.text [ : self.order]
        #print(self.text)
        for i in range (0, len (self.text) - self.group_size):
            key = tuple (self.text [i : i + self.order] )
            value = self.text [i + self.order]
            if key in self.graph:
                self.graph [key] .append (value)
            else:
                self.graph [key] = [value]
        #print(self.graph)        
        return 


    def generate (self,length):
        index = random.randint (0, len (self.text) - self.order)
        result = self.text[index : index + self.order]
        #print(index,result)
        for i in range (length):
            state = tuple (result [len (result) - self.order : ] )
            #print(state)
            next_word = random.choice (self.graph [state] )
            result.append (next_word)
            #print(result)
        return " ".join (result [self.order : ] )


# In[28]:

a = A(6)
a.train(article)
result = a.generate(500)


# In[29]:

result


# In[ ]:



