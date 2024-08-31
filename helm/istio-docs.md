# Istio Docs

This is for storing common scripts that I find along the way of learning working
with Istio. I will try to include the meaning of the scripts along as well.

Installing Istion on a cluster

```
brew install istioctl # install istioctl
istioctl install # install istio on the cluster
```

Create a namespace with sidecar injection enabled.

```
NAMESPACE="sm"
k create ns $NAMESPACE
k label ns $NAMESPACE istio-injection=enabled
```

Install Prometheus

```
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.23/samples/addons/prometheus.yaml -n istio-system
```

Installing Kiali

```
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.23/samples/addons/kiali.yaml -n istio-system
```


