import os
import subprocess


def install_pycoral_tpu():
    script_path = os.path.join(os.path.dirname(
        __file__), 'install_pycoral_tpu.bat')
    subprocess.call([script_path], shell=True)


if __name__ == '__main__':
    install_pycoral_tpu()
