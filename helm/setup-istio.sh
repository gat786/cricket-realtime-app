#! /bin/bash

istioctl install

kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.23/samples/addons/prometheus.yaml -n istio-system

kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.23/samples/addons/kiali.yaml -n istio-system

NAMESPACE=default
kubectl create ns $NAMESPACE
kubectl label ns $NAMESPACE istio-injection=enabled
