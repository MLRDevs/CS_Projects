# Alex Miller
# plays 2048 by going up, right, down, left and repeats

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("Starting...")
driver = webdriver.Firefox()
driver.get('https://play2048.co')

# Get the body element
body = driver.find_element_by_tag_name('html')

# Keep playing the game
while 1:
    body.send_keys(Keys.UP)
    body.send_keys(Keys.RIGHT)
    body.send_keys(Keys.DOWN)
    body.send_keys(Keys.LEFT)

    if driver.find_elements_by_class_name("game-over"):
        break

print("End of game")
sleep(1)
print(f"Your score was: {driver.find_element_by_class_name('score-container').text.split('+')[0]}")
print("Closing browser")
sleep(3)
driver.close()
