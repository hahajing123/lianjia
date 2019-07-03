#!/usr/bin/env python
# coding: utf-8

# In[4]:


'''
import requests
########### 根据url 获取数据 ##########################################
def data_crawl(url):
    header={'Cookie':'TY_SESSION_ID=8613fce5-cc0a-4ed4-ade1-b99f1576b307; lianjia_uuid=8ae0060a-7f18-4cf2-a456-72b4a35e36d1; _smt_uid=5cac5850.414b0663; UM_distinctid=16a0138fb6490a-03f6ff71ea0ac6-5f1d3a17-15f900-16a0138fb65845; _ga=GA1.2.284772620.1554798675; ljref=pc_sem_baidu_sstg_lpc; select_city=210100; all-lj=ba32fa4540e52c45d4c94b9a16e82078; lianjia_ssid=bc4f2b64-60a6-4456-8839-5dbb87c275d5; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1554798672,1554960066; CNZZDATA1255849613=1981234100-1554797903-https%253A%252F%252Fwww.baidu.com%252F%7C1554955102; CNZZDATA1254525948=772856037-1554797444-https%253A%252F%252Fwww.baidu.com%252F%7C1554955692; CNZZDATA1255633284=1770314509-1554793869-https%253A%252F%252Fwww.baidu.com%252F%7C1554956058; CNZZDATA1255604082=966506862-1554793869-https%253A%252F%252Fwww.baidu.com%252F%7C1554955755; _qzjc=1; _jzqa=1.1362142260894983700.1554798673.1554798673.1554960066.2; _jzqc=1; _jzqy=1.1554798673.1554960066.2.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6%E7%BD%91.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6%20%E8%B4%9D%E5%A3%B3; _jzqckmp=1; _gid=GA1.2.803114113.1554960070; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1554960089; _qzja=1.2035633223.1554798672712.1554798672713.1554960066028.1554960066028.1554960089322.0.0.0.7.2; _qzjb=1.1554960066027.2.0.0.0; _qzjto=2.1.0; _jzqb=1.2.10.1554960066.1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216a0138fdf39e-0d7bd2cc72beb5-5f1d3a17-1440000-16a0138fdf4941%22%2C%22%24device_id%22%3A%2216a0138fdf39e-0d7bd2cc72beb5-5f1d3a17-1440000-16a0138fdf4941%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22ppc%22%2C%22%24latest_utm_campaign%22%3A%22%E6%B2%88%E9%98%B3_%E5%95%86%E6%9C%BA_%E7%9F%AD%E8%AF%AD%22%2C%22%24latest_utm_content%22%3A%22%E5%93%81%E7%89%8C%22%2C%22%24latest_utm_term%22%3A%22%E9%93%BE%E5%AE%B6%22%7D%7D','User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    r1 = requests.get(url,headers=header)
    soup = BeautifulSoup(r1.text,'lxml')
    item= {}
    #print(type(item))
    print("************** 获取:"+url+"  数据****************")
    item['title'] = soup.h1.text
    item['info'] = soup.find("div",attrs={"class":"sub"}).text
    item['price'] = soup.find("span",attrs={"class":"total"}).text #价格
    item['room_mainInfo'] = soup.find("div",attrs={"class":"room"}).find("div",attrs={"class":"subInfo"}).text
    item['room_subInfo'] = soup.find("div",attrs={"class":"room"}).find("div",attrs={"class":"subInfo"}).text
    item['eara_mainInfo'] = soup.find("div",attrs={"class":"area"}).find("div",attrs={"class":"mainInfo"}).text #面积
    item['eara_subInfo'] = soup.find("div",attrs={"class":"area"}).find("div",attrs={"class":"subInfo"}).text
    item['type_mainInfo'] = soup.find("div",attrs={"class":"type"}).find("div",attrs={"class":"mainInfo"}).text
    item['type_subInfo'] = soup.find("div",attrs={"class":"type"}).find("div",attrs={"class":"subInfo"}).text 
    item['communityName'] = soup.find("div",attrs={"class":"communityName"}).find("a",attrs={"class":"info"}).text #小区名
    item['areaName'] = soup.find("div",attrs={"class":"areaName"}).find("a").text #哪个区
    #print(item)
    
    #print(soup.find("div",attrs={"class":"areaName"}).find("a").text)
    if(item['title'] != ''):
        return item
    else:
        return "获取失败" 
###############  函数结束  ##############################################

header={'Cookie':'TY_SESSION_ID=8613fce5-cc0a-4ed4-ade1-b99f1576b307; lianjia_uuid=8ae0060a-7f18-4cf2-a456-72b4a35e36d1; _smt_uid=5cac5850.414b0663; UM_distinctid=16a0138fb6490a-03f6ff71ea0ac6-5f1d3a17-15f900-16a0138fb65845; _ga=GA1.2.284772620.1554798675; ljref=pc_sem_baidu_sstg_lpc; select_city=210100; all-lj=ba32fa4540e52c45d4c94b9a16e82078; lianjia_ssid=bc4f2b64-60a6-4456-8839-5dbb87c275d5; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1554798672,1554960066; CNZZDATA1255849613=1981234100-1554797903-https%253A%252F%252Fwww.baidu.com%252F%7C1554955102; CNZZDATA1254525948=772856037-1554797444-https%253A%252F%252Fwww.baidu.com%252F%7C1554955692; CNZZDATA1255633284=1770314509-1554793869-https%253A%252F%252Fwww.baidu.com%252F%7C1554956058; CNZZDATA1255604082=966506862-1554793869-https%253A%252F%252Fwww.baidu.com%252F%7C1554955755; _qzjc=1; _jzqa=1.1362142260894983700.1554798673.1554798673.1554960066.2; _jzqc=1; _jzqy=1.1554798673.1554960066.2.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6%E7%BD%91.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6%20%E8%B4%9D%E5%A3%B3; _jzqckmp=1; _gid=GA1.2.803114113.1554960070; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1554960089; _qzja=1.2035633223.1554798672712.1554798672713.1554960066028.1554960066028.1554960089322.0.0.0.7.2; _qzjb=1.1554960066027.2.0.0.0; _qzjto=2.1.0; _jzqb=1.2.10.1554960066.1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216a0138fdf39e-0d7bd2cc72beb5-5f1d3a17-1440000-16a0138fdf4941%22%2C%22%24device_id%22%3A%2216a0138fdf39e-0d7bd2cc72beb5-5f1d3a17-1440000-16a0138fdf4941%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22ppc%22%2C%22%24latest_utm_campaign%22%3A%22%E6%B2%88%E9%98%B3_%E5%95%86%E6%9C%BA_%E7%9F%AD%E8%AF%AD%22%2C%22%24latest_utm_content%22%3A%22%E5%93%81%E7%89%8C%22%2C%22%24latest_utm_term%22%3A%22%E9%93%BE%E5%AE%B6%22%7D%7D','User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
p_start = 51
p_end = 89
for page in range(p_start,p_end+1):
    print("第",page,"页")
    lianjia = "https://sy.lianjia.com/ershoufang/shenbeixinqu/pg"+str(page)+"/"
    print(lianjia)
    r = requests.get(lianjia,headers=header)
    r.encoding ='UTF-8'
    #print(r.status_code,r.encoding,r.text)

#########  获取连接地址  ###################
    from bs4 import BeautifulSoup
    soap = BeautifulSoup(r.text,"lxml")
    house_list = soap.find("ul",class_="class="list comment-list"")
    #print(house_list)
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    house_list = house_list.find_all('li',attrs={"class":"clear LOGCLICKDATA"})
    print(len(house_list))
    #print(house_list)
    url_list = []
    print(type(url_list))
    for house in house_list:
        url_list.append(house.a.attrs['href'])
        print(house.a.attrs['href'])
################ /获取链接地址 ################################
    info_list = []
    for i in url_list:
        data_i = data_crawl(i)
        if(data_i != "获取失败"):
            info_list.append(data_i)
    print(info_list)
    ######################## 保存数据 ##########################################
    import pandas as pd
    import os
    data =  pd.DataFrame(info_list,columns=info_list[0].keys())
    print("-----------------------第"+str(page)+"页数据"+str(len(info_list))+"条----------------")
    
    if(os.path.exists("house.csv")):
        data.to_csv('house.csv',mode='a', index=False, header=False)
    else:
        data.to_csv('house.csv')
    print("***************成功写入数据"+str(len(info_list))+"条**************************************")
    '''


