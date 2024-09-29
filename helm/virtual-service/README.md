# Virtual Services and Destination Rules

Virtual Services are a Kubernetes object that work as a superset of Kubernetes
Services and they allow you to control the flow of traffic that happens to Kubernetes
Pods by allowing to specify certain conditions according to which pods will be 
distributed across the pods that lay below that service.

For example if you have a Service which is for `app: Frontend` and beneath it you are
deploying multiple versions of that app with labels like `version: beta` & 
`version: alpha` with the help of a virtual service and properly setup destination
rule you can route/share traffic between the pods according your preferance
i.e attach some weight to how much traffic should be delivered to a specific
pod which has a specific label.
