#!/usr/bin/bash
pipenv install --system
pytest -v -s -n 2 --html=/app/reports/report.html --self-contained-html --tb=no
#pytest -v -s --html=/app/reports/report.html --self-contained-html tests/test_airports_id.py::test_get_airports_json_structure
#pytest -v -s --html=/app/reports/report.html --self-contained-html tests/test_airports_id_rate_limit.py::test_101_requests_exceed_1min_rate_limit
