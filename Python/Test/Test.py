from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.reddit.com/r/StoryTime/comments/12ir1tl/i_found_out_my_mom_was_using_my_identity/")
element = driver.find_element(By.CLASS_NAME, "post-content")
element.screenshot("foo.png")

driver.quit()
