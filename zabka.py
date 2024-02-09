print("Witaj w sklepie Żabka!")

age = int(input("Podaj swój wiek: "))
number_of_products = int(input("Podaj ilość produktów: "))
summary_of_bill = 0
number_of_transactions = 1
summary_of_transactions = 0
amount_of_highest_transaction = 1
number_of_highest_transcation = 0

for number_product in range(number_of_products):
    type_of_product = input(f"Podaj typ produktu {number_product + 1}: ")
    price_of_product = float(input(f"Podaj cenę produktu {number_product + 1}: "))
    if age < 18 and (type_of_product.lower() == "alkohol" or type_of_product.lower() == "papierosy" or type_of_product.lower() == "energetyk"):
          print("Produkt niedozwolony dla twojego wieku!")
          continue
    if price_of_product > 100:
          print("Niestety nie mamy takiego produktu na stanie!")
          continue
    summary_of_bill += price_of_product
    if summary_of_transactions >= 100:
        summary_of_transactions += price_of_product
    else:
        if summary_of_transactions >= amount_of_highest_transaction:
            amount_of_highest_transaction = summary_of_transactions
            number_of_highest_transcation = number_of_transactions
        number_of_transactions += 1
        summary_of_transactions = price_of_product

if number_of_transactions == 1:
    if summary_of_bill == 0:
         number_of_transactions = 0        
    amount_of_highest_transaction = summary_of_transactions
    number_of_highest_transcation = number_of_transactions

if number_of_transactions != 0:
    print(f"Suma rachunków: {summary_of_bill}")
    print(f"Liczba transakcji: {number_of_transactions}")
    print(f"Kwota największej transakcji: {amount_of_highest_transaction}")
    print(f"Numer największej transakcji: {number_of_highest_transcation}")
else:
    print("Niestety nie udało Ci się dokonać zakupu!")    