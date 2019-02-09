# Installing Kubeflow on Azure Kubernetes Service

## Install AKS CLI
```
az aks install-cli
```

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
1. Download Kubeflow components.
```
KUBEFLOW_SRC=~/kubeflow
mkdir ${KUBEFLOW_SRC}
cd ${KUBEFLOW_SRC}
export KUBEFLOW_TAG=v0.4.1

curl https://raw.githubusercontent.com/kubeflow/kubeflow/${KUBEFLOW_TAG}/scripts/download.sh | bash
```

2. Set up Kubeflow components.
```
KFAPP=my-kf
${KUBEFLOW_SRC}/scripts/kfctl.sh init ${KFAPP} --platform none
cd ${KFAPP}
${KUBEFLOW_SRC}/scripts/kfctl.sh generate k8s
${KUBEFLOW_SRC}/scripts/kfctl.sh apply k8s
```

## Validate the installation
```
kubectl get all -n kubeflow
```

You should see the similar output

```
demouser@svcjkds1:/data/home/demouser/notebooks/repos$ kubectl get all -n kubeflow
NAME                                                          READY   STATUS      RESTARTS   AGE
pod/ambassador-5cf8cd97d5-9lwxl                               1/1     Running     0          1h
pod/ambassador-5cf8cd97d5-hz8rp                               1/1     Running     0          1h
pod/ambassador-5cf8cd97d5-jr4kt                               1/1     Running     0          1h
pod/argo-ui-7c9c69d464-4jk97                                  1/1     Running     0          1h
pod/centraldashboard-6f47d694bd-b4fnd                         1/1     Running     0          1h
pod/distributed-training-worker-0                             0/1     Completed   0          57m
pod/distributed-training-worker-1                             0/1     Completed   0          57m
pod/distributed-training-worker-2                             0/1     Completed   0          57m
pod/jupyter-0                                                 1/1     Running     0          1h
pod/katib-ui-6bdb7d76cc-6l9m8                                 1/1     Running     0          1h
pod/metacontroller-0                                          1/1     Running     0          1h
pod/minio-7bfcc6c7b9-cs4cg                                    1/1     Running     0          1h
pod/ml-pipeline-6fdd759597-zrwlk                              1/1     Running     0          1h
pod/ml-pipeline-persistenceagent-5669f69cdd-klljr             1/1     Running     1          1h
pod/ml-pipeline-scheduledworkflow-9f6d5d5b6-ntnzh             1/1     Running     0          1h
pod/ml-pipeline-ui-67f79b964d-dx4cv                           1/1     Running     0          1h
pod/mysql-6f6b5f7b64-7nt5z                                    1/1     Running     0          1h
pod/pytorch-operator-6f87db67b7-k4rwx                         1/1     Running     0          1h
pod/spartakus-volunteer-8545877b8f-mqtjd                      1/1     Running     0          1h
pod/studyjob-controller-774d45f695-pkm7v                      1/1     Running     0          1h
pod/tf-job-dashboard-5f986cf99d-ph2pq                         1/1     Running     0          1h
pod/tf-job-operator-v1beta1-5876c48976-kch7q                  1/1     Running     0          1h
pod/vizier-core-fc7969897-q4rcr                               1/1     Running     1          1h
pod/vizier-core-rest-6fcd4665d9-9gscm                         1/1     Running     0          1h
pod/vizier-db-777675b958-k7xsd                                1/1     Running     0          1h
pod/vizier-suggestion-bayesianoptimization-54db8d594f-rsthw   1/1     Running     0          1h
pod/vizier-suggestion-grid-6f5d9d647f-jx8cc                   1/1     Running     0          1h
pod/vizier-suggestion-hyperband-59dd9bb9bc-rm5mk              1/1     Running     0          1h
pod/vizier-suggestion-random-6dd597c997-7qff9                 1/1     Running     0          1h
pod/workflow-controller-5c95f95f58-r6cx6                      1/1     Running     0          1h

NAME                                             TYPE           CLUSTER-IP     EXTERNAL-IP     PORT(S)             AGE
service/ambassador                               LoadBalancer   10.0.179.231   13.66.156.212   80:30421/TCP        1h
service/ambassador-admin                         ClusterIP      10.0.165.4     <none>          8877/TCP            1h
...
```

