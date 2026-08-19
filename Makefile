.PHONY: test labs install

install:
	python -m pip install -r requirements.txt

test:
	python -m pytest

labs:
	python labs/02_parse_response.py
	python labs/03_refusals.py
	python labs/04_fallbacks.py
