.PHONY: all
all: development

.PHONY: virtualenv
virtualenv:
	bash -c "source /Users/dchen/Development/coin_tracker/venv_detector.sh"

.PHONY: development
development: virtualenv
	venv/bin/pip install -r requirements.txt