# In[ ]:





# In[1]:


import pandas as pd
data = pd.read_csv('house.csv')
#del data['Unnamed: 0']
data_common=data[data['price']>0]
data_common.tail()


# In[2]:


data_common.shape[0]


# In[3]:


print("沈阳二手平均房价：%.2f 万元" %data_common['price'].mean())
print("沈阳二手最低房价：%.2f 万元" %data_common['price'].min())
print("沈阳二手最高房价：%.2f 万元："%data_common['price'].max())
print("沈阳二手中位房价：%.2f 万元："%data_common['price'].median())


# In[ ]:





# In[4]:


'''
data_common = data_common[data_common['price']<300]
print("沈阳二手平均房价：%.2f 万元" %data_common['price'].mean())
print("沈阳二手最低房价：%.2f 万元" %data_common['price'].min())
print("沈阳二手最高房价：%.2f 万元："%data_common['price'].max())
print("沈阳二手中位房价：%.2f 万元："%data_common['price'].median())
'''


# In[5]:


data[data['price']>=300]


# In[6]:


data[data['price']==13]


# In[54]:


data[data['price']==1750]


# In[7]:


#面积字段清洗
data['area'] = data['eara_mainInfo'].str.split('平米').str[0]

data['area'] = data['area'].astype(float)


print("最大房屋面积：%.2f" %data['area'].max())
print("最小房屋面积：%.2f" %data['area'].min())


# In[8]:


#面积单价
data['single_price'] = data['price']/data['area']
data


# In[9]:


