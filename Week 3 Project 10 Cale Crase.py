"""
Program: Project10 Crase
Author: Cale Crase
Employee's Overtime Calculator
"""

hour = int(input("How much is the hourly wages: "))
total = int(input("How much total hours did they work: "))
overtime = int(input("How long was their overtime: "))
overtime_pay = overtime * 1.5 * hour
pay = hour * total + overtime_pay
print("The employee's pay is,", pay, )
