start:
	docker-compose up -d --build

start-dev:
	docker-compose up -d postgres pgadmin

stop:
	docker-compose down

server:
	uvicorn app.main:app --reload