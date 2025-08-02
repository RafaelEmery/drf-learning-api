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

## Main contents

- `APIView` [[1]](https://github.com/RafaelEmery/drf-learning-api/blob/main/learning_app/views.py#L21)
- `generics` API Views [[2]](https://github.com/RafaelEmery/drf-learning-api/blob/main/learning_app/views.py#L45)
- `ViewSet` [[3]](https://github.com/RafaelEmery/drf-learning-api/blob/main/learning_app/views.py#L132)
- Custom calls for relation at `ViewSet` [[4]](https://github.com/RafaelEmery/drf-learning-api/blob/main/learning_app/views.py#L161)
- Basic Django models and migrations [[5]](https://github.com/RafaelEmery/drf-learning-api/blob/main/learning_app/models.py#L28)
- Using permissions [[6]](https://github.com/RafaelEmery/drf-learning-api/blob/main/learning_app/permissions.py#L5)[[7]](https://github.com/RafaelEmery/drf-learning-api/blob/main/learning_app/views.py#L147)
- Basic routing [[8]](https://github.com/RafaelEmery/drf-learning-api/blob/main/learning_app/urls.py#L29) and using `SimpleRouter`[[9]](https://github.com/RafaelEmery/drf-learning-api/blob/main/learning_app/urls.py#L21)[[10]](https://github.com/RafaelEmery/drf-learning-api/blob/main/drf_learning_api/urls.py#L27)
- Basic Django Admin [[11]](https://github.com/RafaelEmery/drf-learning-api/blob/main/learning_app/admin.py#L7)
- Basic serializers [[12]](https://github.com/RafaelEmery/drf-learning-api/blob/main/learning_app/serializers.py#L7) with validation [[13]](https://github.com/RafaelEmery/drf-learning-api/blob/main/learning_app/serializers.py#L16)
- Relation in serializers [[14]](https://github.com/RafaelEmery/drf-learning-api/blob/main/learning_app/serializers.py#L71)
- Custom fields and methods at serializers [[15]](https://github.com/RafaelEmery/drf-learning-api/blob/main/learning_app/serializers.py#L86)

#### TODOs:

- [X] Fix local running issues
- [X] Add linter
- [ ] ~~Update django and DRF to latest versions~~
- [ ] Test all the calls using `generic API Views` and `ViewSets`

---

Made with :heart: by [RafaelEmery](https://github.com/RafaelEmery)

