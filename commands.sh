# you can run all of these commands altogether by using it with GNU parallel
# using something like this
# parallel :::: commands.sh
# I start all the services in the background and then run the Frontend and work
# on the frontend
cd player-service/ && poetry run start
cd team-service/ && poetry run start
cd score-service/ && poetry run start
