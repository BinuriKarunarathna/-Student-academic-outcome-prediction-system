pass_m=defer_m=fail_m=id_input=None
final_dic={}
def check_credits():#checking whether credits are integers and in range
    global pass_m, defer_m, fail_m
    while True:
        try:
            pass_m = int(input('Enter your credits at pass: '))#getting credits at pass
        except ValueError:#Handling the error when input is not an integer 
            print('Integer required')
            continue #Getting credits at pass again
        if not(pass_m in [0,20,40,60,80,100,120]):# Checking the range
            print('Out of range')
        else:
            break
    while True:
        try:
            defer_m = int(input('Enter your credits at defer: '))#getting credits at defer
        except ValueError:#Handling the error when input is not an integer 
            print('Integer required')
            continue #Getting credits at pass again
        if not(defer_m in [0,20,40,60,80,100,120]):# Checking the range
            print('Out of range')
        else:
            break
    while True:
        try:
            fail_m = int(input('Enter your credits at fail: '))#getting credits at fail
        except ValueError:#Handling the error when input is not an integer 
            print('Integer required')
            continue #Getting credits at pass again
        if not(fail_m in [0,20,40,60,80,100,120]):# Checking the range
            print('Out of range')
        else:
            break
def check_progress(final_dic,id_input):
    if not(pass_m + defer_m + fail_m == 120):#checking whether total is 120
        print('Total Incorrect')
        check_credits()
        check_progress(final_dic,id_input)
    else:#getting progression outcome
        if pass_m==120:     
            final_dic[id_input]='Progress-'+str(pass_m)+","+str(defer_m)+","+str(fail_m) #Adding credits to the dictionary
        elif pass_m==100:
            final_dic[id_input]='Progress(Module trailer)-'+str(pass_m)+","+str(defer_m)+","+str(fail_m)#Adding credits to the dictionary
        elif pass_m>=40 and pass_m<=80 and fail_m<80:       
            final_dic[id_input]='Module retriever-'+str(pass_m)+","+str(defer_m)+","+str(fail_m)#Adding credits to the dictionary
        elif pass_m==20 and fail_m<80:         
            final_dic[id_input]='Module retriever-'+str(pass_m)+","+str(defer_m)+","+str(fail_m)#Adding credits to the dictionary
        elif pass_m==0 and fail_m<80:           
            final_dic[id_input]='Module retriever-'+str(pass_m)+","+str(defer_m)+","+str(fail_m)#Adding credits to the dictionary
        else:
            final_dic[id_input]='Exclude-'+str(pass_m)+","+str(defer_m)+","+str(fail_m)#Adding credits to the dictionary
   
                
    


