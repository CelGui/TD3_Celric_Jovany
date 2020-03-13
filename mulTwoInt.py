import sys

def mul():
        return x*y

if __name__=="__main__":

          if ( len(sys.argv) == 1 ):
                    x = input( " La premiere valeur est, svp: ")
                    y = input( " La deuxieme valeur est, svp: ")
                    x = int(x)
                    y = int(y)
                    print("La somme est: ", mul() )
