from selenium import webdriver

my_driver = webdriver.Chrome()
my_driver.get("https://translate.google.com/")
my_driver.find_element_by_class_name("er8xn").send_keys("חתול")
my_driver.find_element_by_id("gt-submit").click()



#my_driver.get("http://www.walla.co.il")

#title = my_driver.title
#my_driver.refresh()
#if title == my_driver.title:get
  #  print("equal")

