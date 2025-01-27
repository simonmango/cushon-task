#!/usr/bin/bash
pipenv install --system
pytest -v -s -n 2 --driver=Edge --html=/app/reports/report.html --self-contained-html --tb=no