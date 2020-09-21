from functions.base_functions_en import *
import pytest


@pytest.fixture
def fetch_url():
    redirect_urls = all_url_call()
    url_list =[]
    for redirect_url in redirect_urls:
        driver.get(redirect_url)
        driver.maximize_window()
        time.sleep(2)
        url_list.append(redirect_url)
    return url_list










# def get_env_params():
#     env_name = pytest.config.getoption("--env")
#     return env_params[env_name]
