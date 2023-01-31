money_earned = float(input("Enter how much money you earned: $ "))
fast_offering = float(input("Enter how much money you would like to pay for fast offering: $ "))

print ("\n")
input1 = input("First Item  ")
monthly1 = float(input("First Item Amount  $"))
input2 = input("Second Item ")
monthly2 = float(input("Second Item Amount  $"))
input3 = input("Third Item  ")
monthly3 = float(input("Third Item Amount  $"))
input4 = input("Fourth Item ")
monthly4 = float(input("Fourth Item Amount  $"))
input5 = input("Fifth Item  ")
monthly5 = float(input("Fifth Item Amount  $"))
print ("\n")
format_budget_lines = "{:15} ${:-10.2f} ${:-10.2f}"


headers = '{:>20}'.format('')
#print headers.format("Personal Budget")
print( "************************************")
print ('{:>25}'.format("Personal Budget"))
print ("------------------------------------")


monthly_earned = float(money_earned)
yearly_earned = float(money_earned * 12)
print (format_budget_lines.format(" ", monthly_earned, yearly_earned))
tithing = money_earned / 10


print ("")
print ('{:>25}'.format("May's Expenses"))
print ("************************************")
print ("Expense".ljust(1) + " Month ".rjust(15) + " Annual ".rjust(15) )
print ("------------------------------------")
print (format_budget_lines.format("Tithing", tithing, tithing * 12))
print (format_budget_lines.format("Fast Offering", fast_offering, fast_offering * 12))
print (format_budget_lines.format(input1, monthly1, monthly1 * 12))
print (format_budget_lines.format(input2, monthly2, monthly2 * 12))
print (format_budget_lines.format(input3, monthly3, monthly3 * 12))
print (format_budget_lines.format(input4, monthly4, monthly4 * 12))
print (format_budget_lines.format(input5, monthly5, monthly5 * 12))


print ("")
print ('{:>25}'.format("Savings"))
print ("************************************")
print ("Savings".ljust(1) + " Month ".rjust(15) + " Annual ".rjust(15) )
print ("------------------------------------")
monthly_sav = (money_earned) - (tithing) - (fast_offering) - (monthly1) - (monthly2) - (monthly3) - (monthly4) - (monthly5)
print (format_budget_lines.format("", monthly_sav, monthly_sav * 12))
