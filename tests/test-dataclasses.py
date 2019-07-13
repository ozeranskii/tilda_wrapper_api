# Project
from tests.base import TestCase
from tilda_wrapper_api.dataclasses.exceptions import TildaError
from tilda_wrapper_api.dataclasses.page import Pages, SinglePage
from tilda_wrapper_api.dataclasses.project import Projects, SingleProject


class DataclassesTest(TestCase):

    def test_exception(self) -> None:
        error_dict = {
            'status': 'ERROR',
            'message': 'Wrong public key',
            'errorside': 'info'
        }

        exception_class = TildaError.from_dict(error_dict)
        self.assertEqual(exception_class.to_dict(), error_dict)
        self.assertEqual(str(exception_class), exception_class.message)

    def test_projects(self) -> None:
        projects_dict = {
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

        projects_class = Projects.from_dict(projects_dict)
        self.assertEqual(projects_class.to_dict(), projects_dict)

    def test_single_project(self) -> None:
        project_dict = {
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

        project_class = SingleProject.from_dict(project_dict)
        self.assertEqual(project_class.to_dict(), project_dict)

    def test_pages(self) -> None:
        pages_dict = {
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

        pages_class = Pages.from_dict(pages_dict)
        self.assertEqual(pages_class.to_dict(), pages_dict)

    def test_single_page(self) -> None:
        page_dict = {
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
                'html': '<!DOCTYPE html><html><body><h1>My First Heading</h1><p>My first paragraph.</p></body></html>',
                'images': []
            },
        }

        page_class = SinglePage.from_dict(page_dict)
        self.assertEqual(page_class.to_dict(), page_dict)
