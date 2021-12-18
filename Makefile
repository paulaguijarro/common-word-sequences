.PHONY: help venv install install-test clean flake8 style-check style-fix docker-build docker-run

help:
	@echo "----------------------HELP------------------------------"
	@echo "To setup the project type make install"
	@echo "To test the project type make test"
	@echo "To check PEP8 compliance type make flake8"
	@echo "To check python style compliance type make style-check"
	@echo "To fix python style compliance type make style-fix"
	@echo "To build the Docker image type make run docker-build"
	@echo "To run Docker using a sample text file run docker-build"
	@echo "To clean the environment type make clean"
	@echo "--------------------------------------------------------"

venv:
	python -m venv venv

install: venv
	. venv/bin/activate; pip install -r requirements.txt --upgrade

install-test: venv
	. venv/bin/activate; pip install -r common_word_sequences/tests/requirements.txt --upgrade

clean:
	rm -rf venv

flake8: venv install-test
	. venv/bin/activate
	venv/bin/flake8

style-check: venv install-test
	. venv/bin/activate
	venv/bin/black --check --diff common_word_sequences/
 
style-fix: venv install-test
	. venv/bin/activate
	venv/bin/black common_word_sequences/

test: venv install install-test
	. venv/bin/activate
	venv/bin/pytest --cov=common_word_sequences

docker-build:
	docker build -t common_word_sequences .

docker-run: docker-build
	@echo "---------------INFO-----------------"
	@echo "Runs docker using a sample text file"
	docker run common_word_sequences -f text-examples/origin-of-species.txt
