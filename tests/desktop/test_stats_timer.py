from playwright.sync_api import Page, expect


def test_stats_timer_controls_update(page: Page):
    page.goto("https://cerulean-praline-8e5aa6.netlify.app")
    stats_link = page.get_by_role("link", name="Статистика")
    stats_link.click()
    page.wait_for_url("**/stats")

    page.wait_for_timeout(10000)
    initial_time = page.locator('[class*="_timeValue_ir5wu_112"]').inner_text()
    refresh_button = page.get_by_role("button", name="Обновить сейчас")
    refresh_button.click()
    page.wait_for_timeout(2000)
    new_time = page.locator('[class*="_timeValue_ir5wu_112"]').inner_text()
    print(initial_time)
    print(new_time)
    if initial_time[0] == new_time[0]:
        assert initial_time[2:] < new_time[2:]
    elif initial_time[0] > new_time[0]:
        assert initial_time[0] < new_time[0]

def test_stats_timer_controls_stop(page: Page):
    page.goto("https://cerulean-praline-8e5aa6.netlify.app")
    stats_link = page.get_by_role("link", name="Статистика")
    stats_link.click()
    page.wait_for_url("**/stats")

    page.wait_for_timeout(10000)
    stop_button = page.get_by_role("button", name="Отключить автообновление")
    stop_button.click()
    stop_text = page.locator('[class*="_disabled_ir5wu_136"]').inner_text()
    assert stop_text == "Автообновление выключено"
