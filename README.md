# Kubeflow on Azure sandbox

### Create AKS

### Configure ksonnet app
```

kubectl create namespace kf-sandbox

CURRENT_CONTEXT=$(kubectl config current-context)
CURRENT_CLUSTER=$(kubectl config get-contexts $CURRENT_CONTEXT | tail -1 | awk '{print $3}')
CURRENT_USER=$(kubectl config get-contexts $CURRENT_CONTEXT | tail -1 | awk '{print $4}')

kubectl config set-context kf-sandbox \
  --namespace kf-sandbox \
  --cluster $CURRENT_CLUSTER \
  --user $CURRENT_USER
  
  
ks init ks-sandbox --context kf-sandbox
cd ks-sandbox
```



