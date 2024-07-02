#!/usr/bin/python3
import sys
import yaml


def remove_fields(rm, d):
    for k in rm.keys():
        if k in d.keys():
            if isinstance(rm[k], dict):
                remove_fields(rm[k], d=d[k])
            else:
                del d[k]
    return d


FIELDS_TO_RM = {
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
        "finalizers": " "
    },
    "status": " "
}

if __name__ == "__main__":
    if not sys.stdin.isatty():
        resources = yaml.full_load(sys.stdin)
    else:
        try:
            input_filename = sys.argv[1]
        except IndexError:
            message = 'need filename as first argument if stdin is not full'
            raise IndexError(message)
        else:
            with open(input_filename, "r") as f:
                resources = yaml.load(f)
    filtered_resources = []
    if "items" in resources:
        for resource in resources["items"]:
            filtered_resources.append(remove_fields(FIELDS_TO_RM, resource))
        resources["items"] = filtered_resources
    else:
        resources = remove_fields(FIELDS_TO_RM, resources)
    sys.stdout.write(f"{yaml.dump(resources, default_flow_style=False)}")
