import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-incognito")
driver = webdriver.Chrome(
    executable_path="C:\\Users\\Nick\\Desktop\\chromedriver_win32\chromedriver.exe", chrome_options=chrome_options)

# Open the web page
driver.get('https://www.surveymonkey.com/r/SB_People')
time.sleep(2)

# Find the okay button and click it
okay_btn = driver.find_element_by_css_selector("button.ok-button")
okay_btn.click()
time.sleep(1)

# Find the button corresponding to the answer
correct_answer_btn = driver.find_element_by_id('431623151_3118750202')
actions = ActionChains(driver)
actions.move_to_element(correct_answer_btn).click().perform()

time.sleep(1)


# Go through all the other answers and select randomly
available_answers = driver.find_elements_by_css_selector(
    ".question-single-choice-radio qn question vertical, [data-qnumber=2]")
actions = ActionChains(driver)
actions.move_to_element(available_answers[1]).click().perform()
# answer-option-cell

# driver.quit()
