import random
import string

def encode(In):
    Hash = int(''.join(random.choices('0123456789',k=25)));
    random.seed(Hash);
    db = dict();
    for i in (string.ascii_lowercase+string.ascii_uppercase+
    string.punctuation+string.digits+string.whitespace):
        db[i] = ''.join(random.choices(string.hexdigits, k=2))
    out = str();
    for i in In:
        out+=db[i];
    return(out,Hash);


def search(db,In):
    for key,val in db.items():
        if val == In:
            return key

def decode(In, Hash):
    random.seed(Hash)
    db = dict();
    for i in (string.ascii_lowercase+string.ascii_uppercase+
    string.punctuation+string.digits+string.whitespace):
        db[i] = ''.join(random.choices(string.hexdigits, k=2))
    splitstr = lambda x, n: [x[i:i+n] for i in range(0, len(x), n)];
    In = splitstr(str(In),2);
    out = str();
    for i in In:
        if(i in db.values()):
            out+=search(db,i);
    return(out);
