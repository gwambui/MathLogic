#Predicate 1: Even numbers


			
#2 Predicates: All x greater than 5 and some y Even
def DUAL(d,e):
    test = True
    for num in d:
        if num < 5:
            test= False
            break
        
    if test == True:
        test = False
        for num1 in e:
            x = num1 % 2
            if x == 0:
                test = True
                break
        return test
            
                
    else:
        return test


#main method			
def Main():
		dal = [1,2,3,6,9,7]#random, numbers
		eve = [6,8,18,12]#even numbers
		test= [11,41,31]  #all > 5 none even
		test1 = [1,4,3] #all < than 5 some even

		z=DUAL(eve, dal)
		y= DUAL(test,test)
		x = DUAL(test1,test1)
		
		print ("All values in domtest are greater than 5 and some values in domall are even ")
		print ("The even domain eve")
		print (eve)
		print ("the random domain dal")
		print (dal)
		print ("eve, dal: All x greater than 5 and some y Even")
		print (z)
		print (" test,test:All x greater than 5 and some y Even")
		print (y)
		print ("test1,test1: All x greater than 5 and some y Even")
		print (x)

		
Main()
