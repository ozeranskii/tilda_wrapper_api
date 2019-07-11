# Standard libraries
import os

# Project
from tilda_wrapper_api.client import Client


def run() -> None:
    """
    An example of calling methods
    :return:
    """

    # create a client object
    client = Client(secret=os.getenv('SECRET'), public=os.getenv('PUBLIC'))

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


if __name__ == '__main__':
    run()
