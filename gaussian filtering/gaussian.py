import skimage
from skimage.metrics import peak_signal_noise_ratio
import matplotlib.pyplot as plt
from skimage import io
from scipy import ndimage as nd
import os

in_path2 = "D:/VIP Cup/Dataset/ICIP training data/2/RawDataQA-2 (24)/RawDataQA-2-24 (108).tiff"
out_path = "D:/VIP Cup/Results/gaussian results/gaussian_sigma_4 - " + os.path.basename(in_path2)
noisy_img = skimage.img_as_float(io.imread(in_path2))

gaussian_img = nd.gaussian_filter(noisy_img, sigma =3)
plt.imshow(gaussian_img, cmap='gray')
plt.imsave(out_path, gaussian_img, cmap='gray')