service_name="score-service"

echo "Running $service_name/run-script.sh"
echo "Building $service_name"

container_name=$service_name

echo "Temporarily copying data directory in current directory"
cp -r ../data .

docker build --no-cache . --tag $container_name

if [ "$( docker container inspect -f '{{.State.Running}}' $container_name )" = "true" ]; then ...
  echo "Container is running, stopping and removing it"
  docker stop $container_name
  docker rm $container_name
fi

echo "Running $service_name in a detached container"
docker run -d -p 8000:8000 --name $container_name $container_name

echo "Deleting the temporary data directory"
rm -rf data

echo "Finished running $service_name/run-script.sh"
