def distance(pA,pB):
    return ((pA[0]-pB[0])**2 + (pA[1] - pB[1])**2)**(1/2)
import itertools
import warnings
warnings.filterwarnings("ignore")
def direction(p1,p2):
    """calculate the direction of p1 to p2"""
    p = [p1[0]-p2[0],p1[1]-p2[1]]
    return (p[0]//abs(gcd(p[0],p[1])),p[1]//abs(gcd(p[0],p[1])))
from fractions import gcd
width = 3
height = 2
r = 4
A = [1,1]
B = [2,1]

B_mirror_x = list(set([2*n*width + m*B[0] for n in range(-r//width-1, r//width+2) for m in [-1,1]]))
B_mirror_y = list(set([2*n*height + m*B[1] for n in range(-r//height-1, r//height+2) for m in [-1,1]]))
allpossibleB = [(x,y) for x in B_mirror_x for y in B_mirror_y]
validB = []
for item in allpossibleB:
    if distance(item,A) < 4:
        validB.append(item)
B_mirrors=validB
B_direction_distances = [[direction(v,A),distance(v,A)] for v in B_mirrors]
B_direction_distances.sort()
B_unique_mirrors = [list(grp)[0] for k,grp in itertools.groupby(B_direction_distances,lambda g:g[0])]
print(B_unique_mirrors)
A_mirror_x = list(set([2*n*width + m*A[0] for n in range(-r//width-1, r//width+2) for m in [-1,1]]))
A_mirror_y = list(set([2*n*height + m*A[1] for n in range(-r//height-1, r//height+2) for m in [-1,1]]))
allpossibleA = [(x,y) for x in A_mirror_x for y in A_mirror_y]
validA = []
for item in allpossibleA:
    if distance(item,A) < 4:
        validA.append(item)
A_mirrors=validA
A_direction_distances = [[direction(v,A),distance(v,A)] for v in A_mirrors]
A_direction_distances.sort()
A_unique_mirrors = [list(grp)[0] for k,grp in itertools.groupby(A_direction_distances,lambda g:g[0])]
print(A_unique_mirrors)

