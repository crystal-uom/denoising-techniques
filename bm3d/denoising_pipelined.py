import numpy as np
import matplotlib.pyplot as plt
import bm3d
from skimage import io, img_as_float
import os
import glob
from pathlib import Path
from collections import defaultdict

icip_data = "D:/VIP Cup/Dataset/ICIP training data/"
denoised_data = "D:/VIP Cup/Output dataset/denoised_tiff_data/"
in_path = "D:/VIP Cup/Dataset/ICIP training data/2/RawDataQA-2 (24)/RawDataQA-2-24 (108).tiff"
out_path = "D:/VIP Cup/Results/bm3d library/2-bm3d_sigma_"

tiff_directories = defaultdict(list)
denoised_tiff_count = 0
original_tiff_count = 0

def bm3d_denoise(noisy_image, denoised_image, npsd_sigma = 0.08):

    noisy_oct = img_as_float(io.imread(noisy_image, as_gray=True))
    sigma = npsd_sigma

    bm3d_denoised = bm3d.bm3d(noisy_oct, sigma_psd=sigma, stage_arg=bm3d.BM3DStages.ALL_STAGES)

    plt.imsave(denoised_image, bm3d_denoised, cmap='gray')

def is_tiff_dir(curr_path):
    '''function to check if the current directory having any tiff files'''
    num_tiff = len(glob.glob(os.path.join(curr_path, '*.tiff')))
    return num_tiff

def is_tiff(curr_path):
    '''function to check if the current file is a tiff file or not'''
    if os.path.isfile(curr_path) and (".tiff" in curr_path):
        return True
    else:
        return False
    
def out_path(file, output_dir):
    '''generate output path'''
    base_name = os.path.basename(file)
    case_name = os.path.basename(os.path.dirname(file))
    class_name = os.path.basename(os.path.dirname(os.path.dirname(file)))
    out_path = os.path.join(output_dir,class_name) + "/" + case_name +  "/" + base_name + "_denoised_.tiff"
    return out_path

#convert_tiff_dir_to_nifti(input_path, output_path)

if __name__ == "__main__":

    dataset = glob.iglob(os.path.join(icip_data, '**'), recursive=True)

    for i,file in enumerate(dataset):

        if is_tiff_dir(file):
            current_tiff_count = is_tiff_dir(file)
            tiff_directories[file].append(current_tiff_count)
            print(f"Denoising {len(tiff_directories)}th case {file} ......")
            original_tiff_count += current_tiff_count


        if is_tiff(file):

            #print(file)
            # output directory of the corresponding nifti file
            dest_file = out_path(file, denoised_data)
            new_dir = os.path.dirname(dest_file)
            os.makedirs(new_dir, exist_ok=True)

            #denoising tiffs
            try:
                bm3d_denoise(file, dest_file, npsd_sigma=0.08)
                denoised_tiff_count += 1

            except Exception as e:
                print(e)

    print("\n")
    print("Denoising Completed....")
    print(f"Denoised cases: {len(tiff_directories)}")
    print(f"Denoised tiff images: {denoised_tiff_count}")
    print(f"Original tiff images: {original_tiff_count}")

    