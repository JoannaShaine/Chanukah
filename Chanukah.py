def noc(specs):
    C = specs[0]
    D = specs[1]
    
    nC = D + ((D * (D + 1))/2)
    print('{0} {1}'.format(C, int(nC)))
n = int(input())
for i in range(n):
    Specs = [int(j) for j in input().split()]
    noc(Specs)
