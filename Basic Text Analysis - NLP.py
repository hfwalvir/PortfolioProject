#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install nltk


# In[ ]:


import nltk


# In[ ]:


nltk.download()


# # Tokenization

# In[11]:


from nltk.tokenize import sent_tokenize
text = """Hello Vanny, how are you doing today? The weather seems great!"""
tokenized_sent = sent_tokenize(text)
print(tokenized_sent)


# # WORD TOKENIZATION

# In[10]:


from nltk.tokenize import word_tokenize
tokenized_word = word_tokenize(text)
print(tokenized_word)


# # FREQUENCY DISTRIBUTION 

# In[7]:


from nltk.probability import FreqDist
fdist = FreqDist(tokenized_word)
print(fdist)


# In[8]:


fdist.most_common(2)


# In[9]:


#Frequency Distribution Plot
import matplotlib.pyplot as plt
fdist.plot(20,cumulative = False)
plt.show()


# # STOPWORDS

# In[13]:


from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))
print(stop_words)


# # REMOVE STOPWORDS

# In[14]:


filtered_sent = []
for w in tokenized_word :
    if w not in stop_words:
        filtered_sent.append(w)
print ("Tokenized sent",tokenized_word)
print("Filtered Sent :", filtered_sent)


# # STEMMING

# In[16]:


from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
ps = PorterStemmer()
stemmed_words = []
for w in filtered_sent:
    stemmed_words.append(ps.stem(w))
print("FIltered Sentence:",filtered_sent)
print("Stemmed Sentence:",stemmed_words)


# # POS Tagging

# In[20]:


sent = "Alber Einstient was born in ULM, Germany, in 1879."


# In[21]:


tokens = nltk.word_tokenize(sent)
print(tokens)


# In[22]:


nltk.pos_tag(tokens)

