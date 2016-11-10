#
# Ubuntu Dockerfile
#

# Pull base image
FROM ubuntu:16.04
FROM python:3.5.2

# Add files
ADD serverTest.py /

# Install libraries
RUN pip install image
RUN pip install flask

# Expose
EXPOSE 8888

# Execute the server file
CMD ["python", "./serverTest.py"]


