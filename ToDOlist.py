#THIS FUNCTION CREATES TO-DO-LIST
def To_DO_list_Create():

    #w Mode because it will only create File and write
    f=open(f'{NAME}.txt','w')
    f.write(TASKS+'\n')
    f.close()

#THIS FUNCTION UPDATE TO-DO-LIST
def To_Do_list_update():

    #a Mode becuase it will update file
    f=open(f'{NAME}.txt','a')
    f.write(TOBEADDED+'\n')
    f.close()

#THIS FUNCTION PRINT TO-DO-LIST
def Track_Tasks():

    # r Mode because this Function just have to read the file
    f=open(f'{NAME}.txt','r')
    print(f'{NAME}TO-DO-LIST\n',f.read())

while True:
    print('-------------------------------------------------------------------------------------------------')
    choice = input('ENTER 1 IF YOU WANT TO CREATE YOUR TO-DO-LIST\n\n' \
                   'ENTER 2 IF YOU WANT TO UPDATE YOUR LIST\n\n' \
                   'ENTER 3 TO SEE YOUR TO-DO-LIST\n\n'\
                   'ENTER HERE:')

    if choice == '1':
        Name = input('Enter Your Name:\n')
        NAME=Name.upper()
        print("Your TO-DO-LIST has been created \n\n")
        Tasks = input('Enter your First task:')
        TASKS=Tasks.upper()
        To_DO_list_Create()

    if choice == '2':
        TobeAdded_Tasks = input('Enter your Task to be Added in the list:')
        TOBEADDED=TobeAdded_Tasks.upper()
        To_Do_list_update()
    if choice == '3':
        Track_Tasks()


