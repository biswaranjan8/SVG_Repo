from selenium.webdriver import Chrome
import time

driver = Chrome(executable_path="../Driver/chromedriver.exe")


# It's own Django application
driver.get("http://127.0.0.1:8000/")
# driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(10)


color = driver.find_element_by_xpath("//*[name()='svg']//*[local-name()='rect']").get_attribute("fill")
print(color)
# First approach
# data = driver.find_element_by_xpath("//div[@class='container']//*[@id='pointline']")
# print(data.text)
# Second approach
data = driver.find_element_by_xpath("//*[name()='svg']//*[local-name()='text' and @id='pointline']")
print(data.text)

#################### Filpkart search Icon #######################################
# time.sleep(5)
# driver.find_element_by_xpath("//div[@class='_2QfC02']//button").click()
# time.sleep(1)
# driver.find_element_by_xpath("//div[@class='_3OO5Xc']/input").send_keys("pregnancy belt after delivery")
# time.sleep(1)
# driver.find_element_by_xpath("//*[name()='svg']//*[local-name()='path' and @class='_34RNph'][1]").click()

driver.close()

