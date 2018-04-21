def NOT(a,x): #NOT operator
    result = a
    new=[]
    for row in result:
        if row[x] == 0:
            new.append(1)
               
        else:
           new.append(0)
    return new
def AND(a): #And operator
    result =[]
    for row in a:
    
        if row[0] == row[1]:
            result.append(row[0])
        else:
            result.append(0)
    
    return result

def OR(a): #Or operator
    result = []
    for row in a:
        if row[0] + row[1]  == 0:
            result.append(0)
        else:
            result.append(1)
    return result

def truthtable (n):#generates a table of n propositions
      if n < 1:
        return [[]]
      subtable = truthtable(n-1)
      return [ row + [v] for row in subtable for v in [0,1] ]

def JOIN(a,b):# puts together 2 propositions to be passed to operation
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
def QA(a): #[-p ^ (p v q)] -> q
    print "the predicates p and q table"
    print a
    print "Funtion: [-p ^ (p v q)] -> q"
    print "notp"
    notp = NOT(a,0)
    print notp
    print "p OR q"
    pORq = OR(a)
    print pORq  
    print "b = [-p ^ (p v q)]"
    b = AND(JOIN(notp, pORq))
    print b
    q= GETP(a,1)
    print "q"
    print q
    print "sol = b implies q = [-p ^ (p v q)] -> q"
    print IMP(JOIN(b,q))

def QB(a):
    #r ^ ((p -> -r) ^ (-p -> -r))
    p = GETP(a,0)
    r= GETP(a,1)
    print "predicates p and r"
    print p
    print r
    notr= NOT(a,1)
    notp=NOT(a,0)
    print "notr , notp"
    print notr
    print notp
    A = IMP(JOIN(p, notr))
    B =IMP(JOIN(notp,notr))
    print "A = IMP(JOIN(p, notr))"
    print A
    print "B =IMP(JOIN(notp,notr))"
    print B
    C=AND(JOIN(A,B))
    sol = AND(JOIN(r,C))
    print "C=AND(JOIN(A,B))"
    print C
    print" sol = AND(JOIN(r,C)) = r ^ ((p -> -r) ^ (-p -> -r))"
    print sol  




    
def MAIN():
    predicates=2
    ttable= truthtable(predicates)
    QA(ttable)
    QB(ttable)
   
MAIN()

