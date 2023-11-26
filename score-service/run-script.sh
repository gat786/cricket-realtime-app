echo "Running score-service/run-script.sh"
echo "Building score-service"

container_name="score_service"

docker build --no-cache . --tag $container_name

if [ "$( docker container inspect -f '{{.State.Running}}' $container_name )" = "true" ]; then ...
  echo "Container is running, stopping and removing it"
  docker stop $container_name
  docker rm $container_name
fi

echo "Running score-service in a detached container"
docker run -d -p 8000:8000 --name $container_name $container_name
