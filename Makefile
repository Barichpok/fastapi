start:
	docker-compose up -d

stop:
	docker-compose down

server:
	uvicorn my_api.main:app --reload