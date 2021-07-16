import cv2
import numpy as np
from matplotlib import pyplot as plt
from numpy.core.fromnumeric import mean
from skimage.restoration import estimate_sigma

class PointOperations:
    @staticmethod
    def arithmetic_operators(image,rows,cols,operator,const=128):
        for i in range(rows):
            for j in range(cols):
                pixel = image[i,j]
                if operator == "+":
                    newPixel = pixel + const
                elif operator == "-":
                    newPixel = pixel - const
                elif operator == "*":
                    newPixel = pixel * const
                elif operator == "/": 
                    newPixel = pixel / const
                elif operator == "complement":
                    newPixel = 255 - pixel
                else:
                    raise TypeError("in valid operation")
                if newPixel > 255 :
                    image[i,j] = 255
                elif newPixel < 0 :
                    image[i,j] = 0
                else:
                    image[i,j]= newPixel
    
    @staticmethod
    def low_constract_operation(img,rows,cols,operation,const):
        newPixel = None
        for i in range(rows):
            for j in range(cols):
                pixel = img[i,j]
                if operation == "*":
                    newPixel = pixel * const
                elif operation == "**":
                    newPixel = pixel ** const
                if newPixel > 255:
                    img[i, j] = 255
                elif newPixel < 0:
                    img[i, j] = 0
                else:
                    img[i, j] = newPixel
    @staticmethod
    def stretching_function(img,rows,cols,low_pixel,high_pixel):
        for i in range(rows):
            for j in range(cols):
                pixel = img[i,j]
                if pixel <= low_pixel:
                    img[i,j]= 0
                elif high_pixel <= pixel:
                    img[i,j] = 255
                elif pixel >= low_pixel and pixel <= high_pixel:
                    img[i,j]= 255*((pixel-low_pixel)/(high_pixel-low_pixel))
    @staticmethod
    def addConstToBlueChannele(blue,blue_rows,blue_cols):
        for i in range(blue_rows):
            for j in range(blue_cols):
                pixel = blue[i,j]
                newPixel = pixel + 128
                if newPixel > 255:
                    blue[i, j] = 255
                elif newPixel < 0:
                    blue[i, j] = 0
                else:
                    blue[i, j] = newPixel
        return blue
    
    @staticmethod
    def outlier_method(image,size):
        D = 0.2
        # size = int(input('please enter the size of mask : '))
        step = int((size-1)/2)
        rows,cols = image.shape
        for i in range(rows):
            for j in range(cols):
                p = image[i,j]
                neighbour=[]
                for x in range(i-step, i+step+1):
                    for y in range(j-step, j+step+1):
                        if x < 0 or y < 0 or x > rows-1 or y > cols-1:
                            pass
                        else:
                            neighbour.append(image[x,y])
                m = mean(neighbour)
                if abs(p-m) > D:
                    image[i,j] = m
    @staticmethod
    def Adaptive(image,size):
        step = int((size-1)/2)
        Nsd = estimate_sigma(image , multichannel= True , average_sigmas=True)
        NV = Nsd**2
        rows,cols = image.shape
        for i in range(rows):
            for j in range(cols):
                p = image[i,j]
                neighbour=[]
                for x in range(i-step, i+step+1):
                    for y in range(j-step, j+step+1):
                        if x < 0 or y < 0 or x > rows-1 or y > cols-1:
                            pass
                        else:
                            neighbour.append(image[x,y])
                m = mean(neighbour)
                v = np.var(neighbour)
                image[i,j]= m +(v/(v+NV))*(p-m)