# Posts API REST made with python
This easy project create a REST API for managing posts.

CI status:

Test:
[![Test Status](https://travis-ci.org/pfuentesg/flask_posts_API.svg?branch=master)](https://travis-ci.org/pfuentesg/flask_posts_API)
Coverage:
[![Coverage Status](https://coveralls.io/repos/github/pfuentesg/flask_posts_API/badge.svg?branch=master)](https://coveralls.io/github/pfuentesg/flask_posts_API?branch=master)
## Architecture (To document)
## Testing 
This repository is using [pytest](https://docs.pytest.org/en/latest/contents.html#toc)
to test the source code . to run tests just type ` pytest` and test will be passing for you

-Tip: coverage: if you want to have test coverage, you only have to type `pytest -cov .` and this will return code
 coverage for you, using what we have in .coveragerc to exclude your uwn test and virtual environment fields  
 
## Validation
Flask-restful includes a really good validation library, called reqparse. al validations are inside folder validators
- example:
    
  ```` python
    from flask restful import reqparse

    def my_awesome_validation():
        parser = reqparse.RequestParser()
        parser.add_argument('my_awesome_input', required=True, help='my awesome input')
        return parser.parse_args()
 
## config 
In [config.py](./config.py) we have an object saving all variables tat can be piked from 
a environment variable or default value. You can import this object from container
## swagger



## TODO:
- [x] Include Postgree as database (start with sqlite3)
- [ ] Unit testing (Doing)
- [x] Config field
- [ ] logger
- [x] body validation 
- [x] Container for dependency
- [ ] Integration test 
- [ ] Swagger
- [ ] Document all
- [ ] Docker
- [ ] Travis for testing and deploy (docker and Heroku)
- [ ] Pipenv
