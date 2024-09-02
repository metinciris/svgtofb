# SVS to Facebook Panorama Image Converter

This Python script (`fbtopanorama.py`) converts SVS files into optimized JPEG images suitable for uploading as panorama images on Facebook. The script resizes, crops, and optimizes the image to meet Facebook's requirements, ensuring that the image is displayed as a flat panorama rather than a 360-degree spherical image.

## Demo

You can see a demo of the output on Facebook:

- [Facebook Demo](https://www.facebook.com/photo/?fbid=971018931702605)
- Screenshot of the Facebook output:  
  ![Facebook Screenshot](https://raw.githubusercontent.com/metinciris/svgtofb/main/screenfb.png)

## Features

- Converts large SVS files into optimized JPEG images.
- Ensures the image is within Facebook's size and dimension limits.
- Crops the image to a 2:1 aspect ratio to suit panorama displays.
- Provides a simple GUI for selecting and processing SVS files.

## Requirements

Make sure you have Python installed on your system. This script requires the following Python packages:

- `tkinter`: For creating the graphical user interface.
- `Pillow`: For image processing.
- `openslide-python`: For reading SVS files.

You can install the required packages using `pip`:

```bash
pip install Pillow openslide-python
```

Note: `tkinter` is usually included with Python, but if it is not installed, you may need to install it separately depending on your operating system.

## Installation

1. Clone this repository or download the `fbtopanorama.py` script.

```bash
git clone https://github.com/metinciris/svgtofb.git
cd svgtofb
```

2. Install the required Python packages:

```bash
pip install Pillow openslide-python
```

3. Make sure you have `openslide` installed on your system. You can download it from [OpenSlide's official website](https://openslide.org/download/).

## Usage

1. Run the script:

```bash
python fbtopanorama.py
```

2. A GUI will open. Click on the "SVS Dosyasını Seç ve İşle" button to select the SVS file you want to convert.

3. The script will process the SVS file, resize it to Facebook's limits, and save the output as a JPEG file in the same directory as the original SVS file. The output file will have `_panoramic_optimized.jpg` appended to its name.

4. Upload the resulting JPEG file to Facebook as a panorama image.

## Notes

- The script automatically optimizes the image to ensure it meets Facebook's maximum dimension (30,000 pixels in any direction) and file size (128,000,000 pixels in total).
- The image will be cropped to a 2:1 aspect ratio to ensure it is displayed correctly as a panorama.

## Contributing

Feel free to submit issues or pull requests if you find any bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



