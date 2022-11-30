import json
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select


class LoginPage:
    myjsonfile = open('/home/shraddha/PycharmProjects/pythonProject/demo_Project/pageObjects/webelements.json', 'r')
    jsondata = myjsonfile.read()

    obj = json.loads(jsondata)

    textbox_username=obj["textbox_username_id"]
    textbox_pass=obj["textbox_pass_id"]
    button_login=obj["button_login_id"]
    Homepage_logo=obj["Homepage_xpath"]
    add_to_cart=obj["add_to_cart_xpath"]
    go_to_cart=obj["go_to_cart_xpath"]
    continue_shopping_id=obj["continue_shopping_id"]
    second_item_id=obj["second_item_id"]
    checkout_button_id=obj["checkout_button_id"]
    FirstName_id=obj["FirstName_id"]
    Last_name_id=obj["Last_name_id"]
    postal_code_id=obj["postal_code_id"]
    continue_button_id=obj["continue_button_id"]
    finish_button = obj["Finish_button_id"]
    add_to_cart_price=obj["add_to_cart_price_xpath"]
    go_to_cart_price=obj["go_to_cart_price_xpath"]
    Radio_button=obj["Radio_button_xpath"]
    checkbox_button=obj["checkbox_button_name"]
    sec_item_name=obj["sec_item_name_linkText"]
    frames_linkText=obj["frames_linkText"]
    WindowHandling_linkText=obj["windowHandling_linkText"]
    file_browse=obj["file_browse_xpath"]
    dropdown_id=obj["dropdown_id"]
    drag_drop_from=obj["dragdrop_from"]
    drag_drop_to=obj["dragdrop_to"]
    search_item_id=obj["search_item_id"]
    search_item_xpath=obj["search_item_xpath"]
    mouseAction1_id=obj["mouseAction1_id"]
    mouseaction2_linkText=obj["mouseaction2_linkText"]


    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(by=By.ID, value=self.textbox_username).clear()
        self.driver.find_element(by=By.ID, value=self.textbox_username).send_keys(username)

    def setUserpassword(self,password):
        self.driver.find_element(by=By.ID, value=self.textbox_pass).clear()
        self.driver.find_element(by=By.ID, value=self.textbox_pass).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(by=By.ID, value=self.button_login).click()

    def verifylogo(self):
        logoPresent=self.driver.find_element(by=By.XPATH, value=self.Homepage_logo)
        #print(logoPresent.is_displayed())
        return logoPresent.is_displayed()

    def Addtocart(self):
        self.driver.find_element(by=By.XPATH, value=self.add_to_cart).click()

    def Gotocart(self):
        self.driver.find_element(by=By.XPATH, value=self.go_to_cart).click()

    def continue_shopping(self):
        butn=self.driver.find_element(by=By.ID, value=self.continue_shopping_id)
        butn.click()

    def second_product(self):
        sec_item=self.driver.find_element(by=By.ID, value=self.second_item_id)
        sec_item.click()


    def checkout(self):
        self.driver.find_element(by=By.ID, value=self.checkout_button_id).click()

    def setFirstName(self,firstname):
        self.driver.find_element(by=By.ID, value=self.FirstName_id).clear()
        self.driver.find_element(by=By.ID, value=self.FirstName_id).send_keys(firstname)

    def setlastName(self,lastname):
        self.driver.find_element(by=By.ID, value=self.Last_name_id).clear()
        self.driver.find_element(by=By.ID, value=self.Last_name_id).send_keys(lastname)

    def setpostalcode(self,poastalcode):
        self.driver.find_element(by=By.ID, value=self.postal_code_id).clear()
        self.driver.find_element(by=By.ID, value=self.postal_code_id).send_keys(poastalcode)

    def continue_button(self):
        self.driver.find_element(by=By.ID, value=self.continue_button_id).click()

    def Finish_button(self):
        self.driver.find_element(by=By.ID, value=self.finish_button).click()
        # pageSource = self.driver.page_source
        # #print(pageSource)
        # if "THANK YOU FOR YOUR ORDER" in pageSource:
        #     return True
        # else:
        #     return False

    def Add_to_cart_price(self):
        AddtocartPrice=self.driver.find_element(by=By.XPATH, value=self.add_to_cart_price)
        #print(res.text)
        return AddtocartPrice.text

    def Go_to_cart_price(self):
        GotocartPrice=self.driver.find_element(by=By.XPATH, value=self.go_to_cart_price)
        #print(res.text)
        return GotocartPrice.text

    def Radiobutton(self):
        button=self.driver.find_element(by=By.XPATH, value=self.Radio_button)
        button.click()
        #print(button.is_selected())
        return button.is_selected()

    def Checkboxbutton(self):
        button1=self.driver.find_element(by=By.NAME, value=self.checkbox_button)
        button1.click()
        #print(button1.is_selected())
        return button1.is_selected()

    def Frame(self):
        self.driver.switch_to.frame("classFrame")
        self.driver.find_element(by=By.LINK_TEXT, value=self.frames_linkText).click()

    def WindowHanling(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.WindowHandling_linkText).click()
        chwnd = self.driver.window_handles[1]
        self.driver.switch_to.window(chwnd)

    def file_upload(self,filename):
        file_button=self.driver.find_element(by=By.XPATH, value=self.file_browse)
        file_button.send_keys(filename)
        #print(file_button.is_displayed())
        return file_button.is_displayed()


    def dropdown(self):
        dropdown_button=self.driver.find_element(by=By.ID, value=self.dropdown_id)
        res=Select(dropdown_button)
        res.select_by_index(1)
        print(len(res.options))
        all_options = res.options
        newlist=[]
        for option in all_options:
            #print(option.text)
            newlist.append(option.text)
        return newlist


    def text_visible(self):
        pageSource = self.driver.page_source
        #print(pageSource)
        if "All the editions can run on the computer alone" in pageSource:
            print("it is present")
            return True
        else:
            print("it is not present")
            return False



    def Actions_test(self):
        ele1=self.driver.find_element(by=By.ID, value=self.drag_drop_from)
        ele2=self.driver.find_element(by=By.ID, value=self.drag_drop_to)
        actions2 = ActionChains(self.driver)
        actions2.click_and_hold(ele1).move_to_element(ele2).pause(2).move_by_offset(20, 20).release().perform()
        return True
        #actions2.drag_and_drop(ele1, ele2).perform()      #Second Method
        # actions2.move_to_element(ele1)                    # third Method
        # actions2.click(ele2)
        # actions2.perform()

    def search_item(self,search_product):
        self.driver.find_element(by=By.ID, value=self.search_item_id).send_keys(search_product)

    def search_button(self):
        self.driver.find_element(by=By.XPATH, value=self.search_item_xpath).click()

    def search_product(self):
        pageSource = self.driver.page_source
        if "14.1-inch Laptop" in pageSource:
            return True
        else:
            return False

    def Mouse_Actions(self):
        ele1 = self.driver.find_element(by=By.ID, value=self.mouseAction1_id)
        actions2 = ActionChains(self.driver)
        actions2.move_to_element(ele1)
        actions2.perform()
        ele2 = self.driver.find_element(by=By.LINK_TEXT, value=self.mouseaction2_linkText)
        actions2.move_to_element(ele2)
        actions2.perform()





