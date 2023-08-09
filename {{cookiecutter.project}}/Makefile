help:
	@echo "Available command"
	@echo "- pytest.      : Run tests "
	@echo "- format       : Format python scripts using black & isort"
	@echo "- type	      : Perform type check using mypy"
	@echo "- lint         : Lint the code using flake8"
	@echo "- secure       : Perform security vulnerabilities in files"
	@echo "- deps	      : Install required dependency for the project"
	@echo "- ci	      : Perform CI steps using format, type, line & secure"
	@echo "- perms        : Set rwx permission & change group to dev for all files in the project"	

perms:
	sudo chgrp dev {{cookiecutter.project}} && sudo chmod -R u=rwx,g=rwx {{cookiecutter.project}}

pytest:
	python -m pytest --log-cli-level info -p no:warnings -v ./tests

format:
		python -m black -S --line-length 80 --preview *.py
		python -m isort *.py

type:
		python -m mypy *.py

lint:
		flake8 *.py

secure:
		bandit -r ./{{cookiecutter.project}}
deps:
	pip3 install -r requirements.txt

ci : format type lint secure