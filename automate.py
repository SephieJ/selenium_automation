from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time


# User credentials
url = 'https://fyndiq.se/merchant/login/'
username = 'papenam'
password = 'Tomatsoppa77!'



#####################################################################################################
# Create directory for Januari
dir_name = 'Januari'

try:
    os.mkdir(dir_name)
    print("Directory " , dir_name ,  " created")
except FileExistsError:
    print("Directory " , dir_name ,  " already exists")

# Open Chrome with specific download path (Januari)
driver = '/home/sephie/Downloads/chromedriver'
chrome_options = webdriver.ChromeOptions()
path = '/home/sephie/Desktop/Januari'
prefs = {'download.default_directory': path}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(executable_path=driver, chrome_options=chrome_options)

browser.get(url)

# Login Process
browser.find_element_by_id('id_username').send_keys(username)
browser.find_element_by_id('id_password').send_keys(password)
browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
time.sleep(2)

# Download from Page 2 of Januari
browser.get('https://fyndiq.se/merchant/merchantpayment/merchantpayment/?p=2')
td_rows = browser.find_elements_by_class_name('field-to_be_paid_at')
td_pdf = browser.find_elements_by_class_name('field-download_pdf')

for row, pdf in zip(td_rows, td_pdf):
    if '2018' and 'Januari' in row.text:
        pdf.click()
time.sleep(2)

# Download from Page 1 of Januari
browser.get('https://fyndiq.se/merchant/merchantpayment/merchantpayment/?p=1')
td_rows = browser.find_elements_by_class_name('field-to_be_paid_at')
td_pdf = browser.find_elements_by_class_name('field-download_pdf')

for row, pdf in zip(td_rows, td_pdf):
    if '2018' and 'Januari' in row.text:
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
print('Done downloading Januari files')
# End of download for Januari



#####################################################################################################
# Create directory for Februari
dir_name = 'Februari'

try:
    os.mkdir(dir_name)
    print("Directory " , dir_name ,  " created")
except FileExistsError:
    print("Directory " , dir_name ,  " already exists")

# Open Chrome with specific download path (Februari)
driver = '/home/sephie/Downloads/chromedriver'
chrome_options = webdriver.ChromeOptions()
path = '/home/sephie/Desktop/Februari'
prefs = {'download.default_directory': path}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(executable_path=driver, chrome_options=chrome_options)

browser.get(url)

# Login Process
browser.find_element_by_id('id_username').send_keys(username)
browser.find_element_by_id('id_password').send_keys(password)
browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
time.sleep(2)

# Download from Page 1 of Februari
browser.get('https://fyndiq.se/merchant/merchantpayment/merchantpayment/?p=1')
td_rows = browser.find_elements_by_class_name('field-to_be_paid_at')
td_pdf = browser.find_elements_by_class_name('field-download_pdf')

for row, pdf in zip(td_rows, td_pdf):
    if '2018' and 'Februari' in row.text:
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
print('Done downloading Februari files')
# End of download for Februari



#####################################################################################################
# Create directory for Mars
dir_name = 'Mars'

try:
    os.mkdir(dir_name)
    print("Directory " , dir_name ,  " created")
except FileExistsError:
    print("Directory " , dir_name ,  " already exists")

# Open Chrome with specific download path (Mars)
driver = '/home/sephie/Downloads/chromedriver'
chrome_options = webdriver.ChromeOptions()
path = '/home/sephie/Desktop/Mars'
prefs = {'download.default_directory': path}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(executable_path=driver, chrome_options=chrome_options)

browser.get(url)

# Login Process
browser.find_element_by_id('id_username').send_keys(username)
browser.find_element_by_id('id_password').send_keys(password)
browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
time.sleep(2)

# Download from Page 1 of Mars
browser.get('https://fyndiq.se/merchant/merchantpayment/merchantpayment/?p=1')
td_rows = browser.find_elements_by_class_name('field-to_be_paid_at')
td_pdf = browser.find_elements_by_class_name('field-download_pdf')

for row, pdf in zip(td_rows, td_pdf):
    if '2018' and 'Mars' in row.text:
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
print('Done downloading Mars files')
# End of download for Mars



#####################################################################################################
# Create directory for April
dir_name = 'April'

try:
    os.mkdir(dir_name)
    print("Directory " , dir_name ,  " created")
