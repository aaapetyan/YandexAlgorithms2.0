# https://contest.yandex.ru/contest/28970/problems/A/

N = int(input())
colors = dict()
for i in range(N):
    di, ai = map(int, input().split())
    if di not in colors:
        colors[di] = 0
    colors[di] += ai
for d, a in sorted(colors.items()):
    print(d, a)


# https://contest.yandex.ru/contest/28970/problems/B/

f = open('input.txt','r')
candidates = dict()
for line in f.readlines():
    name, votes = line.split()
    if name not in candidates:
        candidates[name] = 0
    candidates[name] += int(votes)
for i, j in sorted(candidates.items()):
    print(i, j)


# https://contest.yandex.ru/contest/28970/problems/C/

mydict = dict()
with open('input.txt','r') as f:
    for line in f.readlines():
        words = line.split()
        for word in words:
            if word not in mydict:
                mydict[word] = 0
            mydict[word] += 1
list_to_sort = []
for i, j in mydict.items():
    list_to_sort.append((i,j))
sort_by_word = sorted(list_to_sort, key = lambda words: words[0])
sort_by_count = sorted(sort_by_word, key = lambda words: words[1],reverse=True)
for words in sort_by_count:
    print(words[0])

# https://contest.yandex.ru/contest/28970/problems/D/

all_votes = []
sum_votes = 0
remaining_seats = 450

i = 0
with open('input.txt','r') as fin:
    for line in fin.readlines():
        party, votes = line.rsplit(' ',1)
        all_votes.append([i, party, int(votes)])
        sum_votes += int(votes)
        i += 1

for i in range(len(all_votes)):
    temp = all_votes[i][2] / sum_votes * 450.0
    all_votes[i][2] = [int(temp),temp-int(temp)]
    remaining_seats -= int(temp)
    
all_votes = sorted(all_votes, key = lambda votes: votes[2][1], reverse = True)

i = 0

while remaining_seats > 0:
    all_votes[i][2][0] += 1
    remaining_seats -= 1
    i += 1
    if i == len(all_votes):
        i = 0
        
all_votes = sorted(all_votes, key = lambda votes: votes[0])        

print_line = ''

for i in range(len(all_votes)):
    print_line += all_votes[i][1] + ' ' + str(all_votes[i][2][0]) + '\n'
    
print(print_line)
