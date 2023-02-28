# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1955604
# Date: 12th December 2022 


'''
get the part want to run as part_choise
get the number of credits in pass as pass_credit
get the number of credits in defer as defer_credit
get the number of credits in fail as fail_credit
print outcome
get the option whethere the user wants to enter another set of data or not
print Histrogram
print entered data with progression outcome
ask whethere the user wants to check other parts with same set of data or not
print the end statement

'''

count_progress  = 0
count_trailer   = 0
count_retriever = 0
count_exclude   = 0
total = 0

part_choise = None
update_opt = None
check_opt = None
answer = None
option = 'y'
login = None

All_data = []
Text_File = open("SD1_Coursework.txt","w")
uowid = {}

def menu():
    global part_choise
    
    while True:
        
        try: # To check part_choise input is an  integer
                    
            #while True:
                        
            print('+'*66,'\n')
            print_menu1 = 'Selection List'
            print_menu2 = print_menu1.center(64)
            print(print_menu2,"\n")
            print("Please choose the part you want to run according to the below list\n\n"
                  "\t\t>For Part 1 enter --> 1\n\t\t>For Part 2 enter --> 2 (Lists)\n"
                  "\t\t>For Part 3 enter --> 3 (Text File)\n\t\t>For Part 4 enter --> 4 (Dictionaries)\n"
                  "\t\t>To 'QUIT' enter  --> 0\n")
            print('+'*66,'\n')
            part_choise = int(input("Please enter your choise here >>> "))
            print()

            if part_choise in range(0,5):
                break

            else:
                print("Invalid choise, Please try again\n")
                    
        except ValueError:
            print("\nInvalid input, Please try again\n")
        
    return part_choise

def uid_validation():
    global update_opt
    global check_opt
    global answer
    global count_progress
    global count_trailer
    global count_retriever
    global count_exclude
    global total

    while True: # Loop until input a valid UoW ID like 'w1234567' format
                                
        uid=str(input("Enter the UoW ID : "))
                        
        try:    # Check 1-7 indexes of uid are numbers
            
            uid=uid.lower()     # convert 'W' to 'w'
            uid_num=list(uid[1:8])      # Listing the 1-7 indicies of uid
            for i in range(0,len(uid_num)): # https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/ 
                uid_num[i]=int(uid_num[i])

            if len(uid)==8 and uid[0]=="w": # To break the loop if UoW ID is in valid format
                if uid in uowid:    # Check if the uid is already exists
                    while True:     # Loop until enter an valid input
                        print("\nThe student ID already exist. Do you wish to update it?\n")
                        update_opt = input("\t(yes/no) >>> ")
                        
                        if update_opt.lower() in ['yes','no']:
                            update_opt = update_opt.lower()
                            break
                        print("Can not read your input, Please check again")
                        
                    if update_opt == 'yes':
                        check_opt == 0
                        value = uowid[uid]
                        if value[0] == 'Progress':
                            count_progress -= 1
                        if value[0] == 'Progress (module trailer)':
                            count_trailer -= 1
                        if value[0] == 'Module retriever':
                            count_retriever -= 1
                        if value[0] == 'Exclude':
                            count_exclude -= 1
                        total -= 1
                        
                    if update_opt == 'no':
                        print()
                        while True:     # Ask user that want to enter another student data or skip the entering new one and see results
                            answer = input("Do you wish to enter new student data? or"
                                           "\n'no' to see the result"
                                           "\n\n\t(yes/no) >>> ")
                            if answer.lower() in ['yes','no']:
                                answer = answer.lower()
                                break
                            else:
                                print("Invalid input, Please enter again")

                        if answer == 'yes':
                            print()
                            continue
                        
                print()
                return uid 
                break

            else:
                print("Invalid UoW ID\n")

        except ValueError:
            print("Invalid UoW ID\n")
    
def part_option():
    each_data=[]
    each_data.append(outcome)
    each_data.append(pass_credit)
    each_data.append(defer_credit)
    each_data.append(fail_credit)
        
    All_data.append(each_data)  # Create a nested list
    
    if part_choise == 4:
        uowid[uid] = each_data  # Assining the value to uid key in dectionary
            
    Text_File.write(f"{outcome} - {pass_credit}, {defer_credit}, {fail_credit}\n")

def print_results():
    if part_choise == 2:
        print("Output from List\n")
        for i in range(0,len(All_data)):
            print(All_data[i][0],end=" - ")
            print(*All_data[i][1:],sep=", ") # https://blog.finxter.com/how-to-print-a-list-without-brackets-in-python/#:~:text=You%20can%20print%20a%20list,str()%20built%2Din%20function.
                                    
    if part_choise == 3:
        print("Output from Text File\n")
        Read_File = open("SD1_Coursework.txt","r")
        Print_File = Read_File.read()
        Read_File.close()
        print(Print_File)

    if part_choise == 4:
        print("Output from Dictionary\n")
        for keys, value in uowid.items(): # https://www.tutorialspoint.com/How-to-print-all-the-keys-of-a-dictionary-in-Python#:~:text=Python%27s%20dict.,keys()%20method.
            print(keys,":",end=" ")
            print(value[0],end=" - ")
            print(*value[1:],sep=", ") # https://blog.finxter.com/how-to-print-a-list-without-brackets-in-python/#:~:text=You%20can%20print%20a%20list,str()%20built%2Din%20function.
    
