import argparse

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description=' Vigenere Cipher Decoder')

	parser.add_argument('-f', '--file', help='Vigenere Cipher text contained file that you want to decode.')
	parser.add_argument('-t', '--text', help="Vigenere Cipher text that you want to decode.")
	parser.add_argument('-k', '--key', help="The key to decode Vigenere Cipher", required=True)

	args = parser.parse_args()

	if (args.text and args.file):
		print("You can't specify File name (-f / --file) and Text (-t / --text) together")
		exit(0)

	elif not(args.text or args.file):
		print("Vigenere Cipher text is required! use (-f / --file) or (-t / --text) to specify Cipher text")
		exit(0)

	elif (args.text):
		lines = args.text

	elif (args.file):
		try:
			with open(args.file,'r') as file:
				lines = file.readlines()
		except:
			print("Can't open '%s'"%args.file)
			exit(0)

	cipher = ''
	for line in lines:
		line = line.replace(' ','')
		line = line.replace('\n','')
		line = line.replace('\t','')
		cipher += line
	del lines
	del line

	cipher_lst = []
	temp = ''
	for i in range (len(cipher)):
		if ( (i%len(args.key)==0) and i!=0 ):
			cipher_lst.append(temp)
			temp = ''
		temp += list(cipher).pop(i)
	cipher_lst.append(temp)
	del temp
	del cipher

	alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

	print("Clear text : ",end='')
	for part in cipher_lst:
		for i in range (len(part)):
			print( alp[alp.index(part[i]) - alp.index(args.key[i]) ] ,end='')

	del cipher_lst
