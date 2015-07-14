__author__ = 'Ryan'

def removeDupes (list):
    seen = []
    for term in list:
        if term not in seen:
            seen.append(term)
    return seen

print(removeDupes([1,2,3,4,2,3,4,5,6,6,8,9,9]))

def combineLists(x, y):
    retList = []
    while len(x) and len(y):
        if x[0] <= y[0]:
            retList.append(x.pop(0))
        else:
            retList.append(y.pop(0))
    return retList

print(combineLists([1,1,2,3,6,7,9], [4,5,7,9,9]))

def cubes():
    summs = [i**3 + j**3 for i in range(25)for j in range(i,25)]
    summs = [k if summs.count(k)>1 else 0 for k in summs]
    return summs

cubes()

def rotCheck(a1, a2):
    for x in xrange(len(a1)):
        if a1 == a2:return True
        a1.append(a1.pop(0))
    return False

print (rotCheck([1,2,3,4,5], [2,3,4,5,1]))

def filePract(filePath):
    file = open(filePath,'r')
    players = file.readlines()
    print players
    for player in players:
        players[players.index(player)] = player.split(' ')
    print ('Players:     DateOB:')
    for player in players:
        print ' '+ player[0],
        print '\t  ' + player[1].strip('\n')

filePract('data.txt')
