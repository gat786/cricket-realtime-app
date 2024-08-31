while true
do
	sleep 2;
	timestamp=$(date +%H:%M:%S_%d:%m:%Y)
	# url_to_check="https://assets-icc.sportz.io/cricket/v1/ranking?client_id=tPZJbRgIub3Vua93/DWtyQ%3D%3D&comp_type=test&feed_format=json&lang=en&type=team"
	url_to_check="https://assets-icc.sportz.io/cricket/v1/ranking?comp_type=test&feed_format=json&lang=en&type=team"
    http_status=$(curl -s -o /dev/null -w "%{http_code}" $url_to_check)
	echo checking $url_to_check;
	echo current time - $timestamp current status - $http_status;

	echo "";
done;