from fractions import Fraction 

# Reading Data
def read_fractions(string):
    if '/' in string:
        parts = string.split('/')
        numerator = int(parts[0])
        denominator = int(parts[1])
        return numerator/denominator
    else:
        return int(string) # Treat the input as an integer with denominator 1

j1 = input(" j1 = ")    
j1 = read_fractions(j1)
j1 = Fraction(j1).limit_denominator()     # Conversion de j1 sous forme a/b


j2 = input(" j2 = ")    
j2 = read_fractions(j2)
j2 = Fraction(j2).limit_denominator()     # Conversion de j2 sous forme a/b



# We will start from the maximum value of m which is j till the minimum value which is -m

j = j1 + j2                             # j < = j1 + j2
j = Fraction(j).limit_denominator()     # Conversion de j sous forme a/b

m = j         # - j < = m < = j         
m1 = j1       # m1 < = j1   
m2 = j2       # m2 < = j2   



print("="*135)  # Just a break line seperates results 

# Les conditons initiales:
CP = [1]
CD = [1]
CF = [1]


# We are interested in the value of CF[i] = jm(i) x jm(i-1) x .... jm(0)
i = 0 
while i < 2*j : # gs = (2j+1) 

    i = i + 1  

    jm = j*(j+1) - m*(m-1)      # m{-j,-j+1,-j+2,...,0,...,j-1,j-2,j}
    m = m - 1                   # Because of J-  
    CF.append(CF[i-1]*jm)       # Add the calculated value of jm(i) = jm(i) x jm(i-1) x .... jm(0) to CF[]



# We are interested in the value of CP[i] = jm1(i) x jm1(i-1) x .... jm1(0)
i = 0 
while i < 2*j1 : # gs = (2j+1) 

    i = i + 1  
    
    jm1 = j1*(j1+1) - m1*(m1-1)   # m{-j,-j+1,-j+2,...,0,...,j-1,j-2,j}
    m1 = m1 - 1                   # Because of J1-
    CP.append(CP[i-1]*jm1)        # Add the calculated value of jm(i) = jm(i) x jm(i-1) x .... jm(0) to CP[]


# We are interested in the value of  CD[i] = jm2(i) x jm2(i-1) x .... jm2(0)
i = 0 
while i < 2*j2 : # gs = (2j+1) 

    i = i + 1  

    jm2 = j2*(j2+1) - m2*(m2-1)   # m{-j,-j+1,-j+2,...,0,...,j-1,j-2,j}
    m2 = m2 - 1                   # Because of J2-  
    CD.append(CD[i-1]*jm2)        # Add the calculated value of jm(i) = jm(i) x jm(i-1) x .... jm(0) to CD[]


m = j # Réinitialisation de la valeur de m  

"""
*** First state after state |J, M> is |J, M - 1>, so i starts with 1.

*** The first state |J, M> and the last state |J, -M> , so the number of states we have is 2j +1 
"""


f3 = " " # Ex : <2,-1|2,-1> =   + 1/2 + 1/2 = 1         Normalization Condition is verified 
i = 0 
while i <2*j+1: 
    

    f1 = " | {} , {} > = ".format(j, m-i )   # Partie 1 de |J,M-i>

    """
      To go through all the possibilities where -j1 ≤ m1 ≤ j1 and -j2 ≤ m2 ≤ j2, we need to start with 
      the "UP DOWN" simultaneously. Therefore, if m1 = j1 ⇒ m2 = -j2, we notice that m1-- and m2++.
    """

    #C = <j,m|j,m>
    C = 0  
    # cn1 = str(a)+...   Ex : + 1/6 + 2/3 + 1/6  
    cn1 = " "      
    # Counter represents k1
    counter = 0

    m1 = j1   
    while m1 >= -j1:

        m2 = -j2
        while m2 <= j2:

            if m2 + m1 == m - i:   # m = m1 + m2 toujours, et valeur nouvelle de m c'est m-i

                # Pascal Matrix dimensions
                rows = i + 1     
                columns = i + 1

                # Empty Matrix (0)
                Pascal_Matrix = [[0] * columns for _ in range(rows)]

                """
                • All elements with column index e = 0 are equal to 1.
                • All elements on the diagonal are equal to 1.
                • The elements between the diagonal of the matrix and column index e = 0 :  
                                      PM[k][e] = PM[k-1][e] + PM[k-1][e-1]
                • All other elements are zero.
                """
                # filling the matrix
                k = 0 
                while k <= i :
                    
                    e = 0
                    while e <= k :  
                        
                        if k == e :              
                            Pascal_Matrix[k][e] = 1  
                        elif e == 0 :
                            Pascal_Matrix[k][e] = 1  
                        elif (e > 0) and (e < k):  
                            Pascal_Matrix[k][e] = Pascal_Matrix[k-1][e] + Pascal_Matrix[k-1][e-1] 
                            
                        e = e + 1
                        
                    k = k + 1  

                """
                We need to add the square root to jm, jm1, jm2 at the beginning of the calculation or 
                we can square Pascal_Matrix[k][e] and take the square root at the end of the calculation.
                """
                CO = Pascal_Matrix[i][counter]*Pascal_Matrix[i][counter]
                
                # Coefficient finale 
                a = (CO*CP[counter]*CD[i-counter])/CF[i]

                # Conversion de r sous forme a/b
                a = Fraction(a).limit_denominator() 

                if (a!=0 and a!=1) :
                    f2 = " + √({})|{},{};{},{}> ".format(a,j1, j2, m1, m2)  # Partie 2 de (+r|j1,j2,m1,m2>)
                    f1 = f1 + f2  # on ajoute partie 2 a partie 1
                    cn1 = cn1 + " + " + str(a) 
                    C = C + a   #C = <j,m|j,m>
                elif (a==1):
                    f2 = " |{},{};{},{}> ".format(j1, j2, m1, m2)  # Partie 2 de (+r|j1,j2,m1,m2>)
                    f1 = f1 + f2  # on ajoute partie 2 a partie 1
                    cn1 = cn1 + str(a) 
                    C = C + a   #C = <j,m|j,m>  

            m2 = m2 + 1 
        m1 = m1 - 1  
        counter = counter + 1 

    if C == 1 : 
        condition = "\t Normalization Condition is verified \n\n"    
    else : 
        condition = "\t Normalization Condition isn't verified \n\n" 
        

    print(f1)      # Affiche de |J,M -i > = .....

    f3 =" <{},{}|{},{}> = {} = {} ".format(j,m-i,j,m-i,cn1,C) + condition + f3

    print("-"*135) # Just a break line seperates results 

    i = i + 1 

print(f3)

print("*"*590,"This Code was made by Amine Slimani","*"*597)   # Signature
