from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()
dr.get("C:/Users/sharona/Downloads/tip_calc/tip_calc/index.html")
billamt = dr.find_element(by="id",value="billamt")
billamt.send_keys("100")
dr.find_element(by="xpath",value="//*[@id=\"serviceQual\"]/option[3]").click()
dr.find_element(by="id", value="peopleamt").send_keys("5")
dr.find_element(by="id", value="musicQual").send_keys("5")
dr.find_element(by="id", value="calculate").click()
actual = dr.find_element(by="id",value="tip").text
expected = "9"
assert expected == actual
# if expected == actual:
#     print("all cool")
# else:
#     print("wrong tip")
#print(actual)
# for i in range(5):
#     dr.refresh()
#     sleep(2)
sleep(10)