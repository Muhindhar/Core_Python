held = int(input("Enter number of classes held: "))
attended = int(input("Enter number of classes attended: "))
attendance=(attended/held)*100
if attendance>=75:
    print(str(int(attendance))+"% Allowed")
else:
    medical_cause = input("Do you have medical cause? (Y/N): ")
    if medical_cause=="Y":
        print(str(int(attendance))+"% Allowed")
    else:
        print(str(int(attendance))+"% Not allowed")
