# DRF Learning API

Simple API to learn and practice Django REST Framework (DRF). 

Based on some course of Udemy of DRF essentials.

## Running on local

Set the correct Python version with Pyenv:

    pyenv install 3.7
    
    pyenv local 3.7

To install all dependencies:

    pip install -r requirements.txt

To apply all migrations:

    make migrate

To run on port `8000`:

    make run

To run black linter:

    make format

#### TODOs:

- [X] Fix local running issues
- [X] Add linter
- [ ] ~~Update django and DRF to latest versions~~
- [ ] Test all the calls using `generic API Views` and `ViewSets`

---

Made with :heart: by [RafaelEmery](https://github.com/RafaelEmery)
