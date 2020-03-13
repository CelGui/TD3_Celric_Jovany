import sys

def add():
        return x+y

if __name__== "__main__":
 
        if ( len(sys.argv) == 1 ):
                 x = input( " La premiere valeur, svp: ")
                 y = input( " La deuxieme valeur, svp: ")
                 x = int(x)
                 y = int(y)
                 print("La somme est: ", add() )

