def freqCounter(st):
    l1=st.split(" ")
    d={}
    for i in l1:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

text = "apple banana apple cherry banana apple"
print(freqCounter(text))
