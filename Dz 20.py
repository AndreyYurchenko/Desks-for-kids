v = [[34587,'Learning Python','Mark Lutz',4,40.95],
         [98762,'Programming Python','Mark Lutz',5,56.80],
         [77226,'Head First Python','Paul Barry',3,32.95],
         [88112,'Einführung in Python3','Bernd Klein',3,24.99],
        ]
# y = []
# for i in v:
#     if i[-1]*i[-2] < 100:
#        y.append((i[0],i[-1]*i[-2]+10))
#     else:
#        y.append((i[0],i[-1]*i[-2]))
#
# print(y)
#print([(i[0], i[-1] * i[-2]) if i [-1] * i [-2] > 100 else (i[0], i[-1] * i[-2]+10) for i in v])

print(list(map(lambda i: [i[0], i[-1] * i[-2]] if i[-1] * i[-2] > 100 else (i[0],i[-1] * i[-2] + 10), v)))
