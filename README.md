This is a test file to run a basic tensorflow code on your nvidia gpu:
steps: 


## Installation Steps

### 1. Install GPU Driver

Install the appropriate NVIDIA GPU driver for your computer.
for the exact model of your gpu run command:

```bash
lspci | grep -i nvidia | sed -n 's/.*\[\(.*\)\].*/\1/p'
```


### 2. Install CUDA Toolkit (optional since cuda will be installed on our conda env)

Install the CUDA toolkit, which allows software to use GPUs for general-purpose processing.

https://developer.nvidia.com/cuda-downloads

### 3. Create a Conda Environment


install conda if it doesnt exst on your system :
https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html


  ### <note> to skip levels 3,4 given that anaconda is already 
  ### installed you can run the following command:
  ```bash
  conda env create -f environment.yml
  ```  

Open a terminal and switch to your root user, then create a new Conda environment with Python 3.8: 

```bash
conda create --name <env-name> python=3.8
```

activate the environment you created using command: 

```bash
conda activate <env-name>
```
 your terminal will be formatted in the following way (bash):

 ```bash
 (<env-name>) [root@hostname tenserflow]#
 ```
### 4. Install TensorFlow

Inside the created Conda environment, install TensorFlow:
```bash
conda install -c conda-forge cudatoolkit=11.8.0
python3 -m pip install nvidia-cudnn-cu11==8.6.0.163 tensorflow==2.13.*
mkdir -p $CONDA_PREFIX/etc/conda/activate.d
echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.file)"))' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
echo 'export LD_LIBRARY_PATH=$CUDNN_PATH/lib:$CONDA_PREFIX/lib/:$LD_LIBRARY_PATH' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
source $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
```
### 5. Monitor GPU Usage

Watch and monitor the processes running on your GPU using the following command:

```bash
watch -n 1 nvidia-smi  
```
(SMI = systems management interface)


```bash
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.104.05             Driver Version: 535.104.05   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce RTX 3050 ...    Off | 00000000:01:00.0 Off |                  N/A |
| N/A   41C    P3               9W /  35W |    437MiB /  4096MiB |     14%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+

+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|    0   N/A  N/A     60585      G   /usr/libexec/Xorg                           337MiB |
|    0   N/A  N/A     60801      G   /usr/bin/gnome-shell                         49MiB |
|    0   N/A  N/A     62660      G   ...sion,SpareRendererForSitePerProcess       43MiB |
+---------------------------------------------------------------------------------------+
```



### 6. Run TensorFlow Code

While inside the Conda environment you created, navigate to the directory with the TensorFlow code (e.g., `test.py`) and execute it
using cli command `python test.py` , if everything is configured correctly you should see a process named python in the nvidia smi  while the file is being executed. also during the execution output in the terminal you will see the name of your GPU  :

note that you can also run `hello world.py` but its runtime is very fast.

Example:
```bash
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.104.05             Driver Version: 535.104.05   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce RTX 3050 ...    Off | 00000000:01:00.0 Off |                  N/A |
| N/A   41C    P3               9W /  35W |    437MiB /  4096MiB |     14%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|    0   N/A  N/A     60585      G   /usr/libexec/Xorg                           337MiB |
|    0   N/A  N/A     60801      G   /usr/bin/gnome-shell                         49MiB |
|    0   N/A  N/A     62660      G   ...sion,SpareRendererForSitePerProcess       43MiB |
|    0   N/A  N/A     75363      C   python                                     1932MiB | (Successful execution)
+---------------------------------------------------------------------------------------+
```
### 7. go get yourself a cookie for getting here 
