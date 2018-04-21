#[p -> (q -> r)] -> [(p -> q) -> r]


def IMP(a): # imlies method
    result =[]
    for row in a:
        if row[0] == row[1]:
                result.append(1)
        
        elif row[0] > row[1]:
                result.append(0)
        elif row[0] < row[1]:
                result.append(1)
    return result

def JOIN(a,b): # puts together 2 propositions to be passed to operation
    jn=[]
    i=0
    for n in a:
        jn.append([a[i],b[i]])
        i=i+1    
    return jn

def GETP(a,x):# extracts a column of p from a table of propositions p,q,r
    result =[]
    for row in a:
        result.append(row[x])
    return result

def truthtable (n):#generates a table of n propositions
      if n < 1:
        return [[]]
      subtable = truthtable(n-1)
      return [ row + [v] for row in subtable for v in [0,1] ]


def Q3(a):
    p = GETP(a,0)
    q = GETP(a,1)
    r = GETP(a,2)
    A = IMP(JOIN(q,r))
    A2 = IMP(JOIN(p,A))
    print  "(q -> r)"
    print  A
    print  "[p -> (q -> r)]"
    print A2
    B = IMP(JOIN(p,q))
    B2 = IMP(JOIN(B,r))
    print "(p -> q)"
    print B
    print "[(p -> q) -> r]"
    print B2
    sol = IMP(JOIN(A2,B2))
    print "[p -> (q -> r)] -> [(p -> q) -> r] =sol"
    print sol
def MAIN():
    print "[p -> (q -> r)] -> [(p -> q) -> r]"
    prop =3
    ttable = truthtable(prop)
    print ttable
    print ("p,q,r")
    Q3(ttable)

MAIN()
