# set base image (host OS)
# FROM python:3.8
# FROM python:3.8-alpine
FROM python:3.12-rc-bullseye

RUN apt-get update && apt-get upgrade -y \
  && apt-get install -y \
  curl \
  nodejs \
  npm \
  && npm install -g nodemon

WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . .

# command to run on container start
CMD [ "python", "src/wyrdl.py" ]