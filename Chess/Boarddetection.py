import cv2
import numpy as np
import os

class BoardDetection:
    def __init__(self):
        self.og_img = None
        self.processing_i
        self.scale_percent = 75

    def resize(self):
        # resizes the image so that its easier to work with, computationally faster
        # we resize the image to 20% of the original size
        WIDTH = int(self.processing_i.shape[1] * self.scale_percent / 100)
        HEIGHT = int(self.processing_i.shape[0] * self.scale_percent / 100)
        SCALED_DIMENSION = (WIDTH, HEIGHT)
        
        # resize image
        self.processing_i= cv2.resize(self.processing_i, SCALED_DIMENSION, interpolation = cv2.INTER_AREA)


    def mask_to_remove_white_spots(self):

        pass
        

    def find_chessboard_contours(self):
        # finds the boarder of the chessboard itself
        threshold_value = 140
        contrast = 2
        brightness = -100
        
        self.processing_i = cv2.convertScaleAbs(self.processing_i, alpha = contrast, beta = brightness)
        #self.processing_img = cv2.GaussianBlur(self.processing_img, (5,5), 0)
        #self.processing_img = cv2.medianBlur(self.processing_img, 1)

        self.processing_i_output("changed brightness",1)
        self.processing_i = cv2.threshold(self.processing_i, threshold_value, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
        self. = cv2.inpaint(self.og_img, self.processing_i, 5, cv2.INPAINT_TELEA)
        
    

       
        #self.canny_and_hough_detection
        

    def get_chessboard_corners(self):
        # gets the chessboards 4 corners
        pass


    def shift_perspective(self):
        # we then shift the perspective of the image such that it is a birds eye view of it 
        pass



    def canny_and_hough_detection(self):
        pass


    def find_intersection_points(self):
        pass



    def img_output(self,txt,opt):
        # this will output the image
        if opt == 1:
            cv2.imshow(txt, self.processing_im)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            cv2.imshow(txt, self.og_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()





if __name__ == '__main__':




    # we call our class thsat will contain methods that will be executed on to our images
    detect = BoardDetection()

    # using os we are looping through a directory of images of a chessboard that will be used to see if the methpds of the image processing work
    path = r"C:\Users\Sanju\OneDrive\Documents\My_Coding_Files\chess\chess_board_imgs"
    file_type = '.jpg'

    for filename in os.listdir(path=path):
        #this is to make thsat  we only lopp throug the images  which in jpg form
        if filename.endswith(file_type):
            
            detect.og_img = detect.img = cv2.imread(f"{path}/{filename}")
            detect.img_output("Original image",2)

            detect.img = cv2.cvtColor(detect.img,cv2.COLOR_RGB2GRAY)
            #detect.img_output("original")
            detect.resize()
            detect.find_chessboard_contours()
            detect.img_output("threshbinary",1)
            
    
    
