import re
from playwright.sync_api import Page, expect


def test_theme_toggle_mobile(page: Page):
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto("https://cerulean-praline-8e5aa6.netlify.app")
    theme_toggle = page.locator('button[aria-label*="Switch to dark theme"]')
    theme_toggle.click()
    assert "dark" == page.evaluate('() => document.documentElement.getAttribute("data-theme")'), "Цвет фона не изменился при переключении темы"