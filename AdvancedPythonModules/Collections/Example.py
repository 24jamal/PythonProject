from collections import Counter

mylist = ["a","a","b","c","s","a"]
mycounter = Counter(mylist)
print(mycounter)


mycounter2 = Counter("Hello")
print(mycounter2)

sentence = "How are you?"

mycountersplit = Counter(sentence.lower().split())

print(mycountersplit)

print(mycounter.most_common(2))