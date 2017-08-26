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
	python -m pytest -s tests

