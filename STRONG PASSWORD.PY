p=input("enter the password")
if len(p)>6 or len(p)<16:
    if "A" in p or "Z" in p:
        if "$" in p:
            if "2" in p or "8" in p:
                print("ye strong password hai")
            else:
                print("ye weak password  hai")
        else:
            print("ye weak password hai")
    else:
        print("ye weak password hai")
else:
    print("ye weak password hai")