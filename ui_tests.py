import unittest
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class FlightUiTest(TestCase):
    from_input_css = "[id='headlessui-combobox-input-:Rq9lla:']"
    to_input_css = "[id='headlessui-combobox-input-:Rqhlla:']"
    flight_box_css = "[class*='overflow-hidden']"
    flight_result_text_css = "[class='mb-10']"

    def test_from_to_should_be_distinct(self):
        browser = webdriver.Chrome()
        browser.get("https://flights-app.pages.dev/")
        from_input = browser.find_element(By.CSS_SELECTOR, self.from_input_css)
        from_input.send_keys("Istanbul")
        from_input.send_keys(Keys.ENTER)

        to_input = browser.find_element(By.CSS_SELECTOR, self.to_input_css)
        to_input.send_keys("Istanbul")
        to_input.send_keys(Keys.ENTER)

        assert ("Bu iki şehir arasında uçuş bulunmuyor. Başka iki şehir seçmeyi deneyebilirsiniz." not in
                browser.page_source), "The cities should not be same, yet they are."
        browser.close()

    def test_items_found_equals_to_text(self):
        browser = webdriver.Chrome()
        browser.get("https://flights-app.pages.dev/")
        from_input = browser.find_element(By.CSS_SELECTOR, self.from_input_css)
        from_input.send_keys("Istanbul")
        from_input.send_keys(Keys.ENTER)

        to_input = browser.find_element(By.CSS_SELECTOR, self.to_input_css)
        to_input.send_keys("Los Angeles")
        to_input.send_keys(Keys.ENTER)

        flight_result_text = browser.find_element(By.CSS_SELECTOR, self.flight_result_text_css).text
        flight_boxes = browser.find_elements(By.CSS_SELECTOR, self.flight_box_css)
        assert int(flight_result_text[6]) == len(flight_boxes)
        browser.close()

    def test_no_flight_found(self):
        browser = webdriver.Chrome()
        browser.get("https://flights-app.pages.dev/")
        from_input = browser.find_element(By.CSS_SELECTOR, self.from_input_css)
        from_input.send_keys("Paris")
        from_input.send_keys(Keys.ENTER)

        to_input = browser.find_element(By.CSS_SELECTOR, self.to_input_css)
        to_input.send_keys("Madrid")
        to_input.send_keys(Keys.ENTER)

        assert ("Bu iki şehir arasında uçuş bulunmuyor. Başka iki şehir seçmeyi deneyebilirsiniz." in
                browser.page_source)
        browser.close()


if __name__ == "__main__":
    unittest.main()
