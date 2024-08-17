import requests
import json



API_URL = "https://v6.exchangerate-api.com/v6/7f1cfddd6602ad3dc081c591/latest/USD"

def fetch():
    
    try:
        response = requests.get(API_URL)
        data = response.json()
        
        if response.status_code == 200:
            return data['conversion_rates']
        else:
            print("Error fetching exchange rates:", data.get("error-type", "Unknown error"))
            return None
    except Exception as e:
        print(f"An error occuared: {e}")
        return None
    
def convert(amount,from_currency,to_currency,rates):
    
    if from_currency != 'USD':
        amount = amount / rates[from_currency]
    conveted_amount = amount * rates[to_currency]
    return conveted_amount


def main():
    rates = fetch()
    
    if rates:
        print("Available currencies:", ", ".join(rates.keys()))
        
        from_currency = input("Enter the base currency code (e.g., INR, EUR): ").upper()
        to_currency = input("Enter the target currency code: ").upper()
        amount = float(input(f"Enter amount in {from_currency}: "))
        
        
        if from_currency in rates and to_currency in rates:
            converted_amount = convert(amount,from_currency,to_currency,rates)
            print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        else:
            print("Invalid currency code entered. Please try again.")
            
    else:
        print("Failed to retrieve exchange rates.")
        
if __name__ == "__main__":
    main()
