from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=r'C:\Users\tester\AppData\Local\Programs\Python\Python35-32\geckodriver.exe',
                           firefox_binary=r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
driver.get("http://192.168.4.229/")
driver.maximize_window()


# Объекты стартовой страницы
class StartPage:
    login = driver.find_element_by_xpath(
        '/html/body/div[2]/ul/li[2]/div[2]/div[1]/div/form/table/tbody/tr[1]/td[2]/div')
    password = driver.find_element_by_xpath(
        '/html/body/div[2]/ul/li[2]/div[2]/div[1]/div/form/table/tbody/tr[2]/td[2]/div/div[2]')
    enterButton = driver.find_element_by_xpath(
        '/html/body/div[2]/ul/li[2]/div[2]/div[1]/div/form/table/tbody/tr[4]/td[2]/span')
    regButton = driver.find_element_by_xpath(
        '/html/body/div[2]/ul/li[2]/div[2]/div[1]/div/form/table/tbody/tr[5]/td[2]/span/span/span')
    approveRegButton = driver.find_element_by_xpath(
        '/html/body/div[2]/ul/li[2]/div[2]/div[2]/div/form/table/tbody/tr[7]/td[2]/span')
    old_page = driver.find_element_by_tag_name('html')
    backToLoginButton = driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/div[1]/span/span')


# Ожидание Элемента, основаное на экзепшине об его отсутствии
def wait_element(waiting_element, waiting_podelement, param='()'):
    timer = time.time()
    while timer <= timer + 7:
        try:
            x = waiting_element + '.' + waiting_podelement + param + '.is_displayed()'
            eval(x)
        except NoSuchElementException:
            time.sleep(1)
            print('Хозяин, ничего не вышло')
        else:
            print('дело сделано')
            break
        finally:

            time.sleep(1)


# Объекты эелементов основной панели табов
class tabs:
    def objectPanel(self):
        objectPanel = driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div[1]')
        return objectPanel

    def historyPanel(self):
        historyPanel = driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div[2]')
        return historyPanel

    def notificationsPanel(self):
        notificationsPanel = driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div[3]')
        return notificationsPanel

    def geofencesPanel(self):
        geofencesPanel = driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div[4]')
        return geofencesPanel

    def routesPanel(self):
        routesPanel = driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div[5]')
        return routesPanel

    def placesPanel(self):
        placesPanel = driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div[6]')
        return placesPanel

    def relayPanel(self):
        relayPanel = driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div[7]')
        return relayPanel

    def tasksPanel(self):
        tasksPanel = driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div[8]')
        return tasksPanel

    def reportsPanel(self):
        reportsPanel = driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div[9]')
        return reportsPanel


# Дополнительные элементы на панели табов (уведомления,инструменты,настройки,администрирование)
class secondTabs:
    # Параметром передается та панель, которую нужно открыть например С - компании, U - Пользователи, L - Слои, R- Роли
    def adminTools(self, param):

        def adminThing(param):
            if param == 'C':
                def C():
                    obj = driver.find_element_by_xpath('/html/body/div[12]/table/tbody/tr[1]/td[2]')
                    return obj

                return C()

            if param == 'U':
                def U():
                    obj = driver.find_element_by_xpath('/html/body/div[12]/table/tbody/tr[2]/td[2]')
                    return obj

                return U()

            if param == 'R':
                def R():
                    obj = driver.find_element_by_xpath('/html/body/div[12]/table/tbody/tr[3]/td[2]')
                    return obj

                return R()

            if param == 'L':
                def L():
                    obj = driver.find_element_by_xpath('/html/body/div[12]/table/tbody/tr[4]/td[2]')
                    return obj

                return L()

        return adminThing(param)

    # Кнопка администрирование
    def adminButton(self):
        adminButton = driver.find_element_by_xpath('/html/body/div[10]/div[3]/div/div[4]/span[1]/span')
        return adminButton


# Класс Элементов панели администрирования компаний
class companyAdmin:
    def addCompButton(self):
        addComp = driver.find_element_by_xpath(
            '/html/body/div[13]/div[2]/div/div/div[3]/div[2]/span[1]/span/span/span[3]')
        return addComp

    def compName(self):
        CompName = driver.find_element_by_xpath(
            '/html/body/div[13]/div[2]/div/div/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/div/div[2]')
        return CompName

    def parenGr(self, ):
        parent = driver.find_element_by_xpath(
            '/html/body/div[13]/div[2]/div/div/div[3]/div[1]/form/table/tbody/tr[2]/td[2]/div/div[1]')
        return parent

    def parenGrName(self, param):
        parent = driver.find_element_by_xpath(
            './/*[contains(@class, "gridxTreeExpandoContent") and text()="%s"]' % param)
        return parent

    def maxUsrChbx(self):
        Chbx = driver.find_element_by_xpath(
            './/tr/td/label[@for="userLimit"]/../..//input[contains(@id, "dijit_form_CheckBox")]')
        return Chbx

    def maxUsr(self):
        max = driver.find_element_by_xpath(
            './/tr/td/label[@for="userLimit"]/../..//input[contains(@id, "dijit_form_NumberTextBox")]')
        return max

    def maxObjChbx(self):
        Chbx = driver.find_element_by_xpath(
            './/tr/td/label[@for="deviceLimit"]/../..//input[contains(@id, "dijit_form_CheckBox")]')
        return Chbx

    def maxObj(self):
        max = driver.find_element_by_xpath(
            './/tr/td/label[@for="deviceLimit"]/../..//input[contains(@id, "dijit_form_NumberTextBox")]')
        return max

    def licenseExpChbx(self):
        Chbx = driver.find_element_by_xpath(
            './/tr/td/label[@for="expireDate"]/../..//input[contains(@id, "dijit_form_CheckBox")]')
        return Chbx

    def licenseExpDate(self):
        Date = driver.find_element_by_xpath(
            './/tr/td/label[@for="expireDate"]/../..//input[contains(@id, "dijit_form_DateTextBox")]')
        return Date

    def saveButton(self):
        saveB = driver.find_element_by_xpath('.//div//span[text()="Сохранить"]/..')
        return saveB

    def cancelButton(self):
        cancel = driver.find_element_by_xpath('.//div//span[text()="Отмена"]/..')
        return cancel

    def searchField(self):
        searchField = driver.find_element_by_xpath('.//div[contains(@role, "toolbar")]/div[1]/div[3]/div[1]/input')
        return searchField

    def companyInGrid(self, companyName):
        companyInGrid = driver.find_element_by_xpath(
            './/div[contains(@class, "gridxBody")]//div[contains(@class, "gridxCell")]//b[text()="%s"]' % companyName)
        return companyInGrid

    def editButton(self):
        editButton = driver.find_element_by_xpath(
            './/div[contains(@class, "buttonContainer")]/span[2]/span/span/span[3]')
        return editButton

    def companyCheck(self, name, maxUsers, maxObjects, licenseExpDate, ):
        NameIn = driver.find_element_by_xpath(
            './/div[contains(@class, "gridxBody")]//div[contains(@class, "gridxCell")]//b[text()="%s"]' % name).text
        # GroupIn=driver.find_element_by_xpath()
        MaxUsersIn = driver.find_element_by_xpath(
            './/div[contains(@class, "gridxBody")]//div[contains(@class, "gridxCell")]//b[text()="%s"]/../../../../../tr/td[4]' % name).text
        MaxObjectsIn = driver.find_element_by_xpath(
            './/div[contains(@class, "gridxBody")]//div[contains(@class, "gridxCell")]//b[text()="%s"]/../../../../../tr/td[5]' % name).text
        LicenseExpIn = driver.find_element_by_xpath(
            './/div[contains(@class, "gridxBody")]//div[contains(@class, "gridxCell")]//b[text()="%s"]/../../../../../tr/td[7]' % name).text
        if name == NameIn:
            flagName = 'Name-OK'
        else:
            flagName = 'Name-Error'

        if maxUsers == MaxUsersIn:
            flagUsers = 'Users-OK'
        else:
            flagUsers = 'Users-Error'
        if maxObjects == MaxObjectsIn:
            flagObjects = 'Objects-OK'
        else:
            flagObjects = 'Objects-Error'
        if licenseExpDate == LicenseExpIn:
            flagLicense = 'ExpDate-OK'
        else:
            flagLicense = 'ExpDate-Error'

        return print(flagName, flagUsers, flagObjects, flagLicense)


Obj1 = StartPage()
tabs = tabs()
secondTabs = secondTabs()
wait_element('Obj1', 'regButton', param='')
Obj1.regButton.click()
wait_element('Obj1', 'backToLoginButton', param='')
Obj1.backToLoginButton.click()
Obj1.login.click()
Obj1.login.send_keys("root")
Obj1.password.click()
Obj1.password.send_keys('1234')
Obj1.enterButton.click()
wait_element('tabs', 'historyPanel')
secondTabs.adminButton().click()
wait_element('secondTabs', 'adminTools', param='("C")')
secondTabs.adminTools('C').click()
CompAd = companyAdmin()
wait_element('CompAd', 'addCompButton')
CompAd.addCompButton().click()
wait_element('CompAd', 'saveButton')
CompAd.compName().click()
CompAd.compName().send_keys('abrraCadabra')
CompAd.parenGr().click()
wait_element('CompAd', 'parenGrName', param='("test0607")')
CompAd.parenGrName('test0607').click()
CompAd.maxUsrChbx().click()
CompAd.maxUsr().click()
CompAd.maxUsr().send_keys('3')
CompAd.maxObjChbx().click()
CompAd.maxObj().click()
CompAd.maxObj().send_keys('10')
CompAd.licenseExpDate().click()
CompAd.licenseExpDate().clear()
CompAd.licenseExpDate().send_keys('22.02.2020')
CompAd.saveButton().click()
CompAd.searchField().click()
time.sleep(3)
CompAd.searchField().send_keys('abrraCadabra')
CompAd.searchField().send_keys(Keys.ENTER)
wait_element('CompAd', 'companyInGrid', param='("abrraCadabra")')
CompAd.companyCheck('abrraCadabra', '3', '10', '22.02.2020')
