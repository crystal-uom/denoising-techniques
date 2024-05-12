import numpy as np
import matplotlib.pyplot as plt
from skimage.restoration import (denoise_tv_chambolle, estimate_sigma)
from skimage import io, img_as_float
import os

in_path = "D:/VIP Cup/Dataset/ICIP training data/2/RawDataQA-2 (24)/RawDataQA-2-24 (108).tiff"
out_path = "D:/VIP Cup/Results/total variation/total variation_"

noisy_oct = img_as_float(io.imread(in_path, as_gray=True))

w = 0.075

save_path = out_path + f"{w:.2f}"  + ".tiff"

tv_denoised = denoise_tv_chambolle(noisy_oct, weight=w)

plt.imsave(save_path, tv_denoised, cmap='gray')


