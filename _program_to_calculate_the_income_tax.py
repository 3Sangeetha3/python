ded_80c = int(input('deduction under 80c: '))
ded_80cc = int(input('deduction under 80cc: '))
ded_hra = int(input('deduction under HRA: '))
ded_medical = int(input('deduction under Medical: '))

standard_deduction = 150000
total_deductions = ded_80c + ded_80cc + ded_hra + ded_medical + standard_deduction

gross_income = int(input('gross income: '))

taxable_income = gross_income - total_deductions

if taxable_income > 0:
    if gross_income <= 500000:
        income_tax = taxable_income * .1
    elif gross_income <= 1000000:
        income_tax = 25000 + ((gross_income - 500000) * .2)
    else:
        income_tax = 75000 + ((gross_income - 1000000) * .3)
    print("gross income:", gross_income)
    print("total deductions:", total_deductions)
    print("income tax:", income_tax)
else:
    print("hurray..No Income Tax")