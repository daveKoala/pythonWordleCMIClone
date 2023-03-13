build:
	docker-compose -f docker-compose.yml up --build

dev:
	docker-compose run --service-ports --rm app /bin/bash

terminal:
	docker-compose run --service-ports --rm web /bin/bash