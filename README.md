#### sporty_hometest_api

An API test framework built as a part of a home test assignment.  
It targets the [PoetryDB](https://poetrydb.org/) public API and demonstrates clean structure, data-driven tests, and response validation.
PoetryDB [Github](https://github.com/thundercomb/poetrydb#readme) 

---

###### Stack

- **Python 3.10+**
- **pytest** – testing framework
- **requests** – HTTP client
- **pydantic** – data models and validation
- **allure-pytest** – rich test reporting
- **dotenv** – environment configuration
- **JSON Schema / Pydantic Validation** – response structure verification

---

###### Project structure

- clients/ # HTTP, API client (requests wrapper)  
- models/ # Pydantic models for API responses  
- schemas/ # JSON schemas (generated)  
- test_data/ # Input test data  
- tests/ # API tests  
- utils/ # Reusable utils   
- validations/ # Validation functions
- conftest.py # Fixtures
- pytest.ini
- README.md  
- requirements.txt  
- README.md  
- settings.py

---

###### Setup

```bash
git clone https://github.com/froislove/sporty_hometest_api.git
cd sporty_hometest_api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

###### Running tests
Run basic tests:

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

---

###### Coverage
- Schema validation of API responses
- Parametrized and data-driven tests
- Exception handling with Allure integration
- Modular client with detailed reporting for each step

###### Highlights
- Custom HTTPClient class with built-in Allure steps 
- Model validation integrated with Pydantic 
- Clean test separation: logic, data, and assertions split across layers 
- Easy to extend: new endpoints = new test + model, no rewiring needed

---

###### Validation
1) Response status code validation is included in all API tests as a baseline check.
2) Schema validation is implemented in the test suite "API Schema Validation" and is intended primarily for smoke testing.
3) Target field checks using Pydantic models serve two purposes: to enforce stricter structural and type validation, and to enable functional assertions within test cases.

###### Test cases

| Test Case | Description                                                                            | Steps                                                                                               | Expected Result                    | Validation                                              |
|-----------|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|------------------------------------|---------------------------------------------------------|
| TC001     | Basic schema validation for all authors                                                | 1. Send `GET /author/`  <br> 2. Check response structure                                            | Response schema is valid           | JSON schema validation                                  |
| TC002     | Basic schema validation for /author/<author> search                                    | 1. Send `GET /author/Algernon Charles Swinburne` <br> 2. Check response structure                   | Response schema is valid           | SON schema validation                                   |
| TC003     | Basic schema validation for /author/<author>/author search                             | 1. Send `GET /author/Algernon Charles Swinburne/author` <br> 2. Check response structure            | Response schema is valid           | SON schema validation                                   |
| TC004     | Negative case: unknown author                                                          | 1. Send `GET /author/Invalid` <br> 2. Check status code and content                                 | code: `404`, message: Not found    | Fields assertion                                        |
| TC005     | Positive parametrized case: checking valid amount of linecounts in response for author | 1. Send `GET /author/<author>/author/linecount` <br> 2. Check actual and expected fields linecount | Matched expected and actual values | Fields assertion throught models verification |


> **Note:** `TC005` may fail  due to inconsistent responses from the API server.  
> This behavior can be considered a potential issue on the API implementation side rather than a test failure.