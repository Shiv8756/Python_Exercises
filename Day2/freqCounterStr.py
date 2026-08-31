# def freqCounter(st):
#     l1=st.split(" ")
#     d={}
#     for i in l1:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     return d
#
# text = "apple banana apple cherry banana apple"
# print(freqCounter(text))

text = "apple banana apple cherry banana apple"
l1=text.split(" ")
d={}
for i in l1:
    d[i]=d.get(i,0) + 1

print(d)



