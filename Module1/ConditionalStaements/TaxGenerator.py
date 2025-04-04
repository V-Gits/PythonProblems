INCOME = float(input("Enter the Salary: "))
if 0 < INCOME < 50000:
    print("No Tax for Upto $50000\n")
elif 50001 <= INCOME <= 100000:
    TaxAmount = INCOME*0.01
    print(f"10% Tax for Upto $100000\nTax Amount: ${TaxAmount}\n")
elif 100000 < INCOME <= 200000:
    TaxAmount = (100000*0.01) + ((INCOME-100000)*0.02)
    print(f"10% Tax for Upto $100000\n20% Tax for Upto $200000\nTax Amount: ${TaxAmount}\n")
elif INCOME > 200000:
    TaxAmount = (100000*0.01) + ((100000)*0.02) + ((INCOME-200000)*0.03)
    print(f"10% Tax for Upto $100000\n20% Tax for Upto $200000\n30% Tax for above $200000\nTax Amount: ${TaxAmount}\n")