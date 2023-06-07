## Everly Health Demo

### Key Points
- The kubernestes cluster is created in AWS using the eksctl command. This command creates all the necessary networking components (VPC, Suibnets, IGW etc), EKS Cluster, Node group and IAM roles required to create a full clsuter. The ideal and recommended method will utilize IAC ( preferrably Terraform) to deploy the AWS infrastrucutre
```
eksctl create cluster \
  --name DEMO-CLUSTER \
  --region us-east-1 \
  --nodes 2 \
  --node-type t2.large
```
- A real domain name (with an A record - demo.ebuka.io) is used for the ingress controller. This domain was created and is being hosted in Route 53
- The Cluster has two applications (microservices) running on it. everly-app and everly-app-2
```
helm create <name-of-app>
helm install <name-of-repo> <path-to-helm-manifests>
```

### Folder Structure
- The app and app2 folder contains the files for the respective applications
- The helm folder containers the kubernetes manifests which was created by the helm command 

### Overview
- the docker images for these applications are built and push to dockerhub locally: [everly-app](https://hub.docker.com/r/eanene/everly-app/tags) & [everly-app-2](https://hub.docker.com/r/eanene/everly-app-2/tags)
- Both applications were deployed using helm charts
- Given that this is a very light and simple application, only the deployment, ingress and service manifests are used (helm/app-name/templates)
- All values are defined in the values.yaml file
- An ingress controller (also installed using helm) is used to expose the applications outside of the cluster. This ingress controller creats a load balancer in AWS and the domain name of the load balancer is seen on the scrrenshots (service/nginx-ingress-ingress-nginx-controller )
- Incoming traffic is routed to these applications using path-based routing
- everly-app has a /app-1 endpoint and everyl-app-2 has /app-2 endpoint


### Video and Screenshot
- A 15 - 20 sec video showing the logs of the ingress controller as the application (both) is accessed from a chrome browser
- 2 browser screenshots of both applications
- Scrrenshot of my terminal showing all the kubenetes objects created to support these apps



