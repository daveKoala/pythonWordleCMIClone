build:
	docker-compose -f docker-compose.yml up --build

dev:
	docker-compose run --service-ports --rm app /bin/bash

terminal:
	docker-compose run --service-ports --rm web /bin/bash

run:
	nodemon --legacy-watch --exec "python3" ./src/wyrdl.py 

list:
	python ./src/create_wordlist.py ./src/wyrdl.py wordlist.txt

api:
	python ./src/wordlist_api.py