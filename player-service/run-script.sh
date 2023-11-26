service_name="player-service"

echo "Running $service_name/run-script.sh"
echo "Building $service_name"

container_name=$service_name

docker build --no-cache . --tag $container_name

if [ "$( docker container inspect -f '{{.State.Running}}' $container_name )" = "true" ]; then ...
  echo "Container is running, stopping and removing it"
  docker stop $container_name
  docker rm $container_name
fi

echo "Running $service_name in a detached container"
docker run -d -p 8001:8001 --name $container_name $container_name
