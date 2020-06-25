**To install Docker Toolbox for Windows 8 or 8.1:** *https://docs.docker.com/toolbox/toolbox_install_windows/*

**To install Docker Desktop for Windows 10:** *https://docs.docker.com/docker-for-windows/install/*

**Docker for beginners:** *https://github.com/docker/labs/tree/master/beginner*

**Steps:**
* Navigate to the directory that has Dockerfile and run the build command

    **docker build -t dockergk1811/myfirstapp .**

* To view the list of docker images available in your local

    **docker images**

* To run the application

    **docker run -p 8888:5000 --name myfirstapp dockergk1811/myfirstapp**

* To find the port in docker machine

    **docker-machine ip default** (In my case: http://192.168.99.100/)

* To view the application

    **http://192.168.99.100:8888/**

* To stop the application

    **docker stop myfirstapp**

* To remove the container

    **docker rm myfirstapp**

* To push the image

    **docker login**
    
    **docker push dockergk1811/myfirstapp**
