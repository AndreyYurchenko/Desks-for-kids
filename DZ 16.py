y = {}
x = ('Abraham Lincoln ; February 12, 1809 – April 15, 1865) was an American statesman and lawyer who served as '
     'the 16th president of the United States from 1861 until his assassination in 1865. Lincoln '
     'led the nation through the American Civil War, the countrys greatest moral, cultural, constitutional, and political crisis. He succeeded in preserving the Union, abolishing slavery, bolstering the federal government, and modernizing the U.S. economy')
for word in x.split():
    y[word] = y.get(word, 0) + 1


max = max(y.values())
for k, v in sorted(y.items()):
    if v == max:
        print(k)
        break