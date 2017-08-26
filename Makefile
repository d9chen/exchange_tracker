DIR = ${CURDIR}

.PHONY: all
all: development

.PHONY: virtualenv
virtualenv:
	bash -c "source $(DIR)/venv_detector.sh"

.PHONY: development
development: virtualenv
	venv/bin/pip install -r requirements.txt

.PHONY: test
test: virtualenv development
	coverage run --source=exchange,helpers -m pytest -s tests
	coverage report
