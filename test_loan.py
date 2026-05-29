from loan import loan_decision

cases = [
    (17, 20.0, 700, "C", "Invalid Input"),
    (66, 20.0, 700, "C", "Invalid Input"),
    (30, 4.9, 700, "C", "Invalid Input"),
    (30, 500.1, 700, "C", "Invalid Input"),
    (30, 20.0, 299, "C", "Invalid Input"),
    (30, 20.0, 700, "X", "Invalid Input"),
    (30, 20.0, 400, "C", "REJECT"),
    (30, 14.9, 600, "C", "REJECT"),
    (30, 14.9, 750, "F", "REJECT"),
    (30, 14.9, 750, "C", "MANUAL REVIEW"),
    (30, 15.0, 650, "C", "APPROVE"),
    (30, 15.0, 750, "F", "MANUAL REVIEW"),
]

print("Bat dau chay kiem thu luong du lieu...")
print("-" * 45)

for i, (age, income, score, emp, expected) in enumerate(cases, 1):
    result = loan_decision(age, income, score, emp)

    if result == expected:
        print(f"TC{i:02d}: Chay thanh cong (Gia tri nhan ve: {result})")
    else:
        print(f"TC{i:02d}: THAT BAI! Ky vong '{expected}' nhung ra '{result}'")
        exit(1)

print("-" * 45)
print("Ket qua: Da thong qua toan bo 12 test cases!")