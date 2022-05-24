from data_loader.data_loader import DataLoader
from initializer.cameras_corregistration import CamerasCorregistrator
from utils.utils import get_logger
from utils.plot_utils import pixels_select_click

logger = get_logger(name="select_signatures")

def main(cfg):
    data_loader_cfg = cfg.data_loaders.data_loader
    if not data_loader_cfg.corregistrate_dir_name:
        logger.warning("No data directory provided to perform corregistration")
        return
    if not data_loader_cfg.data_sources.path_ending_camera1 and \
        not data_loader_cfg.data_sources.path_ending_camera2:
        logger.warning("No camera paths endings provided to perform corregistration")
        return

    data_loader = DataLoader(cfg)
    data_loader.change_dir("corregistrate").load_images()

    images_cam1 = data_loader.images.cam1
    images_cam2 = data_loader.images.cam2
    image_cam1 = images_cam1[cfg.image_idx]
    image_cam2 = images_cam2[cfg.image_idx]

    selected_pixels_cam1 = pixels_select_click(image_cam1)
    selected_pixels_cam2 = pixels_select_click(image_cam2)

    corregistrator = CamerasCorregistrator(cfg)
    corregistrator.align(selected_pixels_cam2, selected_pixels_cam1,
                         plot_progress=True, points_ordered=True)
    corregistrator.save_params()






