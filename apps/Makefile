build-docker-all:
	echo "building all the images all at once"
	
	# cd frontend-blazor && bash run-script.sh
	cd player-service && bash run-script.sh
	cd score-service && bash run-script.sh
	cd team-service && bash run-script.sh

build-ps-docker:
	cd player-service && bash run-script.sh

build-ts-docker:
	cd team-service && bash run-script.sh

build-ss-docker:
	cd score-service && bash run-script.sh
