# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
# If you have external dependencies, uncomment the next line and add a requirements.txt file
# RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
# This is optional and can be changed based on your needs
EXPOSE 80

# Define environment variable
# You can define environment variables that your application uses
# ENV NAME World

# Run app.py when the container launches
# Replace 'app.py' with the script name you want to run, for example, 'myscript.py'
CMD [ "python", "./user-input.py" ]

