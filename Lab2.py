reg_hours = 40
reg_rate = 18.25
ov_rate = 27.78
workhours = float(input("Enter your work hours: "))
overtime_hours = workhours - reg_hours
if(overtime_hours <= 0): 
    overtime_hours = 0
regular_wage = (workhours - overtime_hours)*reg_rate
overtime_wage = overtime_hours * ov_rate
total_wage = regular_wage + overtime_wage
print("Regular Charge: " , regular_wage)
print("Overtime Charge: ",overtime_wage)
print("Total Wage:$ ", total_wage)