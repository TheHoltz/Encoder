import random
import string

def encode(In):
    Hash = int(''.join(random.choices('0123456789',k=25)));
    random.seed(Hash);
    db = dict();
    for i in (string.ascii_lowercase+string.ascii_uppercase+
    string.punctuation+string.digits+string.whitespace):
        db[i] = ''.join(random.choices(string.hexdigits, k=3))
    out = str();
    for i in In:
        out+=db[i];
    return(out,Hash);

def decode(In, Hash):
    random.seed(Hash)
    db = dict();
    for i in (string.ascii_lowercase+string.ascii_uppercase+
    string.punctuation+string.digits+string.whitespace):
        db[i] = ''.join(random.choices(string.hexdigits, k=3))
    splitstr = lambda x, n: [x[i:i+n] for i in range(0, len(x), n)];
    In = splitstr(str(In),3);
    out = str();
    for i in In:
        if i in db.values():
            for key,val in db.items():
                if val == i:
                    out+=key;
    return(out);

while True:
    print("\n┬ ┬┌─┐╔═╗┌┐┌┌─┐┬─┐┬ ┬┌─┐┌┬┐\n├─┤┌─┘║╣ ││││  ├┬┘└┬┘├─┘ │\n┴ ┴└─┘╚═╝┘└┘└─┘┴└─ ┴ ┴   ┴")
    In = str(input("\nInsira uma string para codificar:"))
    In = encode(In)
    print("\nKey:\t",In[0]);
    print("Hash:\t",In[1]);
    Out = str(input("\nInsira uma key para decodificar:"))
    Hash = int(input("Insira um hash valido:"))
    print("")
    print("Entrada: %.20s..."%Out)
    print("Hash:\t %.20s..."%str(Hash))
    print("Saida:\t "+decode(Out,Hash))
