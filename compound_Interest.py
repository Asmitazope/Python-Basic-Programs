def compound_Interest(principle,rate,time):
    amount=principle*(pow((1+rate/100),time))
    cmp_interest=amount-principle

    print("Compound Interest is:",cmp_interest)

compound_Interest(10000,10.25,5)
