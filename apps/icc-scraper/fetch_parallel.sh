# grab test data
python src/main.py --comp-type 1 --rank-for 1

python src/main.py --comp-type 1 --rank-for 2

python src/main.py --comp-type 1 --rank-for 3

# grab odi data
python src/main.py --comp-type 2 --rank-for 1 --scrape-from-date 20111118

python src/main.py --comp-type 2 --rank-for 2 --scrape-from-date 20120731

python src/main.py --comp-type 2 --rank-for 3 --scrape-from-date 20120716

# grab t20 data
python src/main.py --comp-type 3 --rank-for 1 --scrape-from-date 20180612

python src/main.py --comp-type 3 --rank-for 2 --scrape-from-date 20171220

python src/main.py --comp-type 3 --rank-for 3 --scrape-from-date 20171107
