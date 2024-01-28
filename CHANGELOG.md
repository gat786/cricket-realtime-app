2024-01-28 12:53:51

I have came onto realisation that the frontend that we have made using svelte
works but the issue that we were facing regarding URLs of the services is not
going to get solved by using variables during docker build time. 

Because if we call the Service URLs from frontend we cannot use k8s internal
urls as the frontend won't have any idea about the internal urls. So we have
to make sure that the node server that is running svelte app calls the urls 
and on the frontend we just see the data.

I was thinking svelte is causing unnecessay complexity for the urls but now
it makes much more sense to me.
