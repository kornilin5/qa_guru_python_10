from selene import browser, be, have
import pytest
def test_search_text(options_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python. Contribute to yashaka/selene development by'))

def test_search_text_two(options_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('asdawerrgjsokglwkjkgnfahdadjaisdoajdsoajdhadasdasdadsad12313qawadsasad').press_enter()
    browser.element('#botstuff > div > div.mnr-c > div > p:nth-child(1)').should(have.text('ничего не найдено.'))
    #testnewbranch
def test_search_text_three(options_browser):
    browser.open('https://yandex.ru') #ищменио ссылку на яндекс# 
    browser.element('[name="text"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[class="serp-item"]').should(have.text('User-oriented Web UI browser tests in Python. Contribute to yashaka/selene development by'))