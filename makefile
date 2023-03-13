# dev:
# 	docker-compose -f docker-compose.yml up --build

dev:
	docker-compose run --service-ports --rm app /bin/bash
