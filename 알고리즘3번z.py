import sys
from itertools import permutations
sys.stdin=open("input.txt","rt")
# 1~100의 카드 N장 중복가능 3장 뽑기 3장 덧셈 경우의수 기록 기록값중 k번째로 큰수 출력 

n,k = map(int,input().split()) # n = 10 k = 3
a = list(map(int,input().split())) # 기록된 카드들 의 값
d = []
cex = list(permutations(a,3))
for x,y,z in cex:
    _plus=x+y+z
    d.append(_plus)

res=set(d)
res1=sorted(res)
res2=list(reversed(res1))
print(res2[2])