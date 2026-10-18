import sys
import requests


def main():
    amount , fr , to = get_arguments()
    rate=get_rate(fr,to)
    print(f"{amount} {fr} = {convert(amount,rate):.2f} {to}")
    

    
    
  
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


def get_rate(fr,to):
    try:
        response=requests.get(f"https://api.frankfurter.dev/v2/rate/{fr}/{to}",timeout=3)
    except requests.exceptions.RequestException:
        sys.exit("Could not connect to the exchange rate service. Check your internet connection and try again.")
    
    if response.status_code == 422 :
        sys.exit(f"Invalid currency: {to} or {fr} . Please enter a valid currency code.")
    elif response.status_code != 200:
        sys.exit("Could not connect to the exchange rate service")
        
        
    data=response.json()
    
    return data["rate"]

        
    
    


    

         
    
if __name__=="__main__":
    main()      
    

