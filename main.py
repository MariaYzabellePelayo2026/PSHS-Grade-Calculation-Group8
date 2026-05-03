print("=== PSHS Grades Calculator ===")
print("Hello! A pleasant day to you! Enjoy calculating your grade.")

q1 = float(input("Enter Q1 Grade in %: "))
tentative_q2 = float(input("Enter Tentative Q2 Grade in %: "))
tentative_q3 = float(input("Enter Tentative Q3 Grade in %: "))
tentative_q4 = float(input("Enter Tentative Q4 Grade in %: "))

q2 = (q1 + 2 * tentative_q2) / 3
q3 = (q2 + 2 * tentative_q3) / 3
final_grade = (q3 + 2 * tentative_q4) / 3

if final_grade >= 96:
    equivalent = "1.00"
    remarks = "EXCELLENT"
elif final_grade >= 90:
    equivalent = "1.25"
    remarks = "VERY GOOD"
elif final_grade >= 84:
    equivalent = "1.50"
    remarks = "VERY GOOD" 
elif final_grade >= 78:
    equivalent = "1.75"
    remarks = "GOOD"
elif final_grade >= 72:
    equivalent = "2.00"
    remarks = "GOOD"
elif final_grade >= 66:
    equivalent = "2.25"
    remarks = "SATISFACTORY"
elif final_grade >= 60:
    equivalent = "2.50"
    remarks = "SATISFACTORY"
elif final_grade >= 55:
    equivalent = "2.75"
    remarks = "FAIR"
elif final_grade >= 50:
    equivalent = "3.00"
    remarks = "FAIR"
elif final_grade >= 40:
    equivalent = "4.00"
    remarks = "FAILED ON CONDITION"
else:
    equivalent = "5.00"
    remarks = "FAILED"

print("=== RESULT ===")
print("Final Percent Grade:", round(final_grade, 2))
print("Equivalent:", equivalent)
print("Adjectival Equivalent:", remarks)
