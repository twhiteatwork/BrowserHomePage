# XYZ Application

## Summary

This repository contains a web application for an imaginary client of Liatrio named XYZ. The application is written in Python using the Flask module. The application can be run by developers directly using Flask or built into a Docker container and run using Docker Desktop.

There is an Azure DevOps team project with build and release pipelines. The build pipeline pushes a tagged version of the built container image to an Azure Container Registry repository. Each new build of the image is also pushed to the repository with tag of latest. The CI/CD release pipeline pulls the image tagged latest and deploys it to the Azure App Service.

## Preparing Developer Environment

### Install prerequisites as required
1. Install [Python](https://www.python.org/downloads/)
2. Install [Git](https://git-scm.com/downloads)
3. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
4. Install [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)

### Pull source repository
1. Connect to [BrowserHomePage](https://github.com/twhiteatwork/BrowserHomePage) and [configure SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
2. Create local folder "Code" with Subfolder "BrowserHomePage" and open command prompt in that folder
3. Add remote origin

    git remote add origin git@github.com:twhiteatwork/BrowserHomePage.git

4. Fetch remote source

    git fetch origin main

### Install required Python modules not already installed

    pip install -requirements.txt

## Running and accessing the application

### Directly using Flask

    flask run --host 0.0.0.0 --port 8080

### By building and tagging docker container and running it

    docker build -t homepage .
    docker run -d -p 8080:8080 homepage

### Accessing the application locally

Irrespective of option selected to run the application locally, it is accessible at [http://localhost:8080].

## Azure Container Registry (ACR)

It is assumed an ACR instance exists, here is how to [create an ACR instance using Azure CLI](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-azure-cli).

    az group create --name LiatrioXYZ_group --location centralus
    az acr create --resource-group LiatrioXYZ_group --name LiatrioXYZ --sku Basic
    az login
    az acr login --name LiatrioXYZ

Container images can be pushed into ACR using [Docker CLI](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-docker-cli?tabs=azure-cli). The following is example of tagging a version of the Docker container image  and pushing it to an ACR repository named homepage with a version of V1.

    docker tag homepage liatrioxyz.azurecr.io/homepage:v1
    docker push homepage

The Azure App Service will require access to the ACR in order to pull the container image. This should be setup using an web app identity, but for purposes of example enabling admin access.

    az acr update -n LiatrioXYZ --admin-enabled true

## Azure DevOps

A team project has been provisioned in Azure DevOps for this effort. Within the team project you will find a build pipeline responsible for containerizing the Python application and committing the resulting container image to the ACR repository. You will also find a release pipeline responsible for deploying the application to the Azure App Service.

[Team Project](https://dev.azure.com/twhiteatwork/Liatrio.XYZ)

[Main Branch Build Pipeline](https://dev.azure.com/twhiteatwork/Liatrio.XYZ/_build?definitionId=1)

[Main Branch Release Pipeline](https://dev.azure.com/twhiteatwork/Liatrio.XYZ/_release?_a=releases&view=mine&definitionId=1)

## Azure App Service

The Azure App Service can be used to [host a container image](https://learn.microsoft.com/en-us/azure/app-service/tutorial-custom-container?tabs=azure-cli&pivots=container-linux) and make an application contained therein accessible from the internet.

    az appservice plan create --name ASP-LiatrioXYZgroup-93b8 --resource-group LiatrioXYZ_group --is-linux
    az webapp create --resource-group LiatrioXYZ_group --plan ASP-LiatrioXYZgroup-93b8 --name liatrioxyzapp --deployment-container-image-name liatrioxyz.azurecr.io/xyzapp:latest

In production, instances of the application could be configured with a vanity domain, but by default application can be accessed under azurewebsites.net domain. For purposes of this example, that is at [https://liatrioxyzapp.azurewebsites.net].

The application's Dockerfile configures the application to listed at port 8080, so the application instance must pass through that port.

    az webapp config appsettings set --resource-group LiatrioXYZ_group --name liatrioxyzapp --settings WEBSITES_PORT=8080

[App Overview](https://portal.azure.com/#@twhiteatworkhotmail.onmicrosoft.com/resource/subscriptions/15538f9c-a59c-4b59-95e6-9f84842af8f6/resourcegroups/LiatrioXYZ_group/providers/Microsoft.Web/sites/liatrioxyzapp/appServices)

## Cleanup

The container registry, application service plan, and application service can be cleaned up by [deleting the resource group](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-cli).

    az group delete --name LiatrioXYZ_group