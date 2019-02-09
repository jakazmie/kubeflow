# TFJOB Quick Start

## Create TFJOB component
### Install Kubeflow ksonnet prototypes
```
export  KF_VERSION=v0.4.1
ks registry add kubeflow-git github.com/kubeflow/kubeflow/tree/${KF_VERSION}/kubeflow
```

### Install TF-JOB-OPERATOR package
```
ks pkg install kubeflow-git/tf-training
```

