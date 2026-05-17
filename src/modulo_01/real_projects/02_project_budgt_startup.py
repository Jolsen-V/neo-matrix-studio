# module 01: project 02

#topic: project 02 - calculate the budget of a startup
print("------------------------------------------")
print(" Simulator for starting a company 🏦 ")
print("------------------------------------------")
print()

# capital for the foundation of the company
name_company = input("What will the company name be? :")
capital = float(input("How much capital do you have for the foundation of the company? $."))
permissions = input("What permissions do you have?: ")
approach = input("What will the company focus on?: ")  
workers = int(input("how many workers will it have?: "))

# bills of the company
rent = float(input("How much is the rent of the office? $."))
salary= float(input("monthly payment: $."))
computer = float(input("bill of computer equipment: $."))
internet = float(input("bill of internet: $."))

# calculate the total of bills
total_bills = rent + salary * workers + computer + internet
surplus_capital = capital - total_bills
pay_workers = salary * workers
percentage = (total_bills / capital) * 100

#* business expense summary
print()
print("===========================================")
print(" ------ SUMMARY OF BUSINESS EXPENSES ------- ")
print("===========================================")
print()
print(f" company name: {name_company.upper()}")
print(f" My capital for the foundation of the company is: $ {capital:,.2f}")
print(f" I have the permissions: {permissions}")
print(f" My approach is: {approach.upper()}")
print(f" My first stage: {workers} workers") 
print()
print("*******************************************")
print("------ BILLS OF THE COMPANY -----")
print("*******************************************")
print(f"rent:               $ {rent:,.2f}")
print(f"payment to workers: $ {pay_workers:,.2f}")
print(f"computer equipment: $ {computer:,.2f}")
print(f"internet:           $ {internet:,.2f}")
print(f"total bills:        $ {total_bills:,.2f}") 
print()

print("__________________________________")
print(f"bills total:     $ {total_bills:,.2f}")
print(f"surplus capital: $ {surplus_capital:,.2f}")
print(f"percentage of bills: {percentage:,.2f} %")
print("__________________________________")
print()

print(" 🏪 thank you for using this simulator 🧑🏻‍💻 ")

