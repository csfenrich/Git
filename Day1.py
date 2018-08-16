
# coding: utf-8

# In[1]:


name = "superstar"


# In[2]:


age = 101


# In[3]:


print(name)


# In[4]:


print(age)


# In[5]:


print("my name is")


# In[6]:


print("my name is",name)


# In[7]:


print("my age is",age)


# In[8]:


print ("my name is",age,"and my age is",age)


# In[9]:


newage=age-50


# In[10]:


print(newage)


# In[11]:


multipliedage=age*2


# In[12]:


print("your age is actually",newage)


# In[13]:


print("your multiplied age is",multipliedage)


# In[14]:


sequence="CTAGCTAG"


# In[15]:


print(sequence)


# In[16]:


print(sequence[0])


# In[17]:


print(sequence[3])


# In[18]:


print("my fourth letter is",sequence[3])


# In[19]:


len(sequence)


# In[20]:


print("the length of the sequence is",len(sequence))


# In[21]:


COX1="CTAG"


# In[22]:


first_name="colleen"


# In[23]:


sequence[0:2]


# In[24]:


sequenc[0:3]


# In[25]:


sequence[0:3]


# In[26]:


type(sequence)


# In[27]:


type(age)


# In[28]:


COX2="TACG"


# In[29]:


COX1-COX2


# In[30]:


COX1+COX2


# In[31]:


firstname="colleen"


# In[32]:


lastname="fenrich"


# In[33]:


firstname+lastname


# In[34]:


firstname+ " " +lastname


# In[35]:


lens(age)


# In[36]:


len(age)


# In[37]:


name+age


# In[38]:


5**2


# In[39]:


print(5**2)


# In[40]:


print("f squared is", 5**2)


# In[41]:


5%2


# In[42]:


# This is a comment


# In[43]:


# adding two sequences because they turned out to be the same gene


# In[44]:


COX1+COX2


# In[45]:


max(23,2,5)


# In[46]:


max(3,len("colleen"))


# In[47]:


round(3.14159)


# In[48]:


round(3.14159,2)


# In[49]:


min(2,3,1)


# In[50]:


help(min)


# In[51]:


print(aege)


# In[52]:


max(21,32,45)


# In[53]:


max(21,32,45)+min(21,32,45)


# In[54]:


hundred_C ="c"*100


# In[55]:


print(hundred_C)


# In[56]:


COX1+hundred_C


# In[57]:


hundred_C+COX1


# In[58]:


len(hundred_C+COX1)


# In[59]:


import math


# In[60]:


math.cos(57)


# In[61]:


math.sin(90)


# In[62]:


math.sin(pi)


# In[63]:


math.sin(PI)


# In[65]:


print("the cos of 180 is",math.cos(180))


# In[66]:


math.pi


# In[67]:


math.sin(math.pi)


# In[68]:


math.cos(math.pi)


# In[69]:


help(math)


# In[70]:


import math as m


# In[71]:


m.cos(1)


# In[72]:


from math import cos


# In[73]:


cos(45)


# In[74]:


help(import)


# In[75]:


from math import *


# In[76]:


from math import*


# In[77]:


from math import pi,degrees


# In[78]:


angle=degrees(pi,2)


# In[79]:


from math import degrees
from math import pi


# In[81]:


angle=degrees(pi/2)


# In[82]:


print(angle)


# In[83]:


import pandas


# In[86]:


pandas.read_csv("data/gapminder_gdp_oceania.csv")


# In[87]:


pandas.read_csv("data/gapminder_gdp_oceania.csv")


# In[88]:


pandas.read.csv("data/gapminder_gdp_africa.csv")


# In[89]:


import pandas


# In[90]:


pandas.read.csv("data/gapminder_gdp_africa.csv")


# In[91]:


pandas.read.csv("data/gapminder_gdp_africa.csv")


# In[92]:


pandas.read_csv("data/gapminder_gdp_africa.csv")


# In[94]:


pandas.read_csv("data/gapminder/gdp_americas.csv")


# In[95]:


pandas.read_csv("data/gapminder_gdp_americas.csv")


# In[96]:


pandas.read_csv("data/gapminder_gdp_asia.csv")


# In[97]:


pandas.read_csv("data/gapminder_gdp_europe.csv")


# In[98]:


pandas.read_csv("data/gapminder_europe.csv")


# In[99]:


pandas.read_csv("data/gapminder_gdp_europe.csv")


# In[100]:


data=pandas.read_csv("data/gapminder_gdp_oceania.csv")


# In[101]:


print(data)


# In[102]:


data=pandas.read_csv("data/gapminder_gdp_oceania.csv", index_col="country")


# In[103]:


data


# In[104]:


data.info()


# In[105]:


data


# In[106]:


data.T


# In[107]:


data.describe()


# In[108]:


data.T.describe()


# In[109]:


americas=pandas.read_csv("data/gapminder_gdp_americas.csv")


# In[110]:


americas.describe()


# In[111]:


americas.T.describe()


# In[112]:


print(americas)


# In[113]:


americas=pandas.read_csv("data/gapminder_gdp_americas.csv",index_col="country")


# In[114]:


americas.describe()


# In[115]:


americas.T.describe()


# In[116]:


data.columns


# In[117]:


data.rows


# In[118]:


data.T.columns


# In[119]:


americas.columns


# In[120]:


data


# In[121]:


data(1,2)


# In[122]:


data.iloc[1,2]


# In[123]:


data.iloc[0,0]


# In[124]:


data.loc["Australia","gdpPercap_1952"]


# In[125]:


data.loc["Australia"]


# In[127]:


data.loc[:,"gdpPercap_1952"]


# In[128]:


data.loc[:, "gdpPercap_1952":"gdpPercap_1962"]


# In[129]:


data.iloc[0,0]


# In[130]:


data.iloc[0:2,0]


# In[131]:


data.iloc[0:2,0:3]


# In[132]:


data.ilo[0,0:3]


# In[134]:


data.iloc[0,0:3]


# In[137]:


data.loc["Australia","gdpPercap_1952":"gdpPercap_1962"]


# In[138]:


data.loc[:,"gdpPercap_1952":"gdpPercap_1962"].max()


# In[139]:


data.loc[:,"gdpPercap_1952":"gdpPercap_1962"].min()


# In[140]:


subset=data.loc[:,"gdpPercap_1952":"gdpPercap_1962"]


# In[141]:


print(subset)


# In[142]:


print(subset>11000)


# In[144]:


subset[subset>11000]


# In[145]:


subset[subset>11000].describe()


# In[151]:


europe=pandas.read_csv("data/gapminder_gdp_europe.csv",index_col="country")


# In[152]:


europe


# In[153]:


europe.loc["Serbia","gdpPercap_2007"]


# In[147]:


europe


# In[150]:





# In[154]:


europe


# In[156]:


europe_subset=europe.loc["Italy":"Norway","gdpPercap_1962":"gdpPercap_1972"]


# In[157]:


europe_subset


# In[158]:


europe_subset[europe_subset<15000].describe()