print("房屋单价最高：%.2f  万元/平米" %data['single_price'].max())
print("房屋单价最低：%.2f 万元/平米" %data['single_price'].min())
print("房屋单价平均价格：%.2f 万元/平米" %data['single_price'].mean())
data[data['single_price'] > 4]


# In[10]:


#各个区的房价分组, 各个区的房源数量
grouped = data.groupby(['areaName'],as_index=False)['title'].count()
grouped


# In[11]:


#各个区的面积单价平均值
grouped_single_price = data.groupby(['areaName'],as_index=False)['single_price'].mean()
grouped_single_price.sort_values(by='single_price',ascending=False)


# In[12]:


#各个区的房屋价格平均值
grouped_price = data.groupby(['areaName'],as_index=False)['price'].mean()
grouped_price.sort_values(by='price',ascending=False)


# In[13]:


from pyecharts import  Scatter
print("ss")
data['price']


# In[14]:


scatter = Scatter("总价-面积散点图",'统计时间：2019-4-25')
scatter.add('🏠总价(单位：万元)',data['area'],data['price'],visual_type="color",visual_range=[10, 300],mark_point=['max'], is_visualmap = True,visual_pos = 'right',xaxis_name = '面积' , yaxis_name = '总价')
print(type(scatter))
print("aa")
#scatter.show_config()
scatter.render('./沈阳房价散点图.html')


# In[15]:


import pyecharts
from pyecharts import Map


# In[16]:


#各个行政区均价

grouped_single_price = data.groupby(['areaName'],as_index=False)['single_price'].mean()
grouped_single_price.sort_values(by='single_price',ascending=False)

attr = list(grouped_single_price['areaName'])
vv = grouped_single_price['single_price']*10000
value = list(vv.round(2))
print(type(grouped_single_price['single_price']))
#行政区的名称与map 中的保持一致
for i, dist in enumerate(attr):
    if(dist.find('区') == -1):
        attr[i] =  attr[i]+ '区'
            


    
print(attr)
print(value)
print(type(attr))
map = pyecharts.Map("沈阳各行政区二手房均价", "统计时间：2019-04-25", width=800, height=1600)
map.add(
    "二手房均价(单位：元)", attr, value, maptype= u"沈阳",is_legend_show = True,is_label_show = True,visual_range=[min(value),max(value)],is_visualmap=True,
)
map
#map.render("沈阳各行政区二手房均价.html")


# In[53]:


#各个行政区均价柱状图
grouped_single_price = data.groupby(['areaName'],as_index=False)['single_price'].mean()
#grouped_single_price =grouped_single_price.sort_values(by='single_price',ascending=False)

attr = list(grouped_single_price['areaName'])
value = list(grouped_single_price['single_price'].round(2))
print(grouped_single_price)
print(value)
line =pyecharts.Line('沈阳各行政区房价',"统计时间：2019-5-14")
line.add('每平米均价（单位：万元）',attr,value,is_label_show = True,mark_point=["max", "min"])
line


# In[18]:


#看看哪个小区的房价最高

community_data = data.groupby(['communityName'],as_index=False)['single_price'].mean().round(2)
community_data = community_data.sort_values(by='single_price',ascending=False)
temp = community_data.nlargest(10,'single_price')
print(temp)
#community_data.head(10)
bar_comm =pyecharts.Bar('沈阳豪华小区前10排行',"统计时间：2019-5-14")
bar_comm.add('每平米均价 单位：万元',list(temp['communityName']),list(temp['single_price']),is_label_show = True,xaxis_interval=0,xaxis_rotate=30)


# In[26]:


#词频
from jieba import posseg as psg
import collections
import sys
#imp.reload(sys)
#sys.setdefaultencoding('utf-8')


# In[28]:


'''分词'''
word_list = []
stop_words = ['花园','业主','出售']
string =  str(''.join(data['title']))
print(string)


# In[30]:


words = psg.cut(string)
for x in words:
    if len(x.word)==1:
        pass
    elif x.flag == 'x':
        pass
    elif x.word in stop_words:
        pass
    else:
        word_list.append(x.word)
    


# In[32]:


c = collections.Counter(word_list)
attr = []
value = []
for x in c.most_common(10):
    attr.append(x[0])
    value.append(x[1])

'''
柱形图
'''
Bar = pyecharts.Bar("标题中出现频率最高的10个词", "统计时间：2018-09-22")
Bar.add("出现次数", attr, value,mark_point=['max'],is_legend_show = False)
Bar.render
Bar


# In[36]:


'''生成词云'''
import imageio
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt


# In[50]:


back_color = imageio.imread('house10.jpg') 
words = ' '.join(word_list)
wc = WordCloud(background_color='white', 
               max_words=5000,  
               mask=back_color, 
               max_font_size=200, 
                font_path="SimHei.ttf",
               random_state=None
               )

wc.generate(words)
image_colors = ImageColorGenerator(back_color)
plt.figure(figsize = (15,8))
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis('off')
plt.show()
wc.to_file('comment.png')


# In[ ]:





# In[ ]:




