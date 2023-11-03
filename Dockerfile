# Use the specific base image
FROM kshanmukha1501/flask:v4

# Set the working directory inside the container
WORKDIR /root/flaskapp

# Copy the Flask app files from your host to your current location (WORKDIR) in the image
COPY . .

ENTRYPOINT ["/bin/bash", "/run_services.sh"]