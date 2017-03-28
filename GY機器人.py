
# coding: utf-8

# In[8]:

bye=["掰", "88", "掰掰", "再見", "滾", "走開"]
good=["爽", "開心", "高興", "哈哈哈"]
bad=["傷心", "難過", "很煩", "不爽", "爛"]
ask=["你哪位", "你壞掉了嗎"]
word=''
print("嗨～今天過得如何？")
k=0
while k<=1 :
    word=input("")
    if any(i in word for i in bye):
        print("跟你聊天真是浪費時間")
        k=k+100
    elif any(i in word for i in good):
        print("過太爽")
    elif any(i in word for i in bad):
        print("呵呵，還好我不是你")
    elif any(i in word for i in ask):
        print("乾你屁事喔")
    else:
        print("我聽不懂你公啥")


# In[ ]:



