# Helm charts

This is the public helm repository for Citizens Advice charts.

## Adding to Helm

```
helm repo add citizensadvice 'https://citizensadvice.github.io/helm-charts'
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

- Add the chart source to the `src` directory
- Create a pull request to `master`
- Chart will be published upon merge

## Validator

The Python script `bin/validate.py` will check the validity of the `Chart.yaml` in the `src` directory according to the above criteria.

## Troubleshooting

If the `publish-charts` Action fails with the message:

```
Error: error creating GitHub release <chart name>-<chart version>: POST https://api.github.com/repos/citizensadvice/helm-charts/releases: 422 Validation Failed [{Resource:Release Field:tag_name Code:already_exists Message:}]
```

Then you need to bump the version number for said chart, as it will fail if you make changes to a chart but fail to bump the version number.