except FileExistsError:
    print("Directory " , dir_name ,  " already exists")

# Open Chrome with specific download path (April)
driver = '/home/sephie/Downloads/chromedriver'
chrome_options = webdriver.ChromeOptions()
path = '/home/sephie/Desktop/April'
prefs = {'download.default_directory': path}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(executable_path=driver, chrome_options=chrome_options)

browser.get(url)

# Login Process
browser.find_element_by_id('id_username').send_keys(username)
browser.find_element_by_id('id_password').send_keys(password)
browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
time.sleep(2)

# Download from Page 1 of April
browser.get('https://fyndiq.se/merchant/merchantpayment/merchantpayment/?p=1')
td_rows = browser.find_elements_by_class_name('field-to_be_paid_at')
td_pdf = browser.find_elements_by_class_name('field-download_pdf')

for row, pdf in zip(td_rows, td_pdf):
    if '2018' and 'April' in row.text:
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
print('Done downloading April files')
# End of download for April



#####################################################################################################
# Create directory for Maj
dir_name = 'Maj'

try:
    os.mkdir(dir_name)
    print("Directory " , dir_name ,  " created")
except FileExistsError:
    print("Directory " , dir_name ,  " already exists")

# Open Chrome with specific download path (Maj)
driver = '/home/sephie/Downloads/chromedriver'
chrome_options = webdriver.ChromeOptions()
path = '/home/sephie/Desktop/Maj'
prefs = {'download.default_directory': path}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(executable_path=driver, chrome_options=chrome_options)

browser.get(url)

# Login Process
browser.find_element_by_id('id_username').send_keys(username)
browser.find_element_by_id('id_password').send_keys(password)
browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
time.sleep(2)

# Download from Page 1 of Maj
browser.get('https://fyndiq.se/merchant/merchantpayment/merchantpayment/?p=1')
td_rows = browser.find_elements_by_class_name('field-to_be_paid_at')
td_pdf = browser.find_elements_by_class_name('field-download_pdf')

for row, pdf in zip(td_rows, td_pdf):
    if '2018' and 'Maj' in row.text:
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
print('Done downloading Maj files')
# End of download for Maj



#####################################################################################################
# Create directory for Juni
dir_name = 'Juni'

try:
    os.mkdir(dir_name)
    print("Directory " , dir_name ,  " created")
except FileExistsError:
    print("Directory " , dir_name ,  " already exists")

# Open Chrome with specific download path (Juni)
driver = '/home/sephie/Downloads/chromedriver'
chrome_options = webdriver.ChromeOptions()
path = '/home/sephie/Desktop/Juni'
prefs = {'download.default_directory': path}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(executable_path=driver, chrome_options=chrome_options)

browser.get(url)

# Login Process
browser.find_element_by_id('id_username').send_keys(username)
browser.find_element_by_id('id_password').send_keys(password)
browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
time.sleep(2)

# Download from Page 1 of Juni
browser.get('https://fyndiq.se/merchant/merchantpayment/merchantpayment/?p=1')
td_rows = browser.find_elements_by_class_name('field-to_be_paid_at')
td_pdf = browser.find_elements_by_class_name('field-download_pdf')

for row, pdf in zip(td_rows, td_pdf):
    if '2018' and 'Juni' in row.text:
        pdf.click()
time.sleep(2)

# Download from Page 0 of Juni
browser.get('https://fyndiq.se/merchant/merchantpayment/merchantpayment/?p=0')
td_rows = browser.find_elements_by_class_name('field-to_be_paid_at')
td_pdf = browser.find_elements_by_class_name('field-download_pdf')

for row, pdf in zip(td_rows, td_pdf):
    if '2018' and 'Juni' in row.text:
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
print('Done downloading Juni files')
# End of download for Juni



#####################################################################################################
# Create directory for Juli
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
browser.get('https://fyndiq.se/merchant/merchantpayment/merchantpayment/?p=0')
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



#####################################################################################################
# Create directory for Augusti
dir_name = 'Augusti'

try:
    os.mkdir(dir_name)
    print("Directory " , dir_name ,  " created")
except FileExistsError:
    print("Directory " , dir_name ,  " already exists")

# Open Chrome with specific download path (Augusti)
driver = '/home/sephie/Downloads/chromedriver'
chrome_options = webdriver.ChromeOptions()
path = '/home/sephie/Desktop/Augusti'
prefs = {'download.default_directory': path}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(executable_path=driver, chrome_options=chrome_options)

browser.get(url)

# Login Process
browser.find_element_by_id('id_username').send_keys(username)
browser.find_element_by_id('id_password').send_keys(password)
browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
time.sleep(2)

# Download from Page 1 of Augusti
browser.get('https://fyndiq.se/merchant/merchantpayment/merchantpayment/?p=0')
td_rows = browser.find_elements_by_class_name('field-to_be_paid_at')
td_pdf = browser.find_elements_by_class_name('field-download_pdf')

for row, pdf in zip(td_rows, td_pdf):
    if '2018' and 'Augusti' in row.text:
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
print('Done downloading Augusti files')
# End of download for Augusti



#####################################################################################################
# Create directory for September
dir_name = 'September'

try:
    os.mkdir(dir_name)
    print("Directory " , dir_name ,  " created")
except FileExistsError:
    print("Directory " , dir_name ,  " already exists")

# Open Chrome with specific download path (September)
driver = '/home/sephie/Downloads/chromedriver'
chrome_options = webdriver.ChromeOptions()
path = '/home/sephie/Desktop/September'
prefs = {'download.default_directory': path}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(executable_path=driver, chrome_options=chrome_options)

browser.get(url)

# Login Process
browser.find_element_by_id('id_username').send_keys(username)
browser.find_element_by_id('id_password').send_keys(password)
browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
time.sleep(2)

# Download from Page 1 of September
browser.get('https://fyndiq.se/merchant/merchantpayment/merchantpayment/?p=0')
td_rows = browser.find_elements_by_class_name('field-to_be_paid_at')
td_pdf = browser.find_elements_by_class_name('field-download_pdf')

for row, pdf in zip(td_rows, td_pdf):
    if '2018' and 'September' in row.text:
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
print('Done downloading September files')
# End of download for September



#####################################################################################################
# Create directory for Oktober
dir_name = 'Oktober'

try:
    os.mkdir(dir_name)
    print("Directory " , dir_name ,  " created")
except FileExistsError:
    print("Directory " , dir_name ,  " already exists")

# Open Chrome with specific download path (Oktober)
driver = '/home/sephie/Downloads/chromedriver'
chrome_options = webdriver.ChromeOptions()
path = '/home/sephie/Desktop/Oktober'
prefs = {'download.default_directory': path}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(executable_path=driver, chrome_options=chrome_options)

browser.get(url)

# Login Process
browser.find_element_by_id('id_username').send_keys(username)
browser.find_element_by_id('id_password').send_keys(password)
browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
time.sleep(2)

# Download from Page 1 of Oktober
browser.get('https://fyndiq.se/merchant/merchantpayment/merchantpayment/?p=0')
td_rows = browser.find_elements_by_class_name('field-to_be_paid_at')
td_pdf = browser.find_elements_by_class_name('field-download_pdf')

for row, pdf in zip(td_rows, td_pdf):
    if '2018' and 'Oktober' in row.text:
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
print('Done downloading Oktober files')
# End of download for Oktober



#####################################################################################################
# Create directory for November
dir_name = 'November'

try:
    os.mkdir(dir_name)
    print("Directory " , dir_name ,  " created")
except FileExistsError:
    print("Directory " , dir_name ,  " already exists")

# Open Chrome with specific download path (November)
driver = '/home/sephie/Downloads/chromedriver'
chrome_options = webdriver.ChromeOptions()
path = '/home/sephie/Desktop/November'
prefs = {'download.default_directory': path}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(executable_path=driver, chrome_options=chrome_options)

browser.get(url)

# Login Process
browser.find_element_by_id('id_username').send_keys(username)
browser.find_element_by_id('id_password').send_keys(password)
browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
time.sleep(2)

# Download from Page 1 of November
browser.get('https://fyndiq.se/merchant/merchantpayment/merchantpayment/?p=0')
td_rows = browser.find_elements_by_class_name('field-to_be_paid_at')
td_pdf = browser.find_elements_by_class_name('field-download_pdf')

for row, pdf in zip(td_rows, td_pdf):
    if '2018' and 'November' in row.text:
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
print('Done downloading November files')
# End of download for November
