# Installing Kubeflow on Azure Kubernetes Service

## Create AKS
Create a resource group to host AKS.
```
az group create --name <RESOURCE_GROUP_NAME> --location <LOCATION>
```

Create a cluster
```
az aks create --node-vm-size Standard_DS4_v2 --resource-group <RESOURCE_GROUP_NAME> --name <NAME> 
--node-count 3 --kubernetes-version 1.11.6 --location <LOCATION> --generate-ssh-keys
```
Get the `kubeconfig` file.
```
az aks get-credentials --name <NAME> --resource-group <RESOURCE_GROUP_NAME>
```

## Install ksonnet version 0.13.1 or later
```
cd
mkdir ksonnet
cd ksonnet
wget https://github.com/ksonnet/ksonnet/releases/download/v0.13.1/ks_0.13.1_linux_amd64.tar.gz
tar -xvf ks_0.13.1_linux_amd64.tar.gz
ln -s ~/ksonnet/ks_0.13.1_linux_amd64/ks /usr/local/bin/ks
```

## Install Kubeflow
1. Download Kubeflow CLI utility - `kfctl.sh`.
```
KUBEFLOW_SRC=~/kubeflow
mkdir ${KUBEFLOW_SRC}
cd ${KUBEFLOW_SRC}
export KUBEFLOW_TAG=v0.4.1

curl https://raw.githubusercontent.com/kubeflow/kubeflow/${KUBEFLOW_TAG}/scripts/download.sh | bash
```

2. To set up and deploy all Kubeflow components. 
**If you prepare to install only selected components (recommended for the labs) skip this step and follow the instructions in each individual lab**.
```
KFAPP=my-kubeflow
${KUBEFLOW_SRC}/scripts/kfctl.sh init ${KFAPP} --platform none
cd ${KFAPP}
${KUBEFLOW_SRC}/scripts/kfctl.sh generate k8s
${KUBEFLOW_SRC}/scripts/kfctl.sh apply k8s
```

