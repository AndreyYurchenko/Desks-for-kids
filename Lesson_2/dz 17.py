
c = {

   'apple': ['malum', 'pomum', 'popula'],

   'fruit': ['baca', 'bacca', 'popum'],

   'punishment': ['malum', 'multa']

}
y ={}
for k,v in c.items():
    for r in v:
        y.setdefault(r, []).append(k)

print(y)
