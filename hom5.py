#!/usr/bin/env python3
FILENAME="data_txt "
a=0
b=0
keep_running=True
while keep_running:
    print(""" a = {}  b = {}
    set(a) --> to input a new value for a
    set(b) --> to input a new value for b
    (s)ave --> save a and b data to data_txt {}
    (l)oad --> load a and b data from data_txt {}
    (Q)uit --> quit the program
    """.format(a,b,FILENAME,FILENAME))
    choice=str(input("enter your choice: ")).lower()

    if choice=='a':
        a = int(input("enter a new value for a: "))
    elif choice=='b':
        b = int(input("enter a new value for b: "))
    elif choice=='s':
         with open(FILENAME,'w') as f:
            f.write('{}\n{}\n'.format(a,b))

            print("saved successfully! ")
    elif choice=='l':
       with open(FILENAME) as f:
        a=int(f.readline())
        b=int(f.readline())

    elif choice == 'q':
        keep_running = False
    else:
        print("error: invalid choice.")
print("goodbye")