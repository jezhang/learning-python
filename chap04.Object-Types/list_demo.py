L = [123, 'spam', 1.23]
print(L.count(123))
print(L.index(1.23))

print(len(L))
print(L[0])

print(L[-1])
print(L[len(L) - 1])   
print(L[-1] == L[len(L) - 1])

L.append('NI')
print(L)

L.pop(2)
print(L)

print('=' * 50)
M = ['bb','aa','cc']
M.sort()
print(M)
M.reverse()
print(M)


M = [[1,2,3],
	[4,5,6],
	[7,8,9]]
print(M)
print(M[1])
print(M[1][2])

col2 = [row[1] for row in M]
print(col2)
print(M)

print([row[1] + 1 for row in M])
print([row[1] for row in M if row[1] % 2 == 0])

diag = [M[i][i] for i in [0,1,2]]
print(diag)

print('=' * 50)
doubles = [c * 2 for c in 'spam']
print(doubles)

G = (sum(row) for row in M)
print(next(G))
print(next(G))
print(next(G))

print(list(map(sum,M)))