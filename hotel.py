class Hotel:
    bill=0
    
    def __init__(self):
       
        print("-----------------MENU---------------------\n\n1. VEG:\n\ta. Palak Paneer\t\t50 Rs\n\tb. Veg Biryani\t\t60 Rs")
        print("\n2. NON-VEG:\n\tc. Chicken Biryani\t100 Rs\n\td. Chicken Masala\t90 Rs")
        print("------------------------------------------------------------------------------")


    def veg(s):
        choice= input("\nwhat do you like to have in VEG?? For Palak Paneer click 'a' and For Veg Biryani click 'b': ")
        if choice=='a':
            qantity= int(input("\nHow much qantity you have?: "))
            s.bill= s.bill+(qantity*50)
                
        elif choice=='b':
            qantity= int(input("\nHow much qantity you have?: "))
            s.bill= s.bill+(qantity*60)
                   
        

    def nonveg(s):
        choice= input("\nwhat do you like to have in NON-VEG??  For Chicken Biryani click 'c' and for Chicken Masala click 'd': ")
        if choice=='c':
            qantity= int(input("\nHow much qantity you have?: "))
            s.bill= s.bill+(qantity*100)
                    
        elif choice=='d':
            qantity= int(input("\nHow much qantity you have?: "))
            s.bill= s.bill+(qantity*90)
                
        

    def menu(s):
        option= int(input("\nFor VEG click 1 and For NON-VEG click 2: "))
        if option==1:
            s.veg()
        elif option==2:
            s.nonveg()
                
        again= input("\nDo you want to order again?(y/n)")
        if (again=='Y' or again=='y'):
            s.menu()
        elif (again=='N' or again=='n'):
            print("\nYOUR TOTAL AMOUNT IS: ", s.bill, "Rs")
            print("\nTHANK YOU FOR VISITING!!!")



h=Hotel()
h.menu()
        








