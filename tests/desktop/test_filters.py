from playwright.sync_api import Page


def test_price_range_filter(page: Page):
    page.goto("https://cerulean-praline-8e5aa6.netlify.app")
    page.get_by_placeholder("От").fill("1000")
    page.get_by_placeholder("До").fill("5000")

    page.wait_for_timeout(1500)

    price_texts = page.locator('[class*="_card__price"]').all_inner_texts()
    prices = [int(''.join(filter(str.isdigit, text))) for text in price_texts]

    for price_str in prices:
        assert 1000 <= int(price_str) <= 5000, f"Цена {price_str} вышла за диапазон"


def test_price_category_filter(page: Page):
    page.goto("https://cerulean-praline-8e5aa6.netlify.app")
    select = page.locator('[class*="_filters__select_1iunh_21"]')
    select.select_option(label = "Электроника")

    price_texts = page.locator('[class*="_card__category"]').all_inner_texts()
    print(price_texts)
    # prices = [int(''.join(filter(str.isdigit, text))) for text in price_texts]

    # for price_str in prices:
    #     assert 1000 <= int(price_str) <= 5000, f"Цена {price_str} вышла за диапазон"

