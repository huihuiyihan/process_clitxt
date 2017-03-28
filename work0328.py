# -*- coding: UTF-8 -*- 
w1 = open('pinyin.txt')
w2 = open('pinyin_without.txt', 'a')
w3 = open('pinyin_with.txt', 'a')
w4 = open('asd.txt','a')
for line in w1:
	if "(" in line or "（"  in line:
		w3.write(line)
		# if 'B' in line.split('\t')[0]:
		# 	tempdata=line.split('\t')[0][:-3]+'\t'+line.split('\t')[1][:-2]+'\n'
		# 	w4.write(tempdata)
	else:
		w2.write(line)