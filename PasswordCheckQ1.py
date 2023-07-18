pwd= (input("Enter Password: "))

def check_password_strength(pwd):


    if len(pwd) >=8:
        if (any(char.islower() for char in pwd)==True) and  (any(char.isupper() for char in pwd)== True):  #islower()/isupper() gives o/p = TRUE
            # print("Good Password")
            if any(char.isdigit() for char in pwd):                     #isdigit() gives o/p = True
                # print("Your password has at least 1 number")
                if any( not char.isalnum() for char in pwd):            #not isalnum() = at leat any 1 character should be other than Alphanumeric(which is special char ex- @,$,#,& etc)
                    # print("Your Password has a special char")
                    # print("Your Password Strength looks Good.")
                    # return print(pwd, "Your Password Strength looks Good")
                    return print(bool(pwd))

                else: print("Your Password strength looks weak, it should contain atleast 1 special Char.")

            else: print("Your Password strength looks weak, it should contain at least 1 Number.")

        else: print("Your Password strength looks weak, it should contain atleast 1 Upper & 1 Lower case character.")

    else: print("Your Password strength looks weak, it should atleast 8 character long.")    


(check_password_strength(pwd))



     
    
    





