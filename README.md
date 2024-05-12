# denoising-techniques
A collection of denoising technique experimenting to denoise OCT B-Scans. Includes conventional and modern methods.

## Conventional Methods

### 1. Wavelet Transform & Wavelet thresholding
[Devnith] Currently working on wavelet transform based denoising methods using MATLAB and Python.

### 2. BM3D

Old approach: [Nadun & Ravindu] Used the implementation by Chihao Zhang at "https://github.com/ChihaoZhang/BM3D".

Latest approach: [Nadun] Used the bm3d python library based on original bm3d paper.

#### BM3D Comparison

<p align="center">
<img src="bm3d/bm3d_results.png" alt="Initial Prototype" width="600"/>
</p>


### 3. SVD Thresholding
[Devnith] Tested SVD truncation and got positive results. Working on finding the optimal threhold or using soft thresholding. Literature is mentioned in the pdfs.

#### SVD-HT Comparison

Following comparison shows the noise level improvement
<p align="center">
<img src="svd/svd.jpg" alt="SVD_comp" width="400"/>
</p>

Following series of SVD reconstruction shows suppression of noise with truncated sigma values. 
<p align="center">
<img src="svd/svd_process.jpg" alt="SVD_comp" width="400"/>
</p>

### 4. Gaussian Filtering
[Nadun] simple gaussian filtering to filter out the gaussian noise distributions

#### Gaussian filtering comparison

<p align="center">
<img src="gaussian filtering/gaussian_filter_comparison.png" alt="Initial Prototype" width="600"/>
</p>

### 5. Anisotropic Diffusion

[Sasika] Anisotropic Diffusion results for both 2 formulae

- Notebook : [Google Colab](https://colab.research.google.com/drive/1igHUi8mmSP5KIeDVMj8qd3Wg7tTggsV5?usp=sharing)

<p align="center">
<img src="anisotropic_diffusion/Anisotropic diffusion results.png" alt="Initial Prototype" />
</p>

### 6. Total Variation

[Nadun] Total bariation method

<p align="center">
<img src="total_variation/total_variation_results.PNG" alt="tv" width="500"/>
</p>




