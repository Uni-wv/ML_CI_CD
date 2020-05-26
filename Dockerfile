FROM centos:7 
RUN yum install python36 -y
RUN python3 -m pip install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN yum install epel-release -y
RUN yum install python36-devel -y
RUN pip3 install sklearn 
RUN pip3 install pandas
RUN pip3 install matplotlib
RUN pip3 install tensorflow
RUN pip3 install scipy
RUN pip3 install pillow
RUN pip3 install keras
RUN pip3 install opencv-python
RUN pip3 install numpy
CMD ["python3","/task/cnn/cnntrain.py"]