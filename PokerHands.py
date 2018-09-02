import re
def score(hand):
    hand.sort()
    sets = []
    if 10 in hand and 11 in hand and 12 in hand and 13 in hand and 14 in hand and hand[0][-1]==hand[1][-1]==hand[2][-1]==hand[3][-1]==hand[4][-1]:
        sets.append([10,0])

    if hand[0][-1]==hand[1][-1]==hand[2][-1]==hand[3][-1]==hand[4][-1]:
        bool = True
        for i in range(1,len(hand)):
            if hand[i][0]-1!=hand[i-1][0]:
                bool = False
                break
        if bool==True:
            sets.append([9,hand[-1][0]])

    if hand[0][0]==hand[3][0] or hand[1][0]==hand[4][0]:
        sets.append([8,hand[2]])

    if hand[0][0]==hand[1][0] and hand[2][0]==hand[4][0] or hand[3][0]==hand[4][0] and hand[0][0]==hand[4][0]:
        if hand[2][0]==hand[4][0]:
            sets.append([7,hand[2][0],hand[0][0]])
        else:
            sets.append([7,hand[2][0],hand[4][0]])

    if hand[0][-1]==hand[1][-1]==hand[2][-1]==hand[3][-1]==hand[4][-1]:
        sets.append([6,0])

    bool = True
    for i in range(1,len(hand)):
        if hand[i][0]-1!=hand[i-1][0]:
            bool = False
            break
    if bool==True:
        sets.append([5,hand[-1][0]])

    if hand[0][0]==hand[2][0] or hand[1][0]==hand[3][0] or hand[2][0]==hand[4][0]:
        sets.append([4,hand[2][0]])

    pairs = 0
    for i in range(1,len(hand)):
        if hand[i-1][0]==hand[i][0]:
            pairs += 1

    if pairs==2:
        h = False
        for i in range(len(hand)-2,0,-1):
            if hand[i+1][0]==hand[i][0] and not h:
                hpair = hand[i][0]
                h = True

            if hand[i+1][0]==hand[i][0] and h:
                lpair = hand[i][0]

        sets.append([3,hpair,lpair])

    if pairs ==1:
        for i in range(1,len(hand)):
            if hand[i-1][0]==hand[i][0]:
                pair = hand[i][0]
        sets.append([2,pair])

    sets.append([1,hand[4][0]])
    return sets

def winCount(lines):
    wins = 0
    for i in lines:
        #print(i)
        p1=score(i[0:5])
        p2=score(i[5:len(i)+1])
        lenp1 = len(p1)
        lenp2 = len(p2)

        if lenp1>lenp2:
            p2 = p2 + [[0]]*(lenp1-lenp2)
        if lenp1<lenp2:
            p1 = p1 + [[0]]*(lenp2-lenp1)
        #print('')
        #print(p1)
        #print(p2)
        breaker = False
        for j in range(0,len(p1)):
            if breaker: break
            if p1[j][0]==p2[j][0]:
                lenp1 = len(p1)
                lenp2 = len(p2)
                if lenp1>lenp2:
                    p2 = p2 + [[0]]*(lenp1-lenp2)
                if lenp1<lenp2:
                    p1 = p1 + [[0]]*(lenp2-lenp1)

                for k in range(0,len(p1[j])):
                    if p1[j][k]>p2[j][k]:
                        wins +=1
                        #print("p1", p1[j])
                        breaker = True
                        break
                    elif p1[j][k]<p2[j][k]:
                        breaker = True
                        break

            elif p1[j][0]<p2[j][0]: break
            else:
                wins += 1
                #print("p1-2")
                break

    return wins

with open('Material/poker.txt') as f:
    rep = {'T':'10', 'J': '11', 'Q': '12', 'K': '13', 'A': '14','\n': ''}
    pattern = re.compile("|".join(rep.keys()))
    lines = [i for i in f.readlines()]
    lines = [pattern.sub(lambda m: rep[m.group(0)], i).split() for i in lines]
    #lines = [[i[j][0:-1],i[j][-1]] for i in lines for j in range(0,len(i))]
    for k in range(0,len(lines)):
        for j in range(0,len(lines[k])):
            lines[k][j]=[int(lines[k][j][0:-1]),lines[k][j][-1]]

    print(winCount(lines))
