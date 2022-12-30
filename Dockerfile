FROM python:3.6

# Install necessary packages, update first to get newest packages
RUN apt update -y

# Change the working directory to 'root'
WORKDIR /usr/src/app/

# Copy the list of python packages required
COPY requirements.txt .

# Update pip
RUN pip install -U pip

# Install all python packages
RUN pip install -r requirements.txt

# Copy all files to current working directory
COPY app.py .

# Change working directory so that python program can be executed
WORKDIR /usr/src/app

# Start the website 
CMD ["python", "app.py"]
