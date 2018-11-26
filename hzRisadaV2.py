#Referencia: https://pt.wikipedia.org/wiki/Alfabeto_portugu%C3%AAs

db = {
"a":1,
"e":2,
"o":3,
"s":4,
"r":5,
"i":6,
"n":7,
"d":8,
"m":9,
"u":10,
"t":11,
"c":12,
"l":13,
"p":14,
"v":15,
"g":16,
"h":17,
"q":18,
"b":19,
"f":20,
"z":21,
"j":22,
"x":23,
"k":24,
"w":25,
"y":26,
" ":0,
}

def encrypt(string):
    out = str();
    for i in string:
        if(i.lower() in db):
            out+=(db[i]*'k'+'j');
    return(out);


def decrypt(In):
    In = In.split("j")
    out = str();
    for i in In:
	    for key,val in db.items():
	        if val == len(i):
	            out+=key;
    return(out);


while(1):
	a = input("Insira string para encriptar:")
	print(encrypt(a))
	a = input("Insira string para desencriptar:")
	print(decrypt(a))
