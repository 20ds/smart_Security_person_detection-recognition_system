
Face recognition system ::
face recognition system has been designed which is capable of :
            > registering new Users
            > training the modle for all users
            > detecting the lables(name of user) and the confidance (accuracy)



the programme is saperated into 3 segments :
1> register.py :>(register.py file will be exhecuted in this phase )
                >new user registration would be asked initially

2> faces_train.py : faces_train.py file  will be exhecuted in this phase
                    > this is the training phase , model will be train on all existing users data

3> faces.py : > faces.py file will be exhecuted in this phase
              > this is the detection phase (final phase )


dependencies :
python has been used build the model
python libraries used

> numpy
> Pickle
> pillow
> OpenCv
>


> steps to run the progrmme
1 > unzip the face_recognition file :
2 > open the cmd and select the progrmme directory(path of the file )
3 > execute run.py by using python
           >python run.py
          > registration for new user would be asked : (register.py will be exhecuted in this phase )
                                    >  yes/no :: if yes > new user input would be taken
                                                                    > user name :
                                                                    > user images would be captured by webcam (10 images would be taken)
                                                                         > please click the images by pressing (q)(10 times) on the keyboard or
                                                                           just move to diff angles the images would be captured with a time lapse of .5 sec

                                    >            if no  > model will be directed to the training phase directly
          > user would be asked to train the model :
                                    > yes/no :: if yes > model mil start the training pipeline and detection phase
                                                       > real time ditection would be shown (bounded boxes , names , confidence )

                                                if no  > real time ditection would be shown (bounded boxes , names , confidence )

          > user can exit the detection by pressing (e) on keyboard (frame window would be exit)
