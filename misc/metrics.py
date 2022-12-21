import numpy as np
from skimage.metrics import structural_similarity as ssim_metric
from skimage.metrics import peak_signal_noise_ratio as psnr_metric

# ref: https://github.com/edenton/svg


class Metric(object):
    """Operates in numpy"""

    def __init__(self):
        self.name = "Metric"

    def compare_mse(self, x1, x2):
        err = np.sum((x1 - x2) ** 2)
        if len(x1) == 4:
            err /= float(x1.shape[0] * x1.shape[1] * x1.shape[2] * x1.shape[3])
        else:
            err /= float(x1.shape[0] * x1.shape[1] * x1.shape[2])
        return err
