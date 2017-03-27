w1=open('1_1.txt')
w2=open('1_2.txt')
ww=open('KA02.txt','a')
temp1 = []
temp2 = []
for line in w1:

	temp1.append(line)
for line in w2:

	temp2.append(line)
for i in range(len(temp1)):
	temp = []
	temp = temp1[i].split('"')
	tempdata = ''
	tempdata += temp[-2] + '\t'
	temp = []
	temp = temp2[i].split('"')
	tempdata += temp[-2] + '\n'
	ww.write(tempdata)