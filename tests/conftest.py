import pytest
from playwright.sync_api import Page

BASE_URL = "https://cerulean-praline-8e5aa6.netlify.app"

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    page.goto(BASE_URL)
    yield page
    page.close()