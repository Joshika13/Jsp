age=int(input("Enter your age:"))
current_year=int(input("Enter the year:"))
year_of_birth=(current_year)-age
bday=input("Has your birthday passed this year(yes/no):").lower()
if bday=="yes":
    print("The year of your birth is :",year_of_birth)
else:
    print("The year of your birth is:",(year_of_birth)-1)
