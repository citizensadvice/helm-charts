# Helm charts

This is the public helm repository for Citizens Advice charts.

## Adding to Helm

```
helm repo add citizensadvice 'https://citizensadvice.github.io/helm-charts'
helm install -n test elasticsearch citizensadvice/elasticsearch
```

Update using `helm repo update`
