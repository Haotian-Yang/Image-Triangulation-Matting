## CSC320 Winter 2019 
## Assignment 1
## (c) Kyros Kutulakos
##
## DISTRIBUTION OF THIS CODE ANY FORM (ELECTRONIC OR OTHERWISE,
## AS-IS, MODIFIED OR IN PART), WITHOUT PRIOR WRITTEN AUTHORIZATION 
## BY THE INSTRUCTOR IS STRICTLY PROHIBITED. VIOLATION OF THIS 
## POLICY WILL BE CONSIDERED AN ACT OF ACADEMIC DISHONESTY

##
## DO NOT MODIFY THIS FILE ANYWHERE EXCEPT WHERE INDICATED
##

# import basic packages
import numpy as np
import scipy.linalg as sp
import cv2 as cv

# If you wish to import any additional modules
# or define other utility functions, 
# include them here

#########################################
## PLACE YOUR CODE BETWEEN THESE LINES ##
#########################################


#########################################

#
# The Matting Class
#
# This class contains all methods required for implementing 
# triangulation matting and image compositing. Description of
# the individual methods is given below.
#
# To run triangulation matting you must create an instance
# of this class. See function run() in file run.py for an
# example of how it is called
#
class Matting:
    #
    # The class constructor
    #
    # When called, it creates a private dictionary object that acts as a container
    # for all input and all output images of the triangulation matting and compositing 
    # algorithms. These images are initialized to None and populated/accessed by 
    # calling the the readImage(), writeImage(), useTriangulationResults() methods.
    # See function run() in run.py for examples of their usage.
    #
    def __init__(self):
        self._images = { 
            'backA': None, 
            'backB': None, 
            'compA': None, 
            'compB': None, 
            'colOut': None,
            'alphaOut': None, 
            'backIn': None, 
            'colIn': None, 
            'alphaIn': None, 
            'compOut': None, 
        }

    # Return a dictionary containing the input arguments of the
    # triangulation matting algorithm, along with a brief explanation
    # and a default filename (or None)
    # This dictionary is used to create the command-line arguments
    # required by the algorithm. See the parseArguments() function
    # run.py for examples of its usage
    def mattingInput(self): 
        return {
            'backA':{'msg':'Image filename for Background A Color','default':None},
            'backB':{'msg':'Image filename for Background B Color','default':None},
            'compA':{'msg':'Image filename for Composite A Color','default':None},
            'compB':{'msg':'Image filename for Composite B Color','default':None},
        }
    # Same as above, but for the output arguments
    def mattingOutput(self): 
        return {
            'colOut':{'msg':'Image filename for Object Color','default':['color.tif']},
            'alphaOut':{'msg':'Image filename for Object Alpha','default':['alpha.tif']}
        }
    def compositingInput(self):
        return {
            'colIn':{'msg':'Image filename for Object Color','default':None},
            'alphaIn':{'msg':'Image filename for Object Alpha','default':None},
            'backIn':{'msg':'Image filename for Background Color','default':None},
        }
    def compositingOutput(self):
        return {
            'compOut':{'msg':'Image filename for Composite Color','default':['comp.tif']},
        }
    
    # Copy the output of the triangulation matting algorithm (i.e., the 
    # object Color and object Alpha images) to the images holding the input
    # to the compositing algorithm. This way we can do compositing right after
    # triangulation matting without having to save the object Color and object
    # Alpha images to disk. This routine is NOT used for partA of the assignment.
    def useTriangulationResults(self):
        if (self._images['colOut'] is not None) and (self._images['alphaOut'] is not None):
            self._images['colIn'] = self._images['colOut'].copy()
            self._images['alphaIn'] = self._images['alphaOut'].copy()

    # If you wish to create additional methods for the 
    # Matting class, include them here

    #########################################
    ## PLACE YOUR CODE BETWEEN THESE LINES ##
    #########################################

    #########################################
            
    # Use OpenCV to read an image from a file and copy its contents to the 
    # matting instance's private dictionary object. The key 
    # specifies the image variable and should be one of the
    # strings in lines 54-63. See run() in run.py for examples
    #
    # The routine should return True if it succeeded. If it did not, it should
    # leave the matting instance's dictionary entry unaffected and return
    # False, along with an error message
    def readImage(self, fileName, key):
        success = False
        msg = 'Placeholder'

        #########################################
        ## PLACE YOUR CODE BETWEEN THESE LINES ##
        #########################################
        try:
            img = cv.imread(fileName)
        except Exception as ex:
            msg = ex.message
        else:
            self._images[key] = img
            success = True
            msg = 'Success'
        #########################################
        return success, msg

    # Use OpenCV to write to a file an image that is contained in the 
    # instance's private dictionary. The key specifies the which image
    # should be written and should be one of the strings in lines 54-63. 
    # See run() in run.py for usage examples
    #
    # The routine should return True if it succeeded. If it did not, it should
    # return False, along with an error message
    def writeImage(self, fileName, key):
        success = False
        msg = 'Placeholder'

        #########################################
        ## PLACE YOUR CODE BETWEEN THESE LINES ##
        #########################################
        try:
            cv.imwrite(fileName, self._images[key])
        except Exception as ex:
            msg = ex.message
        else:
            success = True
            msg = 'Success'

        #########################################
        return success, msg

    # Method implementing the triangulation matting algorithm. The
    # method takes its inputs/outputs from the method's private dictionary 
    # ojbect. 
    def triangulationMatting(self):
        """
success, errorMessage = triangulationMatting(self)
        
        Perform triangulation matting. Returns True if successful (ie.
        all inputs and outputs are valid) and False if not. When success=False
        an explanatory error message should be returned.
        """

        success = False
        msg = 'Placeholder'

        #########################################
        ## PLACE YOUR CODE BETWEEN THESE LINES ##
        #########################################
        try:
            compA = self._images['compA']
            backA = self._images['backA']
            compB = self._images['compB']
            backB = self._images['backB']
            cA_b, cA_g, cA_r = cv.split(compA)
            bA_b, bA_g, bA_r = cv.split(backA)
            cB_b, cB_g, cB_r = cv.split(compB)
            bB_b, bB_g, bB_r = cv.split(backB)
            row = len(compA)
            column = len(compA[0])
            alphOut = np.zeros(compA.shape)
            colOut = np.zeros(compA.shape)
            for r in range(0,row):
                for c in range(0,column):
                    b = np.array([int(cA_b[r][c]) - int(bA_b[r][c]), 
                                int(cA_g[r][c]) - int(bA_g[r][c]), 
                                int(cA_r[r][c]) - int(bA_r[r][c]), 
                                int(cB_b[r][c]) - int(bB_b[r][c]), 
                                int(cB_g[r][c]) - int(bB_g[r][c]), 
                                int(cB_r[r][c]) - int(bB_r[r][c])])
                    A = np.array([[1,0,0,-int(bA_b[r][c])],
                                [0,1,0,-int(bA_g[r][c])],
                                [0,0,1,-int(bA_r[r][c])],
                                [1,0,0,-int(bB_b[r][c])],
                                [0,1,0,-int(bB_g[r][c])],
                                [0,0,1,-int(bB_r[r][c])]])
                    x = np.clip(np.linalg.pinv(A).dot(b),0,255)
                    # print(x)
                    colOut[r,c] = np.array([x[0], x[1], x[2]])
                    # colOut[r,c] = np.array(x[0], x[1], x[2])
                    alphOut[r,c] = np.array([(255 * x[3]), (255 * x[3]), (255 * x[3])])
            self._images['alphaOut'] = alphOut
            self._images['colOut'] = colOut
        except Exception as ex:
            msg = ex
        else:
            success = True
            msg = 'Success'

        #########################################

        return success, msg

        
    def createComposite(self):
        """
success, errorMessage = createComposite(self)
        
        Perform compositing. Returns True if successful (ie.
        all inputs and outputs are valid) and False if not. When success=False
        an explanatory error message should be returned.
"""

        success = False
        msg = 'Placeholder'

        #########################################
        ## PLACE YOUR CODE BETWEEN THESE LINES ##
        #########################################
        try:
            alphaIn = self._images['alphaIn']
            colIn = self._images['colIn']
            backIn = self._images['backIn']

            compOut = np.zeros(backIn.shape)
            row = len(backIn)
            column = len(backIn[0])
            for r in range(0, row):
                for c in range(0, column):
                    a = alphaIn[r][c][0]/255.0
                    compOut_bgr = colIn[r][c] + ((1-a) * backIn[r][c])
                    compOut[r,c] = np.array(compOut_bgr)
            self._images['compOut'] = compOut
        except Exception as ex:
            msg = ex
        else:
            success = True
            msg = 'Success'



        #########################################

        return True, msg


