# TF-IDF Based Product Search API

## Overview
This project is a text-based search engine for ecommerce products using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization. The application is designed with FastAPI and includes features such as hyperparameter tuning for optimal text processing and is containerized using Docker for easy deployment and scalability

## Prerequisites
- Docker
- Python 3.9 or higher

## Project Structure

Below is the directory structure of the TF-IDF Based Product Search API, detailing the organization and purpose of each component:

```plaintext
Project Root
├── data                     # Data directory for storing product datasets. or related data files.
├── harvard_src              # Main source code directory.
│   ├── config               # Contains configuration files for model paths, logging paths, etc.
│   │   └── config.ini       
│   ├── preprocessing        # Preprocessing scripts for preparing the dataset.
│   │   └── preprocessor.py  
│   ├── training             # Contains scripts for model training and inference.
│   │   ├── inference.py    
│   │   └── trainer.py        
│   └── utils                # Utility functions and classes.
│       └── util.py          
├── logs                     # Directory to store application logs.
├── main.py                  # Main FastAPI application entry point for API interface.
├── requirements.txt         # Lists dependencies required for the project.
├── setup.py                 # Script for installing the project as a package.
└── README.md                # README file with project documentation.

```

## Project Setup

1. **Clone the git Repository:**

* Clone the repo using below git url.Replace `branchname` with the branch from which we are cloning. 

   ```bash
   git clone https://github.com/Sra1panasa/Search_Engine.git -b branchname
   ```

2. **Build the Docker image:**

* Go to the directory of Docker file.Run the below Docker build command.This command builds a Docker image named tfidf-product-search from the Dockerfile in the current directory.

    ```
    docker build -t tfidf-product-search 
    ```
3. **Run the Container :**

* Run the container using the docker run command.This maps port 8000 of the container to port 8000 on your host, making the application accessible at http://localhost:8000.(If we are running on any server make sure to replace localhost with server ip)

* The -v parameter mounts a volume for logs from /path/on/your/host on your local machine to /app/logs inside the container.

    ```
    docker run -p 8000:8000 -v /path/on/your/host:/app/logs tfidf-product-search

    example: docker run -p 8000:8000 -v D:/Sravan/logs/harvard.log:/app/logs/tfidf-product-search.log tfidf-product-search
    ```
4. **Uploading Docker Image to Docker Hub(Optional):**

* After we've built and tested your Docker image locally we can upload it to docker hub.Docker Hub is a cloud-based registry service that allows to share image with others or deploy it on different environments without creating again.

* Steps to upload Docker image to Docker Hub:

* Log in to Docker Hub: Before pushing your image to Docker Hub, we must log in using the Docker CLI. 

    ```bash
    docker login
    ```
* Tag Your Docker Image : Docker images are pushed to Docker Hub using a tag, which identifies the image version. we need to tag image with your Docker Hub username, repository name, and version. 

* Replace `yourusername` with your actual Docker Hub username and `version` with your  desired version tag (e.g., `latest` or `1.0`).

    ```bash
    docker tag harvard yourusername/harvard:version
    ```
* Push the Image to Docker Hub: Once your image is tagged, we can push it to Docker Hub using the `docker push` command. This uploads image and makes it available in  Docker Hub repository.

* Replace `yourusername` and `version` with Docker Hub username and the version tag you used earlier

    ```bash
    docker push yourusername/harvard:version
    ```

## Testing the Endpoint

* Once the Docker container is up and running, the FastAPI application's `/search` endpoint. 

* End point url: `http://localhost:8000/search`  (replace localhost with server IP)

