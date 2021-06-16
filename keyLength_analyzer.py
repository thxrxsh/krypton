import argparse

if __name__ == '__main__':
	
	parser = argparse.ArgumentParser(description="Key length analyzer")
	parser.add_argument('-f','--file',help="Name of the file that you want to analyze to get the key length",required=True)
	args = parser.parse_args()

	try:
		with open(args.file,'r') as file:
			lines = file.readlines()
			print(' Reading "%s" ...'%args.file)

	except:
		print(' Can\'t find "%s" !'%args.file)
		exit(" Exiting ...")

	space_rep_seq = {}
	count = 0
	data = ''

	for line in lines:
		line = line.replace(' ','')
		line = line.replace('\n','')
		line = line.replace('\t','')
		data += line

	del lines

	print (' Analyzing the data from "%s"  ...' %args.file)
	for length in range (3,6):

		for i in range (len(data)-length+1):
			temp_1 = data[i:i+length]

			for j in range (i+1,len(data)-length+1):
				temp_2 = data[j:j+length]
				if (temp_1 == temp_2):
					space = j - i

					for x in range (1,space):
						if (space % x == 0) and (space//x < 20) :
							count += 1
							if ((space//x) in space_rep_seq.keys()):
								space_rep_seq[(space//x)] += 1
							else:
								space_rep_seq[(space//x)] = 1

	if (count == 0):
		print (" There are 0 repeated sequences founded :(" )
		exit("Exiting ...")

	else:
		print(" There are %d repeated sequences founded :) "%count)
		space_rep_seq = sorted(space_rep_seq.items(), key= lambda x: x[1], reverse=True)									
		print("\n    Key length\t\tChance\n  "+'-'*31)
		for (k,v) in space_rep_seq:

			print("\t%2d\t=\t%5.2f " % (k, float(v)*100/float(count)) + '%' )
