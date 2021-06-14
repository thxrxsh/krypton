import argparse

if __name__ == '__main__':

	# def getKeyFromValue(dic,val):
	#  	return [k for (k,v) in dic.items() if v == val][0]


	parser = argparse.ArgumentParser(description='Frequency Analyzer')
	parser.add_argument('-f','--file',help='Name of the file that you want to analyze',required=True)
	parser.add_argument('-g','--group_size',type=int,help="Number of letters that you want to group. Set this to 1, if you want to analyze letter by letter",required=True)
	args = parser.parse_args()

	try:
		with open (args.file) as file:
			lines = file.readlines()

	except:
		print ("Can't find '%s'"%args.file)
		exit(0)

	data =''
	for line in lines:
		line = line.replace(' ','')
		line = line.replace('\t','')
		line = line.replace('\n','')

		data += line

	char_table = {}
	tot_char = 0

	for x in range (len(data)-(args.group_size-1)):
		charactor = data[x:x+args.group_size]

		tot_char += 1
	
		if charactor in char_table.keys():
			char_table[charactor] += 1

		else:
			char_table[charactor] = 1

	char_table = sorted(char_table.items(), key=lambda x:x[1], reverse=True)

        for (letter,count) in char_table:
                print(" %s = %d"%(letter, count))


	print("\nTotal number of the charactors : %s"%tot_char)






