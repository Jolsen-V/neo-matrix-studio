# module 01: project 05

# topic: Neo Launch - PayneW startup simulator

print("_____________________________________________")
print("|                                            |")
print("|---- 💳 NEO LAUNCH — PayneW Simulator 🚀-----|")
print("|                                            |")
print("|____________________________________________")
print()

#data of the startup of PayneW
print("--------- DATA OF THE STARTUP ---------")
print()
name_startup = input("Startup name: ")
country_startup = input("launch country : ")
launch_year_month_day = input("launch date (YYYY-MM-DD): ")
sector = input("startup sector: ")
product = input("product of startup: ")
print()

# Expenses and startup launch fund
print(f"======== launch cost: {name_startup.upper()} ========")
print()
capital = float(input("capital initial: $. "))
investment_abroad = float(input("investment abroad: $. "))
cost_collaboration = float(input("cost of collaboration: $. "))
cost_hosting = float(input(f"cost of hosting of {name_startup} is: $. "))
logo_cost = float(input(f"cost of logo for {name_startup}: $. "))
marketing_cost = float(input(f"cost of marketing for {name_startup}: $. "))
expansion_cost = float(input(f"cost of expansion for {name_startup}: $. "))
print()

#team and clients
print(f"======== TEAM & CLIENTS OF {name_startup.upper()} ========")
print()
workers = int(input("how many workers will it have?: "))
initial_clients = int(input("initial clients: "))
salary_worker = float(input("monthly payment: $. "))
customers_projection = int(input("customers projection: "))
group = int(input("How many groups: "))
pay_monthly = input("how much do you pay monthly? $: ")
commission_transactions = input(" how much commission for transactions? %: ")
average_transaction = float(input("average transaction: $. "))
print()

# Calculate the cost of the startup
payroll = salary_worker * workers
total_expenses = cost_collaboration + cost_hosting + logo_cost + marketing_cost + expansion_cost

# revenue 
mrr = initial_clients * pay_monthly
commission_average = initial_clients * average_transaction * (commission_transactions / 100)

total_revenue = mrr + commission_average
