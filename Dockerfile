# Base image
FROM alpine:3.5

# To install python and pip
RUN apk add --update py2-pip

# To install python modules
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# Copy files needed to run the application
COPY app.py /usr/src/app
COPY templates/index.html /usr/src/app/templates/

# The port number that the container should expose
EXPOSE 5000

# To run the application
CMD ["python", "/usr/src/app/app.py"]