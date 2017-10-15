'''
isey run karo toh pro log dikhte hai
'''

import cv2


def show_webcam(mirror=False):
  cam = cv2.VideoCapture(0)
  while True:
    ret_val, img = cam.read()
    if mirror:
        img = cv2.flip(img, 1)
        #cv2.circle(img, (200, 200), 30 , (0,0,255), -1)
        #cv2.circle(img, (300, 200), 30 , (0,0,255), -1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'PRO LOG',(10,400), font, 4,(255,255,255),4,cv2.LINE_AA)
        
    cv2.imshow('my webcam', img)
    if cv2.waitKey(1) == 27: 
        break  # esc to quit
			
  cv2.destroyAllWindows()

def main():
	show_webcam(mirror=True)

if __name__ == '__main__':
	main()
