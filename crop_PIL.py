from PIL import Image
from PIL import ImageOps

im = Image.open(new_image_path)

crop_image = im.copy()
crop_image = np.array(crop_image)
crop_img = crop_image[top:bottom, left:right]
crop_img = Image.fromarray(crop_img)
crop_img = crop_img.convert('RGB')


im.save("test_cropped.jpg",quality=100)
