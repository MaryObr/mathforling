from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import string
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1080")
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("https://shakhty-media.ru/category/novosti/obchestvo/")
element = WebDriverWait(driver=driver, timeout=5).until(
    EC.presence_of_element_located((By.XPATH, "//h5"))
)
for i in range(130):
    driver.find_element(By.ID, "loadmore_listnews").click()
    time.sleep(5)
all_links = [my_elem.get_attribute("href") for my_elem in driver.find_elements(By.XPATH, "//a")]
block = ["category", "konkursy", "reklama", "@", "=", "market", "wa.me", "t.me", "kontakty", "login", "vk", "ok", "zen","liveinternet", "politika-konfidentsialnosti", "feed"]
links = []
for i in all_links:
    x = 0
    for j in block:
        if j in i:
            x +=1
    if x == 0 and "https:" in i and i not in links:
        links.append(i)



for i in range(1, len(links)):
    texts = ""
    driver.get(f"{links[i]}")
    element = WebDriverWait(driver=driver, timeout=10).until(
        EC.presence_of_element_located((By.XPATH, "//p"))
    )
    body = driver.find_element(By.CSS_SELECTOR, ".post-content.offset-md-1")
    texts = "".join(
        [my_elem.text.replace("\n", "").replace(".", " ").replace("«", "").replace("»", "").lower().translate(str.maketrans('', '', string.punctuation)) for my_elem in body.find_elements(By.TAG_NAME, "p") if my_elem.text != ''])
    with open("shachty1.txt", "a+", encoding="utf-8") as f:
        f.write(texts)
        f.write("\n")

