#(p -> q) -> (r -> s) and (p -> r) -> (q -> s) equivalent?

def truthtable (n):#generates a table of n propositions:list comprehensions
      if n < 1:
        return [[]]
      subtable = truthtable(n-1)
      return [ row + [v] for row in subtable for v in [0,1] ]
def GETP(a,x): # extracts a column of p from a table of propositions p,q,r
    result =[]
    for row in a:
        result.append(row[x])
    return result

def JOIN(a,b):# puts together 2 propositions to be passed to operation
    jn=[]
    i=0
    for n in a:
        jn.append([a[i],b[i]])
        i=i+1    
    return jn

def IMP(a):# imlies method
    result =[]
    for row in a:
        if row[0] == row[1]:
                result.append(1)
        
        elif row[0] > row[1]:
                result.append(0)
        elif row[0] < row[1]:
                result.append(1)
    return result

def COMP(a):#method to compare 2 propositions
    answer = True
    for row in a:
        if row[0] != row[1]:
            answer = False
    return answer

def Q4(a):
    p = GETP(a,0)
    q = GETP(a,1)
    r = GETP(a,2)
    s = GETP(a,3)
    
    A1= IMP(JOIN(p,q))
    print "A1= (p -> q"
    print A1
    A2 = IMP(JOIN(r,s))
    print "A2 = (r -> s)"
    print A2
    A= IMP(JOIN(A1,A2))
    print "A = (p -> q) -> (r -> s) = A1->A2"
    print A

    B1= IMP(JOIN(p,r))
    print "B1= (p -> q"
    print B1
    B2 = IMP(JOIN(q,s))
    print "B2 = (r -> s)"
    print B2
    B= IMP(JOIN(B1,B2))
    print "B = (p -> r) -> (q -> s) = B1->B2"
    print B

    
    print "A=B, [(p -> q) -> (r -> s)] is equal to [(p -> r) -> (q -> s)]"
    print COMP(JOIN(A,B))


def MAIN():
    print "(p -> q) -> (r -> s) and (p -> r) -> (q -> s) equivalent?"
    
    prop =4
    ttable = truthtable(prop)
    print ttable
    Q4(ttable)


    
MAIN()
