perms:
	sudo chgrp admins {{cookiecutter.project}} && sudo chmod -R u+rwx,g+rwx {{cookiecutter.project}}

pytest:
	python -m pytest --log-cli-level info -p no:warnings -v ./tests

format:
		python -m black -S --line-length 80 --preview *.py
		python -m isort *.py

type:
		python -m mypy *.py

lint:
		flake8 some.py

ci : format type lint