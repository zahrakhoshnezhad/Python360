x = 10
match x :
    case 10 | 11 | 12 : # | = or (pipe)
        print ("10 va 11 va 12")
    case 13 :
        print("13")    
    case _ :
        print ("_")    