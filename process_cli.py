# -*- coding: UTF-8 -*- 
import json
# w=open('DATASTORE_EMR.json')
# neww=open(r'./newdata/DATASTORE_EMR.json','a')

# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[0]+','+temp[1]+','+temp[2]+','+temp[6]+','+temp[7]+'\n'
# 	neww.write(tempdata)


# w=open('FIN_COM_UNDRUGINFO.json')
# neww=open(r'./newdata/FIN_COM_UNDRUGINFO.json','a')

# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[23]+','+temp[43]+','+temp[46]+','+temp[47]+','+temp[7]+'\n'
# 	neww.write(tempdata)


# w=open('LIS_RESULT.json')
# neww=open(r'./newdata/LIS_RESULT.json','a')

# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[0]+','+temp[2]+','+temp[9]+','+temp[11]+','+temp[12]+','+temp[17]+','+temp[19]+','+temp[20]
# 	neww.write(tempdata)

# w=open('MET_IPM_EXECUNDRUG.json')
# neww=open(r'./newdata/MET_IPM_EXECUNDRUG.json','a')

# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[2]+','+temp[7]+','+temp[12]+','+temp[17]+','+temp[38]+','+temp[40]+','+temp[42]+','+temp[53]+'\n'
# 	neww.write(tempdata)


# w=open('MET_IPM_ORDER.json')
# neww=open(r'./newdata/MET_IPM_ORDER.json','a')

# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[0]+','+temp[15]+','+temp[25]+','+temp[32]+','+temp[39]+','+temp[42]+','+temp[45]+','+temp[49]+','+temp[51]+','+temp[61]+','+temp[75]+','+temp[76]+'\n'
# 	neww.write(tempdata)

# w=open('MET_IPM_EXECDRUG.json')
# neww=open(r'./newdata/MET_IPM_EXECDRUG.json','a')

# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[1]+','+temp[8]+','+temp[14]+','+temp[19]+','+temp[29]+','+temp[34]+','+temp[43]+','+temp[49]+','+temp[60]+','+temp[70]+'\n'
# 	neww.write(tempdata)



# w=open('LOG_EQU_BASEINFO.json')
# neww=open(r'./newdata/LOG_EQU_BASEINFO.json','a')

# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[8]+','+temp[12]+','+temp[13]+','+temp[15]+','+temp[24]+'\n'
# 	neww.write(tempdata)

# w=open('LOG_EQU_COMPANY.json')
# neww=open(r'./newdata/LOG_EQU_COMPANY.json','a')

# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[2]+'\n'
# 	neww.write(tempdata)


# w=open('PHA_COM_BASEINFO.json')
# neww=open(r'./newdata/PHA_COM_BASEINFO.json','a')

# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[4]+','+temp[11]+','+temp[21]+','+temp[38]+','+temp[40]+','+temp[52]+','+temp[79]+','+temp[86]+'\n'
# 	neww.write(tempdata)


# w=open('MET_CAS_OPERATIONDETAIL.json')
# neww=open(r'./newdata/MET_CAS_OPERATIONDETAIL.json','a')

# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[0]+','+temp[2]+'\n'
# 	neww.write(tempdata)


# w=open('MET_CAS_DIAGNOSE.json')
# neww=open(r'./newdata/MET_CAS_DIAGNOSE.json','a')

# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[1]+','+temp[19]+'\n'
# 	neww.write(tempdata)


# w=open('KA03.json')
# neww=open(r'./newdata/KA03.json','a')

# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[19]+','+temp[31]+'\n'
# 	neww.write(tempdata)

# w=open('KA04.json')
# neww=open(r'./newdata/KA04.json','a')

# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[14]+','+temp[21]+','+temp[23]+'\n'
# 	neww.write(tempdata)


# w=open('KA02.json')
# neww=open(r'./newdata/KA02.json','a')

# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[27]+','+temp[37]+','+temp[43]+','+temp[48]+','+temp[54]+'\n'
# 	neww.write(tempdata)



# w=open('IPB_NUR_ORDER_PRINT.json')
# neww=open(r'./newdata/IPB_NUR_ORDER_PRINT.json','a')

# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[0]+','+temp[1]+','+temp[2]+','+temp[6]+'\n'
# 	neww.write(tempdata)


# w=open('FIN_IPR_INMAININFO.json')
# neww=open(r'./newdata/FIN_IPR_INMAININFO.json','a')

# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[32]+','+temp[36]+','+temp[69]+','+temp[70]+','+temp[74]+'\n'
# 	neww.write(tempdata)



# w=open('EMR_COURSERECORD_QCDATA.json')
# neww=open(r'./newdata/EMR_COURSERECORD_QCDATA.json','a')

# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[1]+','+temp[3]+','+temp[11]+','+temp[12]+'\n'
# 	neww.write(tempdata)



# w=open('LIS_TEST_REG.json')
# neww=open(r'./newdata/LIS_TEST_REG.json','a')

# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[0]+','+temp[2]+','+temp[3]+','+temp[8]+','+temp[10]+','+temp[11]+','+temp[18]+'\n'
# 	neww.write(tempdata)




# w=open('FIN_OPR_REGISTER.json')
# neww=open(r'./newdata/FIN_OPR_REGISTER.json','a')
# 未做处理，不知道哪个有用



# w=open('FIN_OPB_FEEDETAIL.json')
# neww=open(r'./newdata/FIN_OPB_FEEDETAIL.json','a')

# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[9]+','+temp[33]+','+temp[46]+','+temp[64]+','+temp[70]+'\n'
# 	neww.write(tempdata)




# w=open('FIN_IPB_MEDICINELIST.json')
# neww=open(r'./newdata/FIN_IPB_MEDICINELIST.json','a')

# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[0]+','+temp[4]+','+temp[8]+','+temp[10]+','+temp[23]+'\n'
# 	neww.write(tempdata)




# w=open('FIN_IPB_ITEMLIST.json')
# neww=open(r'./newdata/FIN_IPB_ITEMLIST.json','a')

# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[0]+','+temp[9]+','+temp[33]+'\n'
# 	neww.write(tempdata)




# w=open('SI_YB_DRUG_ZG.json')
# neww=open(r'./newdata/SI_YB_DRUG_ZG111.json','a')
# for line in w:
# 	tempdata=''
# 	if line[0]=='}':
# 		tempdata+=line
# 	else:
# 		tempdata+=line[:-1]
# 	neww.write(tempdata)

# w=open(r'./newdata/SI_YB_DRUG_ZG111.json')
# neww=open(r'./newdata/SI_YB_DRUG_ZG.json','a')
# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[0]+','+temp[1]+'\n'
# 	neww.write(tempdata)





# w=open('KXNH_DIAGNOSIS.json')
# neww=open(r'./newdata/KXNH_DIAGNOSIS111.json','a')
# for line in w:
# 	tempdata=''
# 	if line[0]=='}':
# 		tempdata+=line
# 	else:
# 		tempdata+=line[:-1]
# 	neww.write(tempdata)


# w=open(r'./newdata/KXNH_DIAGNOSIS111.json')
# neww=open(r'./newdata/KXNH_DIAGNOSIS.json','a')
# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[0]+','+temp[1]+'\n'
# 	neww.write(tempdata)





# w=open('SI_YB_DISEASE_ZG.json')
# neww=open(r'./newdata/SI_YB_DISEASE_ZG111.json','a')
# for line in w:
# 	tempdata=''
# 	if line[0]=='}':
# 		tempdata+=line
# 	else:
# 		tempdata+=line[:-1]
# 	neww.write(tempdata)

# w=open(r'./newdata/SI_YB_DISEASE_ZG111.json')
# neww=open(r'./newdata/SI_YB_DISEASE_ZG.json','a')
# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[0]+','+temp[1]+'\n'
# 	neww.write(tempdata)


# w=open('MET_HQMS_CONTRAST_ICD.json')
# neww=open(r'./newdata/MET_HQMS_CONTRAST_ICD111.json','a')
# for line in w:
# 	tempdata=''
# 	if line[0]=='}':
# 		tempdata+=line
# 	else:
# 		tempdata+=line[:-1]
# 	neww.write(tempdata)


# w=open(r'./newdata/MET_HQMS_CONTRAST_ICD111.json')
# neww=open(r'./newdata/MET_HQMS_CONTRAST_ICD.json','a')
# for line in w:
# 	temp=line[1 :].split(',')
# 	tempdata=temp[3]+','+temp[4][:-1]+'\n'
# 	neww.write(tempdata)



# w=open('EMR_COURSERECORDTEXT.json')
# neww=open(r'./newdata/EMR_COURSERECORDTEXT111.json','a')
# for line in w:
# 	tempdata=''
# 	if line[0]=='}':
# 		tempdata+=line
# 	else:
# 		tempdata+=line[:-1]
# 	neww.write(tempdata)

w=open(r'./newdata/EMR_COURSERECORDTEXT111.json')
neww=open(r'./newdata/EMR_COURSERECORDTEXT.json','a')
for line in w:
	temp=line[1 :].split(',')
	tempdata=','.join(temp[:-2])+'\n'
	neww.write(tempdata)


