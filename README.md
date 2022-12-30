# Deploying a Postgres DB and a Flask server in K8s
This project was made solely to learn how to deploy a database and a web server in Kubernetes, and make them communicate. The deployment is done on a local minikube cluster, but can of course be changed to run on other clusters.

## Prerequisities
- Have a working minikube installation
- Have NGINX Ingress controller enabled on minikube

## How to run the project
1. Follow the steps in **deploy_app** manually, or simply make it executable and run the script
2. Run `minikube ip` to check your cluster's external IP address, it will be used in the next step
3. Add `<IP from step 2> postgres-app.info` to `/etc/hosts` locally
4. Open a web broswer and hit `postgress-app.info`