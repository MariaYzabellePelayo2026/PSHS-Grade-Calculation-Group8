print("=== PSHS Grades Calculator ===")
print("Hello! A pleasant day to you! Enjoy calculating your grade.")

q1 = float(input("Enter Q1 Grade in %: "))
tentative_q2 = float(input("Enter Tentative Q2 Grade in %: "))
tentative_q3 = float(input("Enter Tentative Q3 Grade in %: "))
tentative_q4 = float(input("Enter Tentative Q4 Grade in %: "))

q2 = (q1 + 2 * tentative_q2) / 3
q3 = (q2 + 2 * tentative_q3) / 3
final_grade = (q3 + 2 * tentative_q4) / 3
