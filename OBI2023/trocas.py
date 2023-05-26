Y = input()
Y = [int(x) for x in Y.split(" ")]

cima = input()
baixo = input()
cima = [int(x) for x in cima.split(" ")]
baixo = [int(x) for x in baixo.split(" ")]

for a in range(int(Y[1])):
	Y1 = input()
	Y1 = [int (x) for x in Y1.split(" ")]
	i = Y1[0]-1
	i2 = Y1[1]
	while i < (i2):
		res = cima[i]
		res2 = baixo[i]
		cima[i] = res2
		baixo[i] = res
		i += 1
	# print(cima)
	# print(baixo)
for i in cima:
	print(i, end=" ")