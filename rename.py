from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time


url = 'https://fyndiq.se/merchant/login/'
username = 'papenam'
password = 'Tomatsoppa77!'

dir_name = 'Juli'

try:
    os.mkdir(dir_name)
    print("Directory " , dir_name ,  " created")
except FileExistsError:
    print("Directory " , dir_name ,  " already exists")

# Open Chrome with specific download path (Juli)
driver = '/home/sephie/Downloads/chromedriver'
chrome_options = webdriver.ChromeOptions()
path = '/home/sephie/Desktop/Juli'
prefs = {'download.default_directory': path}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(executable_path=driver, chrome_options=chrome_options)

browser.get(url)

# Login Process
browser.find_element_by_id('id_username').send_keys(username)
browser.find_element_by_id('id_password').send_keys(password)
browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
time.sleep(2)

# Download from Page 1 of Juli
browser.get('https://fyndiq.se/merchant/merchantpayment/merchantpayment/?p=1')
td_rows = browser.find_elements_by_class_name('field-to_be_paid_at')
td_pdf = browser.find_elements_by_class_name('field-download_pdf')

for row, pdf in zip(td_rows, td_pdf):
    if '2018' and 'Juli' in row.text:
        pdf.click()
time.sleep(2)

# Renaming downloaded files
os.chdir(path)
for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_report, f_year, f_month, f_day = f_name.split('-')
    f_report = f_report.replace('utbetalning', 'paymentreport')
    f_year = f_year.strip()
    f_month = f_month.strip()
    f_day = f_day.strip()

    new_name = '{}_{}.{}.{}{}'.format(f_report, f_year, f_month, f_day, f_ext)
    os.rename(f, new_name)

time.sleep(3)
browser.close()
print('Done downloading Juli files')
# End of download for Juli
