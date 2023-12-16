# Django based todo

[![codecov](https://codecov.io/gh/peter-halligan/todo_py/graph/badge.svg?token=W232B3U63Z)](https://codecov.io/gh/peter-halligan/todo_py)

simple django based todo application used for learning django framework.
This repository will also be used for a 100 days of code project starting from the next commit as day 1.

This will evolve as the days pass my goal is to make a production ready application.

## prinary goals (not yet defined)

1. make a GTD style workflow and app
2. hosted and available online
3. monitoring and alerting
4. ci/cd
5. automated testing

## secondary goals

1. add javascript front end
2. cloudfront
3. ha
4. containerise
5. contious deployment
6. other

## Usage

`make setup` creates a virtual environment called ~/local_python_environment  
`make install` installs pip and requirements.txt  
`make test` runs tests agains tetst dir  
`make lint` lints the dir

## run todo application

python manage.py runserver 127.0.0.1:5000

[100 days of code diary](100_days.md)