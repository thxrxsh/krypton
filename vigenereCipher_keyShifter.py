import argparse

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description="Vigenere key shifter")
	parser.add_argument('-f','--file',help="Name of the file that you want to shift keys from.",required=True)
	parser.add_argument('-g', '--group_size',type=int, help="Number of the characters that you want to group together. You need to specify this number according to the character length of the encryption key", required=True)
	parser.add_argument('-s', '--shift',type=int, help= "Index number of the key that you want to shift from a each group. The index starts from 0.",required=True)

	args = parser.parse_args()

	try:
		with open(args.file,'r') as file:
			lines = file.readlines()
	except:
		print("Can't find '%s'"%args.file)
		exit(0)

	if not(args.shift < args.group_size):
		print("Shift number (-s / --shift) must be less than Group Size (-g / --group_size)")
		exit(0)


	data = ''
	for line in lines:
		line = line.replace(' ','')
		line = line.replace('\n','')
		line = line.replace('\t','')
		data += line
	del lines


	output = ''
	for i in range (args.shift,len(data),args.group_size):
		output += data[i]

	print(output)