a = input('Please enter the number of students: ')
try:
    a = int(a)  #number of students
except:
    print ('Enter a number, you FOOL!')
b = input('Please enter the scores (separate them by a single space): ')
raw_score = b.split(' ')    # all scores
try:
    scores = [int(s) for s in raw_score]  #convert to integers
except:
    print ('Enter numbers, you FOOL!!')
if len(scores) != a:
    print ('Enter enough scores, you FOOL!')

best = 1    # a flag to indicate all pass
min_best = 100  # store the min pass score 
worst = 1   # a floag to indicate no one pass
max_worst = 0   # store the max failed score
for i in scores:    # scan all scores 
    if i < 60:
        best = 0    # if one failed score, the best set to 0
        if i > max_worst:
            max_worst = i   # find the max failed score
    if i >= 60:     
        worst = 0   #if existing pass score, the worst set to 0
        if i < min_best:
            min_best = i
scorestr = ''
for s in sorted(scores):    # sort scores and print
    scorestr += str(s)
    scorestr += ' '

print(scorestr[:len(scorestr)-1])
    
if best:
    print ('best case')
else:
    print (max_worst)
if worst:
    print ('worst case')
else:
    print (min_best)

