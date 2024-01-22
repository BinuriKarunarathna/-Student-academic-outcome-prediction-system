pass_m=defer_m=fail_m=id_input=None   #Assigning variables to None
import code_parts as c 
final_dic={} #Empty dictionary initialization
def check_id():
    while True:
        id_input=input('Enter your ID: ')#Getting ID from the user
        if id_input[0]=='w' and len(id_input)==8 and id_input[1:8].isnumeric():
            c.check_credits() #calling functions in that imported file
            c.check_progress(final_dic,id_input)
            break
        else:
            print('Invalid ID')
check_id()
while True:
    print('Would you like to enter another set of data?')#Asking to stop or continue data entering
    another_set=input('Enter "y" for yes or "q" to quit and view results: ')
    if another_set=='y':#Getting data again
        check_id()
    elif another_set=='q': #Printing the dictionary
        print(str(final_dic).replace('{','').replace('}','').replace("'",""))
        break        
    else:
        print('you have entered an invalid letter') # display when user enter another letter except y,q

    







        


   
                
    



