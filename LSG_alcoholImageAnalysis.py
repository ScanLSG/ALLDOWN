#####################################################################
# 1. select the ROI in RGB-------------get                          #
# 2. RGB->HSV--------------------------get                          #
# 3. output the ROI :H, S, V-----------get                          #
# 4. plot the diagram------------------                             #
#####################################################################

import cv2
import numpy

# select the any range 
def roi_anyRange(img_path):
    img_org = cv2.imread(img_path)              # load original image

    # select the roi, the function return a rect:(x_min, y_min, w, h)
    roi_range = cv2.selectROI('img_org', img_org, False, False);        
    img_roi = img_org[int(roi_range[1]) : int(roi_range[1]+roi_range[3]), int(roi_range[0]) : int(roi_range[0]+roi_range[2]), :]
    
    cv2.imshow("img_roi", img_roi)                              # show the roi image
    cv2.imwrite("E:\\Code\\Python\\img_roi.jpg", img_roi)       # save the roi image
    
    return img_roi                                              # return the roi image

# convert image to HSV and get h,s,v
def getHSV(img_bgr):
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)                  # Convert the BGR image to HSV
    h, s, v = img_hsv[:, :, 0], img_hsv[:, :, 1], img_hsv[:, :, 2]      # parse HSV

    # calculate the image's mean
    print("the image H:", numpy.mean(h))
    print("the image V:", numpy.mean(v))
    print("the image S:", numpy.mean(s))

# main
def main():
    img_path = "D:\\Code\\Python\\Python\\lisa.jpg"     # the image path 
    img_bgr = roi_anyRange(img_path)            # select the any range
    getHSV(img_bgr)                             # convert image to HSV and get h,s,v

    cv2.waitKey(0)                              # wait exit

if __name__ == '__main__':
    main()