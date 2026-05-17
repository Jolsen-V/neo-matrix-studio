# module 01: project 03

# topic: project 03 - create a profile of a developer
print("--------- CV OF A DEVELOPER ---------")
print()
print("______________________________________")
print(" 🧑🏻‍💻 PROFILE OF A DEVELOPER 🧑🏻‍💻")
print("______________________________________")
print()

# Personal data
print("--------- PERSONAL DATA ---------")
name = input("what is your name?: ")
age = int(input("What is your age?: "))
dni = input("What is your DNI?: ")
marital_status = input("What is your marital status? (single/married): ")
email = input("What is your email?: ")
phone = input("What is your phone number?: ")
city = input("where are you from?: ")
print()


# education data
print("--------- EDUCATION DATA ---------")
education = input("what is your education level?: ")
school = input("which school did you attend?: ")
university = input("which university did you attend?: ")
short_courses = input("what course do you know?: ")
office_programs = input("What is your level in office programs?: ")
languages = input(" Wow many languages do you speak?: ")
print()

# company and business data
print("--------- COMPANY AND BUSINESS DATA ---------")
company = input("What companies have you worked for?: ")
business = input("What business do you have? : ")
startup = input("What is the name of your startup?: ")
marketing  = input("What apps do you use for marketing? : ")
red_social = input("Which social network do you know?? : ")
print()

# experience data
print("--------- EXPERIENCE DATA ---------")
experience_company = input(f"How many years of experience do you have in {company}?: ")
experience_business = input(f"How many years of experience do you have in {business}?: ")
experience_startup = input(f"How many years of experience do you have in {startup}?: ")
experience_marketing = input(f"How many years of experience do you have in {marketing}?: ") 
experience_red_social = input(f"How many years of experience do you have in {red_social}?: ")
print()

#* profile complete of CV of a developer
print("_____________ Welcome to Your Profile _______________")
print()
print("-------------     PERSONAL DATA       -------------")
print(f"Name: {name.upper()}")
print(f"Age: {age} years")
print(f"DNI: {dni}")
print(f"Marital status: {marital_status.upper()}")
print(f"Email: {email}")
print(f"Phone: {phone}")
print(f"City: {city.upper()}")
print()

print("-------------     EDUCATION DATA       -------------")
print(f"Education level:{education.upper()}")
print(f"School name: {school.upper()}")
print(f"University name: {university.upper()}")
print(f"My short courses: {short_courses.upper()}")
print(f"My level in office programs: {office_programs.upper()}")
print(f"I speak {languages} languages")
print()

print("-------------     COMPANY AND BUSINESS DATA       -------------")
print(f"My first company worked: {company.upper()}")
print(f"My first business: {business.upper()}")
print(f"My first startup founded: {startup.upper()}")
print(f"my first  app or web marketing : {marketing.upper()}")
print(f"social networks I know: {red_social.upper()}")
print()

print("-------------     EXPERIENCE DATA       -------------")
print(f"Experience in {company.upper()}: {experience_company} years")
print(f"Experience in {business.upper()}: {experience_business} years")
print(f"Experience in {startup.upper()}: {experience_startup} years")
print(f"Experience in {marketing.upper()}: {experience_marketing} years")
print(f"Experience in {red_social.upper()}: {experience_red_social} years")
print() 

print(" 🌟🌟✨ 😉thank you for using this profile 🌟🌟✨")
print(" _____________________________________________")