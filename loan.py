def loan_decision(age, income, credit_score, employment):
    # 1. Data Validation (BVA & EP)
    if not isinstance(age, int) or age < 18 or age > 65:
        return "Invalid Input"
    if not isinstance(income, (int, float)) or income < 5.0 or income > 500.0:
        return "Invalid Input"
    if not isinstance(credit_score, int) or credit_score < 300 or credit_score > 850:
        return "Invalid Input"
    if employment not in ['C', 'F']:
        return "Invalid Input"

    # 2. Risk Classification
    if 300 <= credit_score <= 500:
        risk = "High"
    elif 501 <= credit_score <= 700:
        risk = "Medium"
    else:
        risk = "Low"

    # 3. Decision Logic (Decision Table Implementation)
    if risk == "High":
        return "REJECT"

    if income < 15.0:
        if employment == "C" and risk == "Low":
            return "MANUAL REVIEW"
        return "REJECT"
    else:  # income >= 15.0
        if employment == "C":
            return "APPROVE"
        return "MANUAL REVIEW"