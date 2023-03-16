@echo off

REM Install dependencies
pip install -U pyserial
pip install -U Pillow
pip install -U numpy
pip install -U opencv-python
pip install -U tensorflow

REM Install/update pycoral
pip install --upgrade pycoral

REM Download and install Edge TPU runtime and API
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg ^
  | sudo apt-key add -
echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" ^
  | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
sudo apt-get update
sudo apt-get install edgetpu

REM Test the USB accelerator
edgetpu_detect

REM Run a sample script using the USB accelerator
cd C:\Program Files (x86)\Google\Edge TPU Compiler\pycoral\examples
python classify_image.py ^
--model models/mobilenet_v2_1.0_224_inat_bird_quant_edgetpu.tflite ^
--labels models/inat_bird_labels.txt ^
--input images/parrot.jpg ^
--output results/parrot.jpg ^
--top_k 3

