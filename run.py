import faces as detect  # faces.py file is imported here
import faces_train as ft  # face.train.py file is imported here
import register as reg  # register.py  file is imported here

# add user
if_usr_added = False  # flag defined to add user
while True:
    cmd = input("Do you want to register user, yes/no :")

    if cmd.lower() == 'yes':
        reg.run()
        if_usr_added = True
    elif cmd.lower() == 'no':
        break
    else:
        print("enter yes/no only.")

# train model if new users added >>> training phase
while if_usr_added:
    cmd = input("Do you want to train model, yes/no :")

    if cmd.lower() == 'yes':
        ft.run()
        break
    elif cmd.lower() == 'no':
        break
    else:
        print("enter yes/no only.")

# detect faces >>>> final phase-- face detection
detect.run()
