import cv2

cv2_img = cv2.imread(new_image_path)

top = max(0, top)
left = max(0, left)
bottom = min(im_height, bottom)
right = min(im_width, right)



img = cv2_img[top:bottom, left:right]

im_path = "result_images/" + datetime_name + "_before_drawing"+ str(xx) + ".png"
cv2.imwrite(im_path,img)
