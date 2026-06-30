ticket=[]
while True:
    print('''TICKET BOOKING SYSTEM
          \n choose 1 to display all booking
          \n choose 2 to book a ticket
          \n choose 3 to search booking
          \n choose 4 to update booking
          \n choose 5 to cancel booking 
          \n choose 6 to exit''')
    choice=int(input("enter your choice"))
    if choice==1:
        if len(ticket)==0:
            print("no bookings")
        else:
            print("all bookings:")
            for i in tickets:
                print("ticket id:",i[0])
                print("passenger name:",i[1])
                print("from:",i[2])
                print("to:",i[3])
                print("seats:",i[4])
    elif choice==2:
        i=int(input("enter ticket id:"))
        n=input("enter passenger's name:")
        d=input("enter place of departure:")
        a=input("enter place of arrival:")
        s=int(input("enter no. of seats:"))
        t=[i,n,d,a,s]
        ticket.append(t)
        print("booking successful")
    elif choice==3:
        s=int(input("enter id of ticket that you want to search:"))
        found=False
        for i in ticket:
            if i[0]==s:
                print("booking found")
                print("ticket id:",i[0])
                print("passenger name:",i[1])
                print("from:",i[2])
                print("to:",i[3])
                print("seats:",i[4])
                found=True
                break
        if found==False:
            print("booking not found")
    elif choice==4:
        u=int(input("enter ticket id that you want to update:"))
        found=False
        for i in ticket:
            if i[0]==u:
                i[1]=input("enter name:")
                i[2]=input("from:")
                i[3]=input("to:")
                i[4]=int(input("enter no of seats:"))
                print("booking updated")
                found=True
                break
        if found==False:
            print("booking not found")
    elif choice==5:
        c=int(input("enter ticket id that you want to cancel:"))
        for i in ticket:
            if i[0]==c:
                ticket.remove(i)
                print("booking cancelled")
    elif choice==6:
        print("thankyou!")
        break
    else:
        print("invalid choice")
            
        
    
            
                      
                      
                