while part_choise != 0: # Loop until part_choise == 0 (quit the program)
    
    menu()
            
    if part_choise != 0:
        
        if part_choise == 1:
            while True:     # Loop until input a valid input
                print('-'*66,'\n')
                print_menu3 = 'Student/Staff Login Potral'
                print_menu4 = print_menu3.center(64)
                print(print_menu4,"\n")
                print("For student login --> A")
                print("For staff login   --> B\n")
                login = input("Please respond here >>> ")
                if login.upper() == 'A' or login.upper() == 'B':
                    print('\n'+'-'*66,'\n')
                    break
                print("\nInvalid input, Please try again!\n")
                
        while option.lower() != 'q':
                
            if part_choise == 4:

                uid = uid_validation()
                
                if uid in uowid: # If user doesn't want to update existing data break the validation and continue rest of the program
                    if update_opt == 'no':
                        if answer == 'no':
                            option == 'q'
                            break
                            
            try:
                pass_credit = int(input("Enter your pass credits : "))
                                
                if pass_credit in range(0,121,20):
                    defer_credit = int(input("Enter your defer credits : "))
                                    
                    if defer_credit in range(0,121,20):
                        fail_credit = int(input("Enter your fail credits : "))

                        if fail_credit in range(0,121,20):

                            if pass_credit + defer_credit + fail_credit == 120:#9
                                        
                                if pass_credit == 120:
                                    count_progress += 1
                                    outcome = "Progress"
                                                    
                                elif pass_credit == 100:
                                    count_trailer += 1
                                    outcome = "Progress (module trailer)"
                                                    
                                elif fail_credit not in range(80,121,20):
                                    count_retriever += 1
                                    outcome = "Module retriever"
                                                    
                                else:
                                    count_exclude += 1
                                    outcome = "Exclude"

                                part_option()

                                print(outcome,'\n')
                                
                                total += 1

                                if part_choise == 1 and login.upper() == 'A':
                                    login = login.upper()
                                    total = 0
                                    break

                            else: 
                                print("Total Incorrect\n")
                        else: 
                            print("Out of Range\n")
                    else:
                        print("Out of Range\n")
                else: 
                    print("Out of Range\n")
                    
            except ValueError:
                print("Integer required\n")

            while True: # Loop until input a valid input
                                    
                print("\nWould you like to enter another set of data?")
                print("\n    >'y' for yes, or \n    >'q' to quit and view the results\n")
                option=str(input("Enter here >>> "))
                                    
                if option.lower() == 'y' or option.lower() == 'q':
                    print()
                    break
                    
        Text_File.close()
        
        if login != 'A':
            
            print("-"*66,"\n")

            print("Histogram\n")

            print(f"Progress {count_progress}  : {'*'* count_progress}")
            print(f"Trailer {count_trailer}   : {'*'* count_trailer}")
            print(f"Retriever {count_retriever} : {'*'* count_retriever}")
            print(f"Excluded {count_exclude}  : {'*'* count_exclude}")

            print()

            print(total,"outcomes in total.\n")

            print("-"*66,'\n')

            print_results()

            while True: # Loop until input a valid statement to opinion 
                print('\n'+'-'*66,'\n')
                opinion = input("Would you like to use the same set of data to print in other parts as well?\n\n"
                                "\tIf you enter [no] ALL THE DATA you entered so far will be DELETED\n"
                                "\t(yes/no) >>> ")
                
                if opinion.lower() == 'yes':
                    while part_choise != 0: # Loop until enter 0 to quit in the menu section
                        print()
                        menu()

                        if part_choise in [2,3]:
                            if check_opt == 0:
                                print("You updated some data in the program\n"
                                      "Therefore text file does not support it")
                            else:
                                print_results()
                        
                        if part_choise == 4: # To get Uow ID to print part 4
                            if uowid == {}:
                                print("\nTo go further first you need to enter students' UoW ID number"
                                      "for each set of data\n")
                                for i in range(0,len(All_data)):
                                    uid = uid_validation()
                                    uowid[uid] = All_data[i]
                            print_results()
                            
                elif opinion.lower() == 'no': # If user doesn't want to use same set of data, the program reset to defult condition and iterate the loop again
                    count_progress  = 0
                    count_trailer   = 0
                    count_retriever = 0
                    count_exclude   = 0
                    total = 0
                    part_choise = None
                    update_opt = None
                    ckeck_opt = None
                    answer = None
                    option = 'y'
                    login = None
                    All_data = []
                    Text_File = open("SD1_Coursework.txt","w")
                    uowid = {}
                    break
                else:
                    print("Can not read your input, Please ReEnter\n")
                
        print("\n")
    
print_end1 = 'Quiting the Program'
print_end2 = ' Have A Nice Day '
print_end3 = print_end1.center(66)
print_end4 = print_end2.center(62,'*')
print(print_end3,"\n\n",print_end4)
