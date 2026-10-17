import sys

def main():
    amount , fr , to = get_arguments()
    print(amount , fr , to)
    rate=52.851
    print(convert(amount, rate))
    


    
    
    
  
def get_arguments():
    if len(sys.argv) < 4:
        sys.exit("Usage: python converter.py <amount> <from> <to>") 
    elif len(sys.argv) > 4:
        sys.exit("Usage: python converter.py <amount> <from> <to>")
    
    try:
        x=float(sys.argv[1])
    except ValueError:
        sys.exit("Amount must be a number.")


    if x <0:
        sys.exit("Amount must be positive.")
    return x , sys.argv[2].upper() , sys.argv[3].upper()

def convert(amount , rate):
    return amount*rate






         
    
if __name__=="__main__":
    main()      
    

