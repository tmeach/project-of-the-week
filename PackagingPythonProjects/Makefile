LOCAL_TAG:=$(shell date +"%Y-%m-%d-%H-%M")
LOCAL_IMAGE_NAME:=telegram-currency-converter-BOT:${LOCAL_TAG}

test:
	pytest tests/

quality_checks:
	isort .
	black .
	pylint --recursive=y .

build: quality_checks test
	docker build -t ${LOCAL_IMAGE_NAME} ..
	 
setup:
	pip install -r requirements.dev -r requirements.prod
	pre-commit install

clean:
	find . -name "*.pyc" -delete
	rm -rf __pycache__