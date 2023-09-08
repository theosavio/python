roman_val={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
while True:
    roman=input("roman").upper()
    if roman=="exit":
        break
    total=0
    for i in range(len(roman)-1,0,-2):
        if roman_val[roman[i-1]]<roman_val[roman[i]]:
            total=total+(roman_val[roman[i]]-roman_val[roman[i-1]])
        else:
            total=total+(roman_val[roman[i]]+roman_val[roman[i-1]])
    if len(roman)%2!=0:
        total=total+roman_val[roman[0]]
    print("number",total)
    
