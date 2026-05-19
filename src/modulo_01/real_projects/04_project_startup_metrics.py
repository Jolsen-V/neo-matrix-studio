# Module 01: project 04

# topic: project 04 - calculate the metrics of a startup
print("_____________________________________________")
print("|                                            |")
print("|------- SIMULATOR OF STARTUP METRICS -------|")
print("|                                            |")
print("|____________________________________________|")
print()

# data of the startup
print("--------- DATA OF THE STARTUP ---------")
name_startup = input("Startup name: ")
sector = input("startup sector: ")
product = input("product of startup: ")
print()

# MRR - Monthly Recurring Revenue / ARR - Annual Recurring Revenue
print("--------- MRR - Monthly Recurring Revenue ---------")
print("          ARR - Annual Recurring Revenue           ")
print()
clients = int(input("How many clients do you have?: "))
price_for_client = float(input("monthly price per client $."))
cyber_promotion = float(input("What percentage discount is it in a cyber promotion?: "))
print()

# churn rate - customer attrition rate
print("--------- CHURN RATE ---------")
clients_left = int(input("clients left in the last month: "))
clients_promotion = int(input("Customers acquired with the promotion in the last month: "))
print()

# CAC - Customer Acquisition Cost
print("--------- CAC - Customer Acquisition Cost ---------")
marketing_cost = float(input("Monthly marketing cost $."))
new_clients = int(input("New clients acquired in the last month: "))
clients_for_invitation = int(input("Clients acquired by invitation in the last month: "))
print()

# LTV - Lifetime Value
print("--------- LTV - Lifetime Value ---------")
average_months = int(input("average months a client stays: "))
display_free = int(input("monthly free viewing: "))
print()

#* calculate the metrics of the startup
mrr = clients * price_for_client
arr = mrr * 12
churn_rate = (clients_left / clients) * 100
cac = marketing_cost / new_clients
invitation_discount = price_for_client * (cyber_promotion / 100)
invitation_percentage = (clients_for_invitation / clients) * 100
ltv = price_for_client * average_months 
promotional_percentage = (clients_promotion / clients) * 100
view_free_percentage = (display_free / clients) * 100
print()

#* calculate project startup metrics
print("__________________________________________________")
print("|                     ⭐️⭐️⭐️⭐️⭐️                    |")
print("|___***___ RESULTS OF THE STARTUP METRICS ___***___|")
print("|                                                  |")
print()

print("............. DESCRIPTION OF THE STARTUP .............")
print()
print(f"startup name: {name_startup.upper()}")
print(f"startup sector: {sector.upper()}")
print(f"product of startup: {product.upper()}")
print()

print("............. MRR & ARR .............")
print()
print(f"We have {clients} clients with MRR: ${mrr:,.2f}")
print(f"price per client: ${price_for_client:,.2f}")
print(f"ARR: ${arr:,.2f}")
print()

print("............. CHURN RATE .............")
print()
print(f"clients left are: {clients_left} in the last month: {churn_rate:.2f}%")
print(f"Our clients acquired are: {clients_promotion} in the last month: {invitation_percentage:.2f}%")
print()

print("............. CAC .............")
print()
print(f"marketing cost: ${marketing_cost:,.2f} for monthly and CAC is of: ${cac:,.2f}")
print(f"new clients acquired: {new_clients} persons")
print(f"clients acquired by invitation: {clients_for_invitation} persons {invitation_percentage:.2f}%")
print()

print("............. LTV .............")
print()
print(f"Average months a client stays: {average_months} months and {churn_rate:.2f}%")
print(f"Monthly free viewing: {display_free} of persons")
print(f"LTV final is: ${ltv:,.2f}")
print()

print("............. PROMOTIONAL CLIENTS .............")
print()
print(f"Promotional clients: {clients_promotion} — {promotional_percentage:.2f}% of total clients")
print(f"View free: {view_free_percentage:.2f}% and LTV: ${ltv:,.2f}")
print()

print("_____________________________________________________________________")
print("|| 🌟🌟✨ 😉thank you for use this simulator of startup metrics.🌟🌟✨||")
print("_____________________________________________________________________|")