BEFORE SETUP INSTRUCTIONS
    Setup is fairly simple. HOWEVER... if you did not clone this project inside
    of a folder, there will likely be issues later down the line with organization.

    Your folders should look like this:
        'YourFolder/project-vote4us'

    IF YOU DON'T HAVE THIS, I highly reccomend that you put project-vote4us in a
    larger folder.
    


SETUP INSTRUCTIONS

    Navigate into the project-vote4us folder, and there will be two executables,
    along with some other folders and stuff.

    When you run the file, a prompt asking whether you want to use this 

        1) FOR WINDOWS USERS, run the 'Windows_SetupWaldo.bat' file by...
            * Double clicking it in file explorer
            OR
            * Running this command when in the project-vote4us directory
            >   call Windows_SetupWaldo.bat

        2) FOR MAC USERS, run the 'Mac_SetupWaldo.sh' file by...
            * Double clicking it in file explorer
            OR
            * Running this command when in the project-vote4us directory
            >   ./Mac_SetupWaldo.sh

        After this, you should be done. If you have issues, lmk.



RUNNING WALDO INSTRUCTIONS
    There are two things that we can run with What's Waldo. You can either run the
    What's Waldo program, or run the training model program.

    1) RUNNING WHAT'S WALDO
        *** (not implemented fully) ***
        First navigate to the directory, 'project-vote4us/MLTest'
        Then run the python script, 'RunModels.py' by doing the following:
            * click the run button if you're using something like VSCode
            * if you try to run from terminal, i'm not sure that it will run correctly,
              because this requires the .venv path to '.venv/Scripts/python.exe' run with
              all the neccessary libraries.
    
    2) TRAINING WALDO
        This has been made fairly simple to execute I think.

        * run the file in MLTest called RunModels.py
        * this will prompt you with several options. You will chose the 't' option, 
            by entering 't' and pressing enter
        * then you specify how many epochs you want. Enter a number and the script will
          run


        TO ADD NEW TRAINING DATA

        If you are confused, or having issues, Owen is the expert in this, but you could
        contact either me or him.

        First navigate to the directory in 'project-vote4us/data'. This contains the data
        that the current model was trained on.
        
        To add new data, first make sure of the following:
            * the images and labels that you use must line up in size and names. If not,
              the model will not work correctly
            * navigate into the 'images/train' folder and put your images
            * navigate into the 'labels/train' folder and put the corresponding labels

        Run the 'RunModels.py' file, and it should be the same as usual, entering 't' and\
        then the number of epochs.

        The results are output into a file called 'runs/detec' that will be in the same
        space as 'project-vote4us', NOT INSIDE 'project-vote4us'