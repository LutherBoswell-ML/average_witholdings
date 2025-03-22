# average_witholdings
# 🧮 Tax Withholding Calculator

This project calculates the **weekly average tax withholding** for a customer based on their weekly income. The program applies different tax rates depending on income brackets and provides a summary of the total income, total tax withheld, and the average tax withheld per week.

---

## 📌 Features

- Input weekly income for a user-defined number of weeks.
- Applies appropriate tax rate based on income:
  - Income < $500: **10%**
  - $500 ≤ Income < $1500: **15%**
  - $1500 ≤ Income < $2500: **20%**
  - Income ≥ $2500: **30%**
- Calculates and displays:
  - Tax withheld for each week.
  - Total income.
  - Total tax withheld.
  - Average weekly tax withheld.

---

## 🖥️ Sample Execution

withholding-calculator/
│
├── mod3.py     # Main source code
├── screenshots/                  # Screenshots of execution
│   ├── input_example.png
│   └── output_summary.png
├── README.md                     # Project documentation
