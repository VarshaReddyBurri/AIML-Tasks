#!/usr/bin/env python
# coding: utf-8

# In[3]:


def remove_punc(input_text):
    punctuation_marks=['.',',','!','?',';',':','-','_','"',"'", \
                       '(',')','[',']','{','}','/','\\','@', \
                       '#','$','%','^','&','*','+','=','<','>', \
                      '|','`','~']
    output_text = ""
    for char in input_text:
        if char not in punctuation_marks:
            output_text += char
    return output_text


# In[9]:


remove_punc('''Emi!, "Cheyatle bhavi?"''')


# In[21]:


def remove_stopwords(input_text):
    stopwords=["is","and","the","a","an","in","on","at","for","with"]
    output_text = ""
    for char in input_text:
        if char not in stopwords:
            output_text += char
    return output_text


# In[23]:


remove_stopwords('''Reshmi is the bad girl in the world, and gabbu and donga fellow''')


# In[43]:


def remove_stopwords(input_text):
    stop_words=["an","a","the","it","was","is","and"]
    words=input_text.split()
    filtered_words=[]
    for word in words:
        if word.lower() not in stop_words:
            filtered_words.append(word)
    output_text=' '.join(filtered_words)
    return(output_text)


# In[45]:


remove_stopwords("The movie was good and it is a hit")


# In[ ]:




