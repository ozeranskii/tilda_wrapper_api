# Standard libraries
import re

# Third party libraries
import requests_mock

# Project
from tests.base import TestCase
from tilda_wrapper_api.client import Client
from tilda_wrapper_api.dataclasses.exceptions import TildaError
from tilda_wrapper_api.dataclasses.page import Pages, SinglePage
from tilda_wrapper_api.dataclasses.project import Projects, SingleProject


class ClientTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls._client = Client(
            public='public-test-value',
            secret='secret-test-value',
        )
        cls._url_matcher = re.compile('http://api.tildacdn.info/v1/')

    def test_client_init(self):
        self.assertNotEqual(self._client.public, None)
        self.assertNotEqual(self._client.secret, None)

    @requests_mock.Mocker()
    def test_bad_request(self, m) -> None:
        m.get(
            self._url_matcher,
            status_code=404,
            json={
                'status': 'ERROR',
                'message': 'Wrong public key',
                'errorside': 'info'
            }
        )

        self.assertRaises(TildaError, lambda: self._client.get_projects_list())

    @requests_mock.Mocker()
    def test_get_projects_list(self, m) -> None:
        m.get(
            self._url_matcher,
            json={
                'status': 'FOUND',
                'result': [{
                    'id': '0000000',
                    'title': 'Title',
                    'descr': 'Description',
                    'export_csspath': '',
                    'export_jspath': '',
                    'export_imgpath': '',
                    'indexpageid': None,
                    'htaccess': '',
                    'customdomain': '',
                    'images': [],
                    'css': [],
                    'js': []
                }]
            }
        )

        resp = self._client.get_projects_list()
        self.assertIsInstance(resp, Projects)

    @requests_mock.Mocker()
    def test_get_project(self, m) -> None:
        m.get(
            self._url_matcher,
            json={
                'status': 'FOUND',
                'result': {
                    'id': '0000000',
                    'title': 'Title',
                    'descr': 'Description',
                    'export_csspath': '',
                    'export_jspath': '',
                    'export_imgpath': '',
                    'indexpageid': None,
                    'htaccess': '',
                    'customdomain': '',
                    'images': [],
                    'css': [
                        'https://static.tildacdn.com/css/main.css',
                    ],
                    'js': [
                        'https://static.tildacdn.com/js/main.js',
                    ]
                }
            }
        )

        resp = self._client.get_project(project_id=1)
        self.assertIsInstance(resp, SingleProject)

    @requests_mock.Mocker()
    def test_get_project_export(self, m) -> None:
        m.get(
            self._url_matcher,
            json={
                'status': 'FOUND',
                'result': {
                    'id': '0000000',
                    'title': 'Title',
                    'descr': 'Description',
                    'export_csspath': '',
                    'export_jspath': '',
                    'export_imgpath': '',
                    'indexpageid': None,
                    'htaccess': '',
                    'customdomain': '',
                    'images': [],
                    'css': [
                        'https://static.tildacdn.com/css/main.css',
                    ],
                    'js': [
                        'https://static.tildacdn.com/js/main.js',
                    ]
                }
            }
        )

        resp = self._client.get_project_export(project_id=1)
        self.assertIsInstance(resp, SingleProject)

    @requests_mock.Mocker()
    def test_get_pages_list(self, m) -> None:
        m.get(
            self._url_matcher,
            json={
                'status': 'FOUND',
                'result': [{
                    'id': '0000000',
                    'projectid': '0000000',
                    'title': 'Landing 1',
                    'descr': '',
                    'img': '',
                    'featureimg': '',
                    'alias': '',
                    'date': '2019-06-15 17:32:09',
                    'sort': '10',
                    'published': '1561875543',
                    'filename': 'page0000000.html',
                    'html': '',
                    'images': []
                }, {
                    'id': '0000001',
                    'projectid': '0000000',
                    'title': 'Landing 2',
                    'descr': '',
                    'img': '',
                    'featureimg': '',
                    'alias': 'landing2',
                    'date': '2019-06-26 08:19:46',
                    'sort': '20',
                    'published': '1562070685',
                    'filename': 'page0000001.html',
                    'html': '',
                    'images': []
                }]
            }
        )

        resp = self._client.get_pages_list(project_id=1)
        self.assertIsInstance(resp, Pages)

    @requests_mock.Mocker()
    def test_get_page(self, m) -> None:
        m.get(
            self._url_matcher,
            json={
                'status': 'FOUND',
                'result': {
                    'id': '0000000',
                    'projectid': '0000000',
                    'title': 'Landing 1',
                    'descr': '',
                    'img': '',
                    'featureimg': '',
                    'alias': '',
                    'date': '2019-06-15 17:32:09',
                    'sort': '10',
                    'published': '1561875543',
                    'filename': 'page0000000.html',
                    'html': '''
                    <!DOCTYPE html><html><body><h1>My First Heading</h1><p>My first paragraph.</p></body></html>
                    ''',
                    'images': []
                },
            }
        )

        resp = self._client.get_page(page_id=1)
        self.assertIsInstance(resp, SinglePage)

    @requests_mock.Mocker()
    def test_get_page_full(self, m) -> None:
        m.get(
            self._url_matcher,
            json={
                'status': 'FOUND',
                'result': {
                    'id': '0000000',
                    'projectid': '0000000',
                    'title': 'Landing 1',
                    'descr': '',
                    'img': '',
                    'featureimg': '',
                    'alias': '',
                    'date': '2019-06-15 17:32:09',
                    'sort': '10',
                    'published': '1561875543',
                    'filename': 'page0000000.html',
                    'html': '''
                    <!DOCTYPE html><html><body><h1>My First Heading</h1><p>My first paragraph.</p></body></html>
                    ''',
                    'images': []
                },
            }
        )

        resp = self._client.get_page_full(page_id=1)
        self.assertIsInstance(resp, SinglePage)

    @requests_mock.Mocker()
    def test_get_page_export(self, m) -> None:
        m.get(
            self._url_matcher,
            json={
                'status': 'FOUND',
                'result': {
                    'id': '0000000',
                    'projectid': '0000000',
                    'title': 'Landing 1',
                    'descr': '',
                    'img': '',
                    'featureimg': '',
                    'alias': '',
                    'date': '2019-06-15 17:32:09',
                    'sort': '10',
                    'published': '1561875543',
                    'filename': 'page0000000.html',
                    'html': '''
                    <!DOCTYPE html><html><body><h1>My First Heading</h1><p>My first paragraph.</p></body></html>
                    ''',
                    'images': []
                },
            }
        )

        resp = self._client.get_page_export(page_id=1)
        self.assertIsInstance(resp, SinglePage)

    @requests_mock.Mocker()
    def test_get_page_full_export(self, m) -> None:
        m.get(
            self._url_matcher,
            json={
                'status': 'FOUND',
                'result': {
                    'id': '0000000',
                    'projectid': '0000000',
                    'title': 'Landing 1',
                    'descr': '',
                    'img': '',
                    'featureimg': '',
                    'alias': '',
                    'date': '2019-06-15 17:32:09',
                    'sort': '10',
                    'published': '1561875543',
                    'filename': 'page0000000.html',
                    'html': '''
                    <!DOCTYPE html><html><body><h1>My First Heading</h1><p>My first paragraph.</p></body></html>
                    ''',
                    'images': []
                },
            }
        )

        resp = self._client.get_page_full_export(page_id=1)
        self.assertIsInstance(resp, SinglePage)
