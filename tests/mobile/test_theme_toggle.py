def test_theme_toggle_mobile(page: Page):
    # Мобильный viewport
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto("/")

    # Предполагаем селектор переключателя темы
    theme_toggle = page.locator('button[aria-label*="тема"]')  # или data-testid
    theme_toggle.click()

    # Проверка тёмной темы
    expect(page.locator('body')).to_have_class(re.compile(r'dark'))
    dark_bg = page.evaluate('() => getComputedStyle(document.body).backgroundColor')

    theme_toggle.click()
    light_bg = page.evaluate('() => getComputedStyle(document.body).backgroundColor')

    assert dark_bg != light_bg, "Цвет фона не изменился при переключении темы"