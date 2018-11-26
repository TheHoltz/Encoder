#Encriptação de acordo com o valor na tabela ASCII

def encrypt(In):
	out = str();
	for i in In:
		out+=(ord(i.lower())-96)*'k'+'j'
	return(out)

def decrypt(In):
	out = str();
	In=In.split("j")
	for i in In:
		out+=chr(len(i)+96);
	return(out)

while(1):
	a = input("Insira string:")
	print(encrypt(a))
	a = input("Insira string:")
	print(decrypt(a))
