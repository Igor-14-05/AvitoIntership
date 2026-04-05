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
    test_category = "Электроника"
    page.goto("https://cerulean-praline-8e5aa6.netlify.app")
    category_select = page.locator('select').filter(has_text="Все категории")
    category_select.select_option(label=test_category)
    cards = page.locator('[class*="_card__category_15fhn_259"]')
    try:
        cards.first.wait_for(state="attached", timeout=5000)
    except:
        print("Нет карточек товаров после фильтрации")
        no_results = page.get_by_text("Ничего не найдено")
        assert no_results.is_visible(), "Нет ни карточек, ни сообщения об отсутствии"
        return
    categories_texts = cards.all_inner_texts()
    print(categories_texts)

    assert len(categories_texts) > 0, "Список категорий пуст"
    for category in categories_texts:
        assert test_category <= category

