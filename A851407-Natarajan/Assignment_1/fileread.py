from collections import Counter

with open("C:/Rajan/Python/wordsoccurrence/sample.txt","r") as f:
    content = f.read()
    splitContent = content.lower().split()
    #print(splitContent)
    c = Counter(splitContent)
    #print(c)
    #print('Max ',max(c.values()))
    print('Most common words ',c.most_common())
    print('The max count of Most common word :- ',max(c.values()))
    print('Most Common words is ')
    for kv in c.items():
        if kv[1] == max(c.values()):
           print(kv)
    #print([kv for kv in c.items() if kv[1] == max(c.values())])
