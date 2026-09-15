words = {"a": "banana", "b": "kiwi", "c": "strawberry", "d": "fig"}

d=dict(sorted(words.items(),key=lambda k:len(k[1])))
print(d)