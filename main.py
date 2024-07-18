from flask import Flask, Response
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions  # Import for Chrome options

app = Flask(__name__)


def selenium_task():
  options = ChromeOptions()  # Change to ChromeOptions
  options.add_argument("--headless")
  options.add_argument("--disable-gpu")
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  driver = webdriver.Chrome(options=options)  # Change to webdriver.Chrome

  # Perform the selenium task
  driver.get("https://www.cricbuzz.com/")
  
  st=driver.find_element("xpath",'//*[@id="cb-main-menu"]/a[2]')
  print(st.text)

  driver.close()


@app.route('/selenium')
def selenium_endpoint():
  page_source = selenium_task()
  return Response(page_source, mimetype='text/html')


@app.route('/')
def index():
  selenium_task()
  return "200 OK"


if __name__ == '__main__':
  app.run(host='0.0.0.0')
