# I declare that my work contains no examples of misconduct,such as plagiarism,or collusion.Any code taken from other sources is referenced within my code solution.
# Student ID:w1957468
# Date      :01.11.2022
pass_m=defer_m=fail_m=None     #Assigning variables to None
count_progress=count_not_progress_retriever=count_excluded=count_progress_trailer=0 #Assigning variables to 0
count_progress_l=[]            #Empty lists Initialization
count_not_progress_retriever_l=[]
count_excluded_l=[]
count_progress_trailer_l=[]
def check_credits():           #checking whether credits are integers and in range
    global pass_m, defer_m, fail_m
    while True:
        try:
            pass_m = int(input('Enter your credits at pass: '))#getting credits at pass
        except ValueError:
            print('Integer required')#Handling the error when input is not an integer 
            continue #Getting credits at pass again
        if not(pass_m in [0,20,40,60,80,100,120]): # Checking the range
            print('Out of range')
        else:
            break 
    while True:
        try:
            defer_m = int(input('Enter your credits at defer: '))#getting credits at defer
        except ValueError:
            print('Integer required')#Handling the error when input is not an integer 
            continue
        if not(defer_m in [0,20,40,60,80,100,120]): # Checking the range
            print('Out of range')
        else:
            break
    while True:
        try:
            fail_m = int(input('Enter your credits at fail: '))#getting credits at fail
        except ValueError:
            print('Integer required')#Handling the error when input is not an integer 
            continue
        if not(fail_m in [0,20,40,60,80,100,120]): # Checking the range
            print('Out of range')
        else:
            break
def check_progress(): #checking the total and progression outcome
    global another_set,count_progress,count_not_progress_retriever,count_excluded,count_progress_trailer
    if not(pass_m + defer_m + fail_m == 120):#checking whether the total is 120
        print('Total Incorrect')
        check_credits()
        check_progress()
    else:#getting progression outcome
            if pass_m==120:
                print("Progress")
                count_progress+=1#counting number of progresses
                count_progress_l.extend([pass_m,defer_m,fail_m])#Adding credits to count_progres_l
            elif pass_m==100:
                print("Progress(Module trailer)")
                count_progress_trailer+=1   #counting number of module trailers
                count_progress_trailer_l.extend([pass_m,defer_m,fail_m])#Adding credits to count_progres_l  
            elif pass_m>=40 and pass_m<=80 and fail_m<80:
                print("Module retriever")
                count_not_progress_retriever+=1  #counting number of module retrievers
                count_not_progress_retriever_l.extend([pass_m,defer_m,fail_m])#Adding credits to count_progres_l                
            elif pass_m==20 and fail_m<80:
                print("Module retriever")
                count_not_progress_retriever+=1   #counting number of module retrievers
                count_not_progress_retriever_l.extend([pass_m,defer_m,fail_m])#Adding credits to count_progres_l         
            elif pass_m==0 and fail_m<80:
                print("Module retriever")
                count_not_progress_retriever+=1   #counting number of module retrievers
                count_not_progress_retriever_l.extend([pass_m,defer_m,fail_m]) #Adding credits to count_progres_l      
            else:
                print("Exclude")
                count_excluded+=1  #counting number of excluded
                count_excluded_l.extend([pass_m,defer_m,fail_m])#Adding credits to count_progres_l
f=open('cwfile.txt','w')#Openning a file to write                   
check_credits()
check_progress()
def divide_lists(l,n):#divide the list in to another lists
    for i in range(0, len(l), n):
        yield l[i:i + n]
while True:
    print('Would you like to enter another set of data?')#Asking to stop or continue data entering
    another_set=input('Enter "y" for yes or "q" to quit and view results: ')
    if another_set=='y': #Getting another data set
        check_credits() 
        check_progress()
    elif another_set=='q':
        print('----------------------------------------------------------------------------------------------------------------')#Histogram
        print('Progress ',count_progress,' :','*'*count_progress)#Presenting number of progresses by asterisks 
        print('Trailer ',count_progress_trailer,'  :','*'*count_progress_trailer)#Presenting number of trailers by asterisks 
        print('Retriever ',count_not_progress_retriever,':','*'*count_not_progress_retriever)#Presenting number of retrievers by asterisks 
        print('Exclude ',count_excluded,'  :','*'*count_excluded)#Presenting number of exclude outcomes by asterisks 
        print(count_progress+count_progress_trailer+count_not_progress_retriever+count_excluded,'outcomes in total')#Presenting number of outcomes 
        print('----------------------------------------------------------------------------------------------------------------')#list extension
        progress_slice=list(divide_lists(count_progress_l,3))#Dividing count_progress list into chunks of size 3
        retriever_slice=list(divide_lists(count_not_progress_retriever_l,3))#Dividing count_not_progress_retriver list into chunks of size 3
        excluded_slice=list(divide_lists(count_excluded_l,3))#Dividing count_excluded list into chunks of size 3
        trailer_slice=list(divide_lists(count_progress_trailer_l,3))#Dividing count_progress_trailer list into chunks of size 3
        for i in progress_slice: #Printing progress outcomes with credits at pass,defer,fail and writing to a file
            print('Progress',end=':'),f.write('Progress:')
            print(*i,sep=","),f.write(str(i).replace('[','').replace(']','')+'\n')
        for i in retriever_slice:#Printing retriever outcomes with credits at pass,defer,fail and writing to a file
            print('Module retriever',end=':'),f.write('Module retriever:')
            print(*i,sep=","),f.write(str(i).replace('[','').replace(']','')+'\n')
        for i in excluded_slice: #Printing excluded outcomes with credits at pass,defer,fail and writing to a file
            print('Exclude',end=':'),f.write('Exclude:')
            print(*i,sep=","),f.write(str(i).replace('[','').replace(']','')+'\n')      
        for i in trailer_slice:  #Printing trailer outcomes with credits at pass,defer,fail and writing to a file
            print('Progress (module trailer)',end=':'),f.write('Progress (module trailer):')
            print(*i,sep=","),f.write(str(i).replace('[','').replace(']','')+'\n')
        break
    else:
        print('You have entered an invalid letter') #Display when user enter another letter except y,q    
f.close()#Closing the file after writing
print('----------------------------------------------------------------------------------------------------------------') #Text file extension
f=open('cwfile.txt','r') #Openning the file for reading it and printing it  
print(f.read())
f.close() # Closing the file after reading
    
        


   
                
    

