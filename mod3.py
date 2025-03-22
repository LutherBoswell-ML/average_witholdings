def calculate_average_withholding():
    try:
        num_weeks = int(input("Enter the number of weeks: "))
        total_income = 0.0
        total_tax_withheld = 0.0

        for week in range(1, num_weeks + 1):
            income = float(input(f"Enter income for week {week}: $"))
            
            if income < 500:
                tax_rate = 0.10
            elif 500 <= income < 1500:
                tax_rate = 0.15
            elif 1500 <= income < 2500:
                tax_rate = 0.20
            else:
                tax_rate = 0.30
            
            tax_withheld = income * tax_rate
            print(f"Tax withheld for week {week}: ${tax_withheld:.2f}")
            
            total_income += income
            total_tax_withheld += tax_withheld

        average_tax_withheld = total_tax_withheld / num_weeks
        print("\n--- Summary ---")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Tax Withheld: ${total_tax_withheld:.2f}")
        print(f"Average Weekly Tax Withheld: ${average_tax_withheld:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values only.")

# Run the function
calculate_average_withholding()
