from lpips.lpips import LPIPS
import jittor as jt
import jittor.transform as transform
from PIL import Image

loss_fn = LPIPS(net='alex', spatial=False)
#loss_fn = LPIPS(net='vgg', spatial=False)
#loss_fn = LPIPS(net='squeeze', spatial=False)

img_size = 64
transform_image = transform.Compose([
        transform.Resize(size = img_size),
        transform.ImageNormalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])

def read_img(path):
    img = Image.open(path).convert('RGB')
    img = transform_image(img)
    img = jt.array(img)
    img = img.unsqueeze(0)
    return img
ex_ref = read_img('./imgs/ex_ref.png')
ex_p0 = read_img('./imgs/ex_p0.png')
ex_p1 = read_img('./imgs/ex_p1.png')

ex_d0 = loss_fn.execute(ex_ref,ex_p0)
ex_d1 = loss_fn.execute(ex_ref,ex_p1)

print('Distances: (%.8f, %.8f)'%(ex_d0, ex_d1))

