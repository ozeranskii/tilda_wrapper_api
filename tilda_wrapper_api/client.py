# Standard libraries
from dataclasses import dataclass
from typing import Dict

# Third party libraries
import requests

# Project
from tilda_wrapper_api.dataclasses.exceptions import TildaError
from tilda_wrapper_api.dataclasses.page import Pages, SinglePage
from tilda_wrapper_api.dataclasses.project import Projects, SingleProject


@dataclass(frozen=True)
class Client:
    """
    Wrapper for Tilda API
    """

    public: str
    secret: str
    endpoint: str = 'http://api.tildacdn.info/v1'

    def _request(self, method: str, params: Dict = None):
        payload = {
            'publickey': self.public,
            'secretkey': self.secret,
        }

        if params:
            payload.update(params)

        response = requests.get(f'{self.endpoint}/{method}/', params=payload)
        json_response = response.json()
        if response.status_code != requests.codes.ok:
            raise TildaError.from_dict(json_response)
        return json_response

    def get_projects_list(self) -> Projects:
        """
        Get list of projects
        :return:
        """
        projects = self._request('getprojectslist')
        return Projects.from_dict(projects)

    def get_project(self, project_id: int) -> SingleProject:
        """
        Get project information
        :param project_id:
        :return:
        """
        project = self._request('getproject', {'projectid': project_id})
        return SingleProject.from_dict(project)

    def get_project_export(self, project_id: int) -> SingleProject:
        """
        Get project information for export
        :param project_id:
        :return:
        """
        project = self._request('getprojectexport', {'projectid': project_id})
        return SingleProject.from_dict(project)

    def get_pages_list(self, project_id: int) -> Pages:
        """
        Get list of pages in the project
        :param project_id:
        :return:
        """
        project = self._request('getpageslist', {'projectid': project_id})
        return Pages.from_dict(project)

    def get_page(self, page_id: int) -> SinglePage:
        """
        Get information about the page (+ body html-code)
        :param page_id:
        :return:
        """
        page = self._request('getpage', {'pageid': page_id})
        return SinglePage.from_dict(page)

    def get_page_full(self, page_id: int) -> SinglePage:
        """
        Get information about the page (+ full page html-code)
        :param page_id:
        :return:
        """
        page = self._request('getpagefull', {'pageid': page_id})
        return SinglePage.from_dict(page)

    def get_page_export(self, page_id: int) -> SinglePage:
        """
        Get information about the page for export (+ body html-code)
        :param page_id:
        :return:
        """
        page = self._request('getpageexport', {'pageid': page_id})
        return SinglePage.from_dict(page)

    def get_page_full_export(self, page_id: int) -> SinglePage:
        """
        Get information about the page for export (+ full page html-code)
        :param page_id:
        :return:
        """
        page = self._request('getpagefullexport', {'pageid': page_id})
        return SinglePage.from_dict(page)
