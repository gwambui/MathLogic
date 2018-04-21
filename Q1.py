#Predicate 1: Even numbers
# universal quantifier test for even Ax P(x)

def ALL(d):
    test = True
    for num in d:
        if num % 2 > 0:
            test = False
            break

    return test
        
#existential quantifier	test for even Ex P(x)		
def SOME(d):
    test = False
    for num in d:
            if num % 2 == 0:
                    test = True
    return test
			
#2 Predicates: all greater than 5 and all even AxAy Q(x; y).
def DUAL(d,e):
        test = True
        for num in d:
            for num1 in e:
                if num > 5:
                    if num1 % 2 > 0:
                        test = False
                        
                else:
                    test = False
        return test
					
			
				
			

#main method			
def Main():
		domall = [1,7,2,5]
		domeve = [2,14,6,8]
		domtest = [6,8,7,8]
		x=ALL(domeve)
		y=ALL(domall)
		s=SOME(domall)
		z=DUAL(domtest, domtest)
		print ( "X The domain domeve has only even numbers" )
		print (x)
		print ( "S The domain domall has some even numbers" )
		print (s)
		print ("Y The domain domall has only even numbers " )
		print (y)
		print ("Z All values in domtest are greater than 5 and all in domtest are even ")
		print (z)

		
Main()
