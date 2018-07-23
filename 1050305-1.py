a = input('Please enter the number of students: ')
try:
    a = int(a)
except:
    print ('Enter a number, you FOOL!')
b = input('Please enter the scores (separate them by a single space): ')
raw_score = b.split(' ')
try:
    scores = [float(s) for s in raw_score]
except:
    print ('Enter numbers, you FOOL!!')
if len(scores) != a:
    print ('Enter enough scores, you FOOL!')

best = 1
min_best = 100
worst = 1
max_worst = 0
for i in scores:
    if i < 60:
        best = 0
        if i > max_worst:
            max_worst = i
    if i >= 60:
        worst = 0
        if i < min_best:
            min_best = i
scorestr = ''
for s in sorted(scores):
    scorestr += str(s)
    scorestr += ' '

print(scorestr)
    
if best:
    print ('best case')
else:
    print (max_worst)
if worst:
    print ('worst case')
else:
    print (min_best)

