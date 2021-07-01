# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#############################################################################################
## Importing Significant Library 

import os                          ## import os Help you to use system app and give you permission to use apps without "Sudo" Command
from glob import glob              ## Use it for change on directorys
import cv2                         ## Image proccessing library 
import time                       ## use it for sleep and delay
import webbrowser                 ## fined Defulat web-browser
import numpy as np                ## use it for opencv library
from os import path               ## get path which should be changed without administor permission
from glob import glob

#######################
###########################
###############################

  
def find_ext(dr, ext):                                  ## function which allowed you to get all format be need
    return glob(path.join(dr,"*.{}".format(ext)))



#######################################################
"""
All of the code should be inside unlimited loop 

Which gives you this option to run your code permenently

to have real time result.
"""
##
while True:                                 
    arr = os.listdir("/media/mehdi")                             ## gives you the list of Folders which are inside the current directory.
    print(len(arr))                                             ## print The name of directory
    if len(arr) is 0:                                           ## check if there is no Flash device connected to system
        print("No device connected ")                           ## gives warning that there is no device
        time.sleep(3)
        
    if len(arr) > 0:                                            ## if there was any flash derive will start to read files
        
        print(" Please wait ... ... ... " )
        print()
        print()
        print()
        arr1=os.chdir("/media/mehdi/"+str(arr[0]))               ## change main python code Directory
        arr2 = os.listdir("/media/mehdi/"+str(arr[0]))           ## Gives you directory files list
        time.sleep(5)
        print(arr2);
        print(arr[0]);
        print()
        print()
        print()
        print("Here you go ... Flash mounted ")                 ## warning when you pluged the flash
        print()
        print()
        print()
        time.sleep(3)
        List_pdf_files = []                                     ## make zero member list for generating list
        List_Image_files = []                                   ## same
        
        List_pdf_files = find_ext(".","pdf")                    ## seprate pdf files
        print()
        print()
        print()
        List_JPG_Image_files = find_ext(".","jpg")              ## seprates jpg files 
        print()
        print()
        print()
        List_PNG_Image_files = find_ext(".","png")              ## seprate png files
        print()
        print()
        print()
        print(List_JPG_Image_files)                             
        print()
        print()
        print()
        print("\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*")
        print()
        print()
        print()
        print(List_PNG_Image_files)
        print()
        print()
        print()
        print("\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*")
        print()
        print()
        print()      
        print(List_pdf_files)
        my_array1 = np.asarray(List_JPG_Image_files)        ## change the characters to numbers for calls
        my_array2 = np.asarray(List_PNG_Image_files)
        my_array3 = np.asanyarray(List_pdf_files)
        
        """
        Infiniti loop for entering Desired Files
        
        """
        while True:
        
            des = input("Enter desire file to open : ") ## function for reciveing name of file
        
            """
            image read
            """
            pic= cv2.imread(str(des))                   ## use imread function to read images 
            if pic is None:
                    pass
                
            if not pic is None:
                pic=cv2.resize(pic,(640,480))           ## rescale image to show in small window 
                cv2.imshow("Frame",pic)
                cv2.waitKey(2000)
                while True:
                    choise=input("You wanna close the Pic ? (y/n) ")
                    if choise == 'n':
                        continue
                    if choise == 'y':
                        cv2.destroyAllWindows()         ## close pictures window
                        break
                    else:
                        print('invalid input')
            """
            end of image call
            """
################################################################################################
            """
            pdf read 
            """
            for i in List_pdf_files:
                if './'+str(des)+".pdf" == i :
                    webbrowser.open_new(str(des)+'.pdf')
            
            """
            end of pdf call
            """
################################################################################################

            answer = input('you wanna unpluge flash ? (y/n): ') ## ask you to countinue
    
            if answer == 'y':
                  
                  break 
            elif answer == 'n':
                   continue
            else:
                   print ('Invalid input.')
                    
###################################################################################################
                
            
            cv2.waitKey(0)

cv2.destroyAllWindows()
###################################################################################################
"""
The End

"""
