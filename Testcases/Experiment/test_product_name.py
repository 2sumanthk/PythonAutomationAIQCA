from functions.base_functions_en import *
import pytest

test_file_name = os.path.basename(__file__)


@pytest.mark.run(order=1)
def test_notifications(fetch_url):
    # the parameter fetch_url is called from conftest.py as a fixture (which gets called before every test_function)
    click('notifications_product_title1_xpath')
    time.sleep(2)
    prod_title2 = find_element('notifications_product_title2_xpath')
    prod_title3 = find_element('notifications_product_title3_xpath')
    prod_title4 = find_element('notifications_product_title4_xpath')
    prod_title5 = find_element('notifications_product_title5_xpath')

    notifications_prod_titles = [prod_title2, prod_title3, prod_title4, prod_title5]

    for prod_title in notifications_prod_titles:
        highlight_element(prod_title)
    capture_screenshot(test_file_name)


@pytest.mark.run(order=2)
def test_help(fetch_url):
    click('help_product_title_help_button_xpath')
    time.sleep(2)
    click('help_product_title_whats_new_xpath')
    switch_to_window(1)  # next window tab
    help_prod_title1 = find_element('help_product_title1_whats_new_new_tab_xpath')
    help_prod_titles2 = find_elements('help_product_titles_whats_new_new_tab_xpath')

    help_prod_titles = [help_prod_title1]
    help_prod_titles.extend(help_prod_titles2)

    for prod_title in help_prod_titles[0:-1]:
        highlight_element(prod_title)
    capture_screenshot(test_file_name)
    switch_to_window(0)  # default window


@pytest.mark.run(order=3)
def test_shutdown(fetch_url):
    click('shutdown_product_title1_xpath')
    time.sleep(2)
    highlight_element(find_element('shutdown_product_title2_xpath'))
    capture_screenshot(test_file_name)


@pytest.mark.run(order=4)
def test_product_name():
    print('Traversed pages for ' + test_file_name + ' are:')
    redirect_urls = all_url_call()
    for redirect_url in redirect_urls:
        driver.get(redirect_url)
        driver.maximize_window()
        time.sleep(2)
        visited_pages = [redirect_url]
        val = properties('product_title_class_name')
        prod_title = driver.find_element_by_class_name(val)
        highlight_element(prod_title)
        capture_screenshot(test_file_name)
        for page in visited_pages:
            print(page)
