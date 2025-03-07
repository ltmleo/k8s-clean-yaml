# k8s-clean-yaml
Clean useless fields in kubernetes manifests

## Download and Install

```bash
git clone https://github.com/ltmleo/k8s-clean-yaml.git
cd k8s-clean-yaml
pip install -r requirements.txt
sudo ln -s $(pwd)/clean-yaml.py /usr/local/bin/cleanyaml
```

## Dependencies
- python: >= 3.6
- PyYAMl: >= 5.3.1

## How to use
Kubernetes have a ton of useless fields in manifests, to clean these fields, you can execute:
`kubectl get pods -o yaml | cleanyaml`
or
`cleanyaml manifest.yaml`

## Remove custom fiels
To remove custom fields you just need to add them to `FIELDS_TO_RM` dictionary.

By default this fields are being removed:
```json
{
"metadata": {
    "annotations": {
        "kubectl.kubernetes.io/last-applied-configuration": " ",
        "autoscaling.alpha.kubernetes.io/conditions": " ",
        "control-plane.alpha.kubernetes.io/leader": " "
    },
    "generation": " ",
    "creationTimestamp": " ",
    "resourceVersion": " ",
    "selfLink": " ",
    "uid": " ",
    "managedFields": " "
},
"spec": {
    "clusterIP": " ",
    "clusterIPs": " ",
    "finalizers": " "
},
"status": " "
}
```


## Colaborate
All ideas and improvements are welcome!!
