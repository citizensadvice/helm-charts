# Helm charts

This repo contains Helm charts forked from the community, and it's public.

## Adding to Helm

```
helm repo add citizensadvice 'https://raw.githubusercontent.com/citizensadvice/helm-charts/master/'
helm install -n test elasticsearch citizensadvice/elasticsearch
```

Update using `helm repo update`

## Adding a chart to this repository

Before publishing a chart verify that the metadata in `Chart.yaml` (e.g. maintainers) are correct:

```yaml
apiVersion: v1
description: CA fork of Elastic helm chart for Elasticsearch
home: https://github.com/citizensadvice/helm-charts
maintainers:
- email: ca-devops@citizensadvice.org.uk
  name: CA Devops
name: elasticsearch
version: 7.6.2
appVersion: 7.6.2
sources:
  - https://github.com/elastic/elasticsearch
icon: https://helm.elastic.co/icons/elasticsearch.png
```

- package the chart using `helm package <chart_dir>`
- copy the chart archive into the `charts/` directory
- run `helm repo index .` to update `index.yaml`
- open PR
