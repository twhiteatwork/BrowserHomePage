# XYZ Application

This repository contains the XYZ corporation SaaS web application. The application is written in Python using the Flask module. The application can be run by developers directly using Flask or built into a Docker container and run using Docker Desktop.

There is an Azure DevOps team project with build and release pipelines. The build pipeline pushes tagged versions of container image to an Azure Container Registry. The release pipeline pulls latest tagged version of the container image and deploys it to the Azure App Service.

## Preparing Developer Environment

### Install prerequisites as required
1. Install [Python](https://www.python.org/downloads/)
2. Install [Git](https://git-scm.com/downloads)
3. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
4. Install [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)

### Pull source repository
1. Connect to [BrowserHomePage](https://github.com/twhiteatwork/BrowserHomePage) and [configure SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
2. Create folder "Code" with Subfolder "BrowserHomePage" and open command prompt in that folder
3. Add remote origin

    $ git remote add origin git@github.com:twhiteatwork/BrowserHomePage.git

4. Fetch remote source

    $ git fetch origin main

### Install required Python modules not already installed

    $ pip install -requirements.txt

## Running and accessing the application

### Directly using Flask

    $ flask run --host 0.0.0.0 --port 8080

### By building docker container and running it

    $ docker build -t homepage .
    $ docker run -d -p 8080:8080 homepage

### Access the application

Irrespective of how the application is run, it is accessible at [http://localhost:8080].

## Azure DevOps

[Team Project](https://dev.azure.com/twhiteatwork/Liatrio.XYZ)

[Main Build Pipeline](https://dev.azure.com/twhiteatwork/Liatrio.XYZ/_build?definitionId=1)

[Main Release Pipeline](https://dev.azure.com/twhiteatwork/Liatrio.XYZ/_release?_a=releases&view=mine&definitionId=1)