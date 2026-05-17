# Module 01: project 01

#name: project 01 - calculate ROI of a startup

print("=========================================")
print(" 🌱 ROI calculate - first startup project ⭐️ ")
print("=========================================")

# ask for data
investment = float(input("How much do you want to invest: $."))
revenue = float(input("Revenue obtained of the investment: $."))
investment_time = int(input("How many years do you want to invest?:"))
investment_months = investment_time * 12

# calculate ROI: Basic , Annualized and Monthly
gain_basic = revenue - investment
roi = ((revenue - investment) / investment) * 100
annualized_roi = ((revenue / investment) ** (1/ investment_time) - 1) * 100
monthly_roi = (gain_basic / (investment * investment_months)) * 100

gain_annualized = investment * (annualized_roi / 100) * investment_time
gain_monthly = investment * (monthly_roi / 100) * investment_months


#* Show results of gain and roi
print(" ")
print("*********************************************************")
print(f" My first investment is: $ {investment:,.2f}")
print(f" My time of investment is: {investment_time} years and {investment_months} months.")
print(f" percentage of gain is: {roi:.2f}%")
print(f" annualized percentage of gain is: {annualized_roi:.2f}%")
print(f" monthly percentage of gain is: {monthly_roi:.2f}%")
print(f" gain basic  is: ${gain_basic:,.2f}")
print(f" gain annualized is: ${gain_annualized:,.2f} ")
print(f" gain monthly is: ${gain_monthly:,.2f} ")
print("*********************************************************")

print(" 🌟🌟✨ 😉thank you for use this calculator of ROI.🌟🌟✨")