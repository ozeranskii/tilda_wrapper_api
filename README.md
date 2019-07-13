![PyPI](https://img.shields.io/pypi/v/tilda-wrapper-api.svg) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tilda-wrapper-api.svg)  ![PyPI - License](https://img.shields.io/pypi/l/tilda-wrapper-api.svg) ![PyPI - Format](https://img.shields.io/pypi/format/tilda-wrapper-api.svg) ![PyPI - Status](https://img.shields.io/pypi/status/tilda-wrapper-api.svg) [![Coverage Status](https://coveralls.io/repos/github/ozeranskiy/tilda_wrapper_api/badge.svg)](https://coveralls.io/github/ozeranskiy/tilda_wrapper_api)

# Tilda API

A python implementation of [Tilda API](http://help-ru.tilda.ws/api)

## Getting Started

The project provides full access to Tilda.cc API via an object-oriented Python interface using dataclasses.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install package.

```bash
pip install tilda-wrapper-api
```
 
Use the package manager [pipenv](https://github.com/pypa/pipenv) to install package.

```bash
pipenv install tilda-wrapper-api
```

## Usage

```python
# Standard libraries
import os

# Project
from tilda_wrapper_api.client import Client

# create a client object, default value secret=os.getenv('SECRET') and public=os.getenv('PUBLIC')
client = Client()

# get list of projects
projects = client.get_projects_list()
print(projects)

# get project information
project = client.get_project(projects.result[0].id)
print(project)

# get project information for export
project_export = client.get_project_export(projects.result[0].id)
print(project_export)

# get list of pages in the project
pages = client.get_pages_list(projects.result[0].id)
print(pages)

# get information about the page (+ body html-code)
page = client.get_page(pages.result[0].id)
print(page)

# get information about the page (+ full page html-code)
page_full = client.get_page_full(pages.result[0].id)
print(page_full)

# get information about the page for export (+ body html-code)
page_export = client.get_page_export(pages.result[0].id)
print(page_export)

# get information about the page for export (+ full page html-code)
page_full_export = client.get_page_full_export(pages.result[0].id)
print(page_full_export)
```

## Built With

* [Requests](https://github.com/kennethreitz/requests) - Python HTTP Requests for Humans™
* [dataclasses-json](https://github.com/lidatong/dataclasses-json) -  Library provides a simple API for encoding and decoding dataclasses to and from JSON

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Authors

* **Sergey Ozeranskiy** - *Initial work* - [ozeranskiy](https://github.com/ozeranskiy)

See also the list of [contributors](https://github.com/ozeranskiy/tilda_wrapper_api/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details