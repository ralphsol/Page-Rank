from random import randint

def matrixMult(v, u, size):
  res = []
  for i in range(0, size):
    tmpSum = 0
    for j in range(0, size):
      tmpSum += (v[i][j]*u[j])
    res.append(tmpSum)
  return res

def endLoop(W, P, size) :
  Winit = W
  Wfin = []
  ##print W
  term1 = matrixMult(P, W, size)
  ##print term1
  for i in range(0, size):
    Wfin.append((r*term1[i]) + ((1-r)/float(size)))
  for i in range(0, size):
    if (round(Winit[i], 6) != round(Wfin[i], 6)):
      return False
  return True

size = int(raw_input("Enter the number of pages : "))
## size = 100
feedIn = []
for i in range(0, size):
  temp = []
  for j in range(0, size):
    temp.append(randint(0, 1))
  feedIn.append(temp)

##for i in feedIn:
##  print i

u = []
for i in range(0, size):
  u.append(1)

'''The very simple method'''
res1 = matrixMult(feedIn, u, size)
##print
##print res1

'''First Improvement'''
P = []
for i in feedIn:
  P.append(i)  
N = []
for j in range(0, size):
  tmpSum = 0
  for i in range(0, size):
    tmpSum += P[i][j]
  N.append(tmpSum)
##print
##print N
for i in range(0, size):
  for j in range(0, size):
    P[i][j] = float(P[i][j])/float(N[j])
##print
##for i in P:
##  print i
res2 = matrixMult(P, u, size)
##print
##print res2

'''A Final Improvement'''
r = float(0.85)
W = []
for i in range(0, size):
  W.append(1.0/float(size))
loops = 0
while(not endLoop(W, P, size)):
  loops += 1
  res4 = []
  ##print W
  term1 = matrixMult(P, W, size)
  ##print term1
  for i in range(0, size):
    res4.append((r*term1[i]) + ((1-r)/float(size)))
  W = res4
##  print i
##  print res4
for i in range(0, size):
  res4[i] = round(res4[i], 4)
##print "loops = " + str(loops)
##print res4

rankPair = []
for i in range(0, size):
  rankPair.append((res4[i], i + 1))
##print rankPair
rankPair.sort(reverse = True)
##print rankPair

rankVect = []
i = 0
while i != size :
  for j in range(0, size):
    if rankPair[j][1] == (i + 1):
      rankVect.append(j + 1)
  i += 1
print rankVect
