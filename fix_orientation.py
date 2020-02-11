from PIL import Image
Import cv2 

image_path = "images/1.jpg"

input_img = Image.open(image_path).convert('RGB') 


#fix orientation
if hasattr(input_img, '_getexif'):
    orientation = 0x0112
    exif = input_img._getexif()
    if exif is not None:
        orientation = exif[orientation]
        rotations = {
            3: Image.ROTATE_180,
            6: Image.ROTATE_270,
            8: Image.ROTATE_90
        }
        if orientation in rotations:
            input_img= input_img.transpose(rotations[orientation])
            




image = cv2.cvtColor(np.array(input_img), cv2.COLOR_RGB2BGR)
