.PHONY: install virtualenv ipython clean test pflake8

install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'


virtualenv:
	@.venv/bin/python -m pip -m venv .venv


ipython:
	@.venv/bin/ipython

test:
	@.venv/bin/pytest -s --cov=mouracx -vv
	@.venv/bin/coverage xml
	@.venv/bin/coverage html

lint:
	@.venv/bin/pflake8

fmt:
	@.venv/bin/isort mouracx test integration
	@.venv/bin/black mouracx tests integration

watch:
	ls **/*.py | entr pytest --cov=mouracx
	@.venv/bin/coverage xml
	@.venv/bin/coverage html

clean:            ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build
