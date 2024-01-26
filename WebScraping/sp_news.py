from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd

try:
    website = 'https://www.thesun.co.uk/sport/football'
    path = "C:\\Users\\ecernare\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

    # Headless mode
    options = Options()
    options.headless = True

    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(website)

    containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

    titles = []
    subtitles = []
    links = []

    for container in containers:
        # Busca el título
        title_elements = container.find_elements(by="xpath", value='./a/span')
        title = title_elements[0].text if title_elements else "Title not found"
        titles.append(title)

        # Busca el subtítulo
        subtitle_elements = container.find_elements(by="xpath", value='./a/h3')
        subtitle = subtitle_elements[0].text if subtitle_elements else "SubTitle not found"
        subtitles.append(subtitle)

        # Busca el enlace
        link_elements = container.find_elements(by="xpath", value='./a')
        link = link_elements[0].get_attribute("href") if link_elements else "Link not found"
        links.append(link)

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()

my_dictionary = {'title': titles, 'subtitles': subtitles, 'link': links}
df_news = pd.DataFrame(my_dictionary)
df_news.to_csv('news-headless.csv')
