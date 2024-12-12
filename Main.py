
#==========================================NOC WALL AUTO LOGINS============================================

from bengucci import ben
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
#import pyautogui
from selenium.webdriver import Keys
#from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options
import subprocess
import os
#from pynput.keyboard import Key, Controller
import win32api
import win32com.client
#from test import ben
import py_compile
from pywinauto import keyboard
from comtypes import stream

def openSolars():
    solarwind_links = [
        #'http://orion.dhs.lacounty.gov/Orion/Login.aspx?ReturnUrl=%2fOrion%2fSummaryView.aspx%3fViewID%3d106&ViewID=106',
        'http://orion.dhs.lacounty.gov/Orion/SummaryView.aspx?ViewID=300'#, #main solar winds
        #'http://orion.dhs.lacounty.gov/Orion/SummaryView.aspx?ViewID=301', #la general solar winds
        #'http://orion.dhs.lacounty.gov/Orion/SummaryView.aspx?ViewID=302', #ACN solar winds
        #'http://orion.dhs.lacounty.gov/Orion/SummaryView.aspx?ViewID=303', #Harbor & OVMC solar winds
        #'http://orion.dhs.lacounty.gov/Orion/SummaryView.aspx?ViewID=304' #HSA & RLA
    ]

    for link in solarwind_links:
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)

        driver = webdriver.Edge(options=options)

        driver.get(link)

        element = driver.find_element(By.ID, 'ctl00_BodyContent_Username')
        element.send_keys('LACUSCENT')
        element = driver.find_element(By.ID, 'ctl00_BodyContent_Password')
        element.send_keys('USCOrion1$')
        win32api.Sleep(500)
        element.submit()


def openSolar1(): #main solar winds
    link = 'http://orion.dhs.lacounty.gov/Orion/SummaryView.aspx?ViewID=300'
    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Edge(options=options)
    driver.get(link)

    element = driver.find_element(By.ID, 'ctl00_BodyContent_Username')
    win32api.Sleep(1000)
    element.send_keys('LACUSCENT')
    win32api.Sleep(1000)
    element = driver.find_element(By.ID, 'ctl00_BodyContent_Password')
    element.send_keys('USCOrion1$')
    win32api.Sleep(1000)
    element.submit()
    win32api.Sleep(5000)

    keyboard.send_keys("{VK_LWIN down}{UP}")
    for i in range(21):
        win32api.Sleep(700)
        keyboard.send_keys("{RIGHT}")
    keyboard.send_keys("{UP}")
    keyboard.send_keys("{UP}")
    keyboard.send_keys("{VK_LWIN up}")

    driver.fullscreen_window()
    win32api.Sleep(1000)
    keyboard.send_keys("{VK_CONTROL down}")
    for i in range(4):
        keyboard.send_keys("{VK_SUBTRACT}")
    keyboard.send_keys("{VK_CONTROL up}")

    # Switch to the second tab (index 1)
    #driver.switch_to.window(driver.window_handles[1]) TRY THIS NEXT WEEK TO CHANGE FOCUS FROM MAIN SOLARWINDS AS IT KEEPS GOING DOWN


def openSolar2(): #la general solar winds
    link = 'http://orion.dhs.lacounty.gov/Orion/SummaryView.aspx?ViewID=301'
    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Edge(options=options)
    driver.get(link)

    element = driver.find_element(By.ID, 'ctl00_BodyContent_Username')
    win32api.Sleep(1000)
    element.send_keys('LACUSCENT')
    win32api.Sleep(1000)
    element = driver.find_element(By.ID, 'ctl00_BodyContent_Password')
    element.send_keys('USCOrion1$')
    win32api.Sleep(1000)
    element.submit()
    win32api.Sleep(5000)

    keyboard.send_keys("{VK_LWIN down}{UP}")
    for i in range(21):
        win32api.Sleep(700)
        keyboard.send_keys("{LEFT}")
    keyboard.send_keys("{UP}")
    keyboard.send_keys("{UP}")
    keyboard.send_keys("{VK_LWIN up}")

    driver.fullscreen_window()
    win32api.Sleep(1000)
    keyboard.send_keys("{VK_CONTROL down}")
    for i in range(4):
        keyboard.send_keys("{VK_SUBTRACT}")
    keyboard.send_keys("{VK_CONTROL up}")

def openSolar3(): #ACN solar winds
    link = 'http://orion.dhs.lacounty.gov/Orion/SummaryView.aspx?ViewID=302'
    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Edge(options=options)

    driver.get(link)

    element = driver.find_element(By.ID, 'ctl00_BodyContent_Username')
    win32api.Sleep(1000)
    element.send_keys('LACUSCENT')
    win32api.Sleep(1000)
    element = driver.find_element(By.ID, 'ctl00_BodyContent_Password')
    element.send_keys('USCOrion1$')
    win32api.Sleep(1000)
    element.submit()
    win32api.Sleep(2500)

    keyboard.send_keys("{VK_LWIN down}{UP}")
    for i in range(15):
        win32api.Sleep(700)
        keyboard.send_keys("{LEFT}")
    keyboard.send_keys("{UP}")
    keyboard.send_keys("{UP}")
    keyboard.send_keys("{VK_LWIN up}")

    driver.fullscreen_window()
    win32api.Sleep(1000)
    keyboard.send_keys("{VK_CONTROL down}")
    for i in range(4):
        keyboard.send_keys("{VK_SUBTRACT}")
    keyboard.send_keys("{VK_CONTROL up}")

def openSolar4(): #HSA & RLA
    link = 'http://orion.dhs.lacounty.gov/Orion/SummaryView.aspx?ViewID=304'
    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Edge(options=options)

    driver.get(link)

    element = driver.find_element(By.ID, 'ctl00_BodyContent_Username')
    win32api.Sleep(1000)
    element.send_keys('LACUSCENT')
    win32api.Sleep(1000)
    element = driver.find_element(By.ID, 'ctl00_BodyContent_Password')
    element.send_keys('USCOrion1$')
    win32api.Sleep(1000)
    element.submit()
    win32api.Sleep(2500)

    keyboard.send_keys("{VK_LWIN down}{UP}")
    for i in range(24):
        win32api.Sleep(700)
        keyboard.send_keys("{RIGHT}")
    keyboard.send_keys("{UP}")
    keyboard.send_keys("{UP}")
    keyboard.send_keys("{VK_LWIN up}")

    driver.fullscreen_window()
    win32api.Sleep(1000)
    keyboard.send_keys("{VK_CONTROL down}")
    for i in range(4):
        keyboard.send_keys("{VK_SUBTRACT}")
    keyboard.send_keys("{VK_CONTROL up}")

def openSolar5(): #Harbor & OVMC solar winds
    link = 'http://orion.dhs.lacounty.gov/Orion/SummaryView.aspx?ViewID=303'
    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Edge(options=options)

    driver.get(link)

    element = driver.find_element(By.ID, 'ctl00_BodyContent_Username')
    win32api.Sleep(1000)
    element.send_keys('LACUSCENT')
    win32api.Sleep(1000)
    element = driver.find_element(By.ID, 'ctl00_BodyContent_Password')
    element.send_keys('USCOrion1$')
    win32api.Sleep(1000)
    element.submit()
    win32api.Sleep(2500)

    keyboard.send_keys("{VK_LWIN down}{UP}")
    for i in range(18):
        win32api.Sleep(700)
        keyboard.send_keys("{LEFT}")
    keyboard.send_keys("{UP}")
    keyboard.send_keys("{UP}")
    keyboard.send_keys("{VK_LWIN up}")

    driver.fullscreen_window()
    win32api.Sleep(1000)
    keyboard.send_keys("{VK_CONTROL down}")
    for i in range(4):
        keyboard.send_keys("{VK_SUBTRACT}")
    keyboard.send_keys("{VK_CONTROL up}")

def openTelex():
    telex_link = 'http://10.108.210.110/pages/index.html' #Telex camera
    telex_options = webdriver.EdgeOptions()
    telex_options.add_experimental_option("detach", True)

    #telex_options.add_argument("start-maximized")
    #telex_options.add_argument("--start-fullscreen")

    driver = webdriver.Edge(options=telex_options)
    driver.get(telex_link)

    shell = win32com.client.Dispatch("WScript.Shell")
    win32api.Sleep(2500)
    shell.SendKeys("lacuschelp")
    shell.SendKeys("{TAB}")
    shell.SendKeys("helpdesk")
    shell.SendKeys("{ENTER}")

    win32api.Sleep(2500)
    keyboard.send_keys("{VK_LWIN down}{UP}")
    keyboard.send_keys("{VK_LWIN up}")

    driver.fullscreen_window()

def openLink1():
    openLink_link = 'https://w0bf-prod.asp.cernerworks.com/opl-web-24020003/login'

    openLink_options = webdriver.EdgeOptions()
    openLink_options.add_experimental_option("detach", True)

    driver = webdriver.Edge(options=openLink_options)

    driver.get(openLink_link)
    win32api.Sleep(2500)

    keyboard.send_keys("{VK_LWIN down}{UP}")
    for i in range(9):
        win32api.Sleep(700)
        keyboard.send_keys("{LEFT}")
    win32api.Sleep(700)
    keyboard.send_keys("{UP}")
    win32api.Sleep(700)
    keyboard.send_keys("{UP}")
    keyboard.send_keys("{VK_LWIN up}")

    #driver.fullscreen_window()
    win32api.Sleep(3000)
    keyboard.send_keys("e680868")
    keyboard.send_keys("{TAB}")
    keyboard.send_keys(ben())
    keyboard.send_keys("{ENTER}")
    win32api.Sleep(5000)
    driver.fullscreen_window()

def openLink2():
    openLink_link = 'https://w0bf-prod.asp.cernerworks.com/opl-web-24020003/login'

    openLink_options = webdriver.EdgeOptions()
    openLink_options.add_experimental_option("detach", True)

    driver = webdriver.Edge(options=openLink_options)

    driver.get(openLink_link)
    win32api.Sleep(2500)

    keyboard.send_keys("{VK_LWIN down}{UP}")
    for i in range(12):
        win32api.Sleep(700)
        keyboard.send_keys("{LEFT}")
    win32api.Sleep(700)
    keyboard.send_keys("{UP}")
    win32api.Sleep(700)
    keyboard.send_keys("{UP}")
    keyboard.send_keys("{VK_LWIN up}")

    #driver.fullscreen_window()
    win32api.Sleep(3000)
    keyboard.send_keys("e680868")
    keyboard.send_keys("{TAB}")
    keyboard.send_keys(ben())
    keyboard.send_keys("{ENTER}")
    win32api.Sleep(5000)
    driver.fullscreen_window()
    win32api.Sleep(1000)

    #text_to_find = "LAC_CA-DHS-P"
    #element = driver.find_element(By.XPATH, f"//*[text()='{text_to_find}']")
    #print(element)
    #element = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(element))
    #win32api.Sleep(3000)
    #pyautogui.moveTo(400,850)
    #pyautogui.click()

def openSplunk1():
    link = "http://10.106.204.22:8000/en-US/account/login?return_to=%2Fen-US%2Fapp%2Fitsi%2Fglass_table%3FsavedGlassTableId%3D25a74532-51b1-11ee-868f-005056bc7d3f%26action%3Dview%26form.global_time.earliest%3D-15m%26form.global_time.latest%3Dnow%26form.global_refresh_rate%3D300s"
    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Edge(options=options)

    driver.get(link)

    shell = win32com.client.Dispatch("WScript.Shell")
    win32api.Sleep(2500)
    shell.SendKeys("ehd")
    shell.SendKeys("{TAB}")
    win32api.Sleep(1000)
    shell.SendKeys("ehd123")
    shell.SendKeys("{ENTER}")
    win32api.Sleep(2500)

    keyboard.send_keys("{VK_LWIN down}{UP}")
    for i in range(15):
        win32api.Sleep(700)
        keyboard.send_keys("{RIGHT}")
    keyboard.send_keys("{UP}")
    keyboard.send_keys("{UP}")
    keyboard.send_keys("{VK_LWIN up}")

    driver.fullscreen_window()

def openSplunk2():
    link = "http://10.106.204.22:8000/en-US/account/login?return_to=%2Fen-US%2Fapp%2Fitsi%2Fglass_table%3FsavedGlassTableId%3D384c3ca6-51b1-11ee-94cd-005056bc7d3f%26action%3Dview%26form.global_time.earliest%3D-15m%26form.global_time.latest%3Dnow%26form.global_refresh_rate%3D300s"
    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Edge(options=options)

    driver.get(link)

    shell = win32com.client.Dispatch("WScript.Shell")
    win32api.Sleep(2500)
    shell.SendKeys("ehd")
    shell.SendKeys("{TAB}")
    shell.SendKeys("ehd123")
    shell.SendKeys("{ENTER}")
    win32api.Sleep(2500)

    keyboard.send_keys("{VK_LWIN down}{UP}")
    for i in range(12):
        win32api.Sleep(500)
        keyboard.send_keys("{RIGHT}")
    keyboard.send_keys("{UP}")
    keyboard.send_keys("{UP}")
    keyboard.send_keys("{VK_LWIN up}")

    driver.fullscreen_window()

def openSplunk():
    splunk_link_list = [
        "http://10.106.204.22:8000/en-US/account/login?return_to=%2Fen-US%2Fapp%2Fitsi%2Fglass_table%3FsavedGlassTableId%3D25a74532-51b1-11ee-868f-005056bc7d3f%26action%3Dview%26form.global_time.earliest%3D-15m%26form.global_time.latest%3Dnow%26form.global_refresh_rate%3D300s",
        "http://10.106.204.22:8000/en-US/account/login?return_to=%2Fen-US%2Fapp%2Fitsi%2Fglass_table%3FsavedGlassTableId%3D384c3ca6-51b1-11ee-94cd-005056bc7d3f%26action%3Dview%26form.global_time.earliest%3D-15m%26form.global_time.latest%3Dnow%26form.global_refresh_rate%3D300s"
    ]

    for link in splunk_link_list:
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)

        driver = webdriver.Edge(options=options)

        driver.get(link)

        shell = win32com.client.Dispatch("WScript.Shell")
        win32api.Sleep(2500)
        shell.SendKeys("ehd")
        shell.SendKeys("{TAB}")
        shell.SendKeys("ehd123")
        shell.SendKeys("{ENTER}")
        win32api.Sleep(2500)

def openControl():
    control_link = "file://hosted/ha/VDI-ServerBackup/ControlUP-HTML/Dashboard.html"

    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Edge(options=options)

    driver.get(control_link)
    win32api.Sleep(2500)

    keyboard.send_keys("{VK_LWIN down}{UP}")
    for i in range(2):
        win32api.Sleep(500)
        keyboard.send_keys("{LEFT}")

    win32api.Sleep(3000)
    keyboard.send_keys("{ENTER}")
    win32api.Sleep(1000)
    keyboard.send_keys("{VK_LWIN up}")

    keyboard.send_keys("{VK_CONTROL down}")
    for i in range(5):
        keyboard.send_keys("{VK_SUBTRACT}")
    keyboard.send_keys("{VK_CONTROL up}")

def iDashboards():
    dashboard_link = "http://10.106.242.90:6700/idashboards/viewer/?guestuser=guest&dashID=485"

    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Edge(options=options)

    driver.get(dashboard_link)
    win32api.Sleep(5000)

    keyboard.send_keys("{VK_LWIN down}{UP}")
    for i in range(4):
        win32api.Sleep(700)
        keyboard.send_keys("{LEFT}")

    keyboard.send_keys("{VK_LWIN up}")

def openMLKServerRoom1():
    server_link = "http://10.106.196.194/"

    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Edge(options=options)

    driver.get(server_link)

    shell = win32com.client.Dispatch("WScript.Shell")
    win32api.Sleep(2500)
    shell.SendKeys("LACUSC")
    shell.SendKeys("{TAB}")
    shell.SendKeys("lacusc2020")
    shell.SendKeys("{ENTER}")

    keyboard.send_keys("{VK_LWIN down}{UP}")
    for i in range(8):
        win32api.Sleep(700)
        keyboard.send_keys("{RIGHT}")

    keyboard.send_keys("{VK_LWIN up}")

def openMLKServerRoom2():
    server_link = "http://10.106.196.194/"

    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Edge(options=options)

    driver.get(server_link)

    shell = win32com.client.Dispatch("WScript.Shell")
    win32api.Sleep(2500)
    shell.SendKeys("LACUSC")
    shell.SendKeys("{TAB}")
    shell.SendKeys("lacusc2020")
    shell.SendKeys("{ENTER}")

    keyboard.send_keys("{VK_LWIN down}{UP}")
    for i in range(10):
        win32api.Sleep(700)
        keyboard.send_keys("{RIGHT}")

    win32api.Sleep(5000)
    keyboard.send_keys("{ENTER}")
    win32api.Sleep(1000)
    keyboard.send_keys("{VK_LWIN up}")

def openDashboardViewerServer():
    filePath = r"C:\Program Files\Cherwell Software\Cherwell Service Management\DashboardViewer.exe"
    os.startfile(filePath)
    shell = win32com.client.Dispatch("WScript.Shell")
    win32api.Sleep(10000)
    shell.SendKeys("Aa123456")
    shell.SendKeys("{ENTER}")
    win32api.Sleep(100000)

    keyboard.send_keys("{VK_LWIN down}{UP}")
    win32api.Sleep(1000)
    keyboard.send_keys("{RIGHT}")
    win32api.Sleep(1000)
    keyboard.send_keys("{RIGHT}")
    win32api.Sleep(1000)
    keyboard.send_keys("{RIGHT}")
    win32api.Sleep(1000)
    keyboard.send_keys("{RIGHT}")
    win32api.Sleep(1000)
    keyboard.send_keys("{RIGHT}")
    win32api.Sleep(1000)
    keyboard.send_keys("{RIGHT}")
    win32api.Sleep(1000)
    keyboard.send_keys("{RIGHT}")
    win32api.Sleep(1000)
    keyboard.send_keys("{RIGHT}")
    win32api.Sleep(1000)
    keyboard.send_keys("{UP}")
    win32api.Sleep(1000)
    keyboard.send_keys("{UP}{VK_LWIN up}")


def openMetaSysLauncher():
    #filePath = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Johnson Controls\Launcher.lnk"
    #os.startfile(filePath)
    #win32api.Sleep(10000)

    server_link = "jcilaunchersmp://10.102.174.149"
    options = webdriver.EdgeOptions()
    #options.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=options)
    driver.get(server_link)
    win32api.Sleep(5000)

    shell = win32com.client.Dispatch("WScript.Shell")

    shell.SendKeys("{TAB}")
    win32api.Sleep(500)
    shell.SendKeys("{ENTER}")
    win32api.Sleep(5000)
    '''
    shell.SendKeys("{TAB}")
    win32api.Sleep(1000)
    shell.SendKeys("{TAB}")
    win32api.Sleep(1000)
    shell.SendKeys("{TAB}")
    win32api.Sleep(1000)
    shell.SendKeys("{TAB}")
    win32api.Sleep(1000)
    shell.SendKeys("{TAB}")
    win32api.Sleep(1000)
    shell.SendKeys("{TAB}")
    win32api.Sleep(1000)
    shell.SendKeys("{TAB}")
    win32api.Sleep(1000)
    shell.SendKeys("{TAB}")
    win32api.Sleep(1000)
    shell.SendKeys("{ENTER}")
    win32api.Sleep(5000)
    win32api.Sleep(3000)
    '''
    shell.SendKeys("it")
    win32api.Sleep(2000)
    shell.SendKeys("{TAB}")
    win32api.Sleep(2000)
    shell.SendKeys("Ehd!2345")
    shell.SendKeys("{ENTER}")
    win32api.Sleep(4000)

    keyboard.send_keys("{VK_LWIN down}{UP}")
    for i in range(18):
        win32api.Sleep(700)
        keyboard.send_keys("{RIGHT}")
    keyboard.send_keys("{UP}")
    keyboard.send_keys("{UP}")
    keyboard.send_keys("{VK_LWIN up}")

#----------


def openDashboardViewerBen():
    filePath = r"C:\Program Files\Cherwell Software\Cherwell Service Management\DashboardViewer.exe"
    os.startfile(filePath)
    shell = win32com.client.Dispatch("WScript.Shell")
    win32api.Sleep(2500)
    shell.SendKeys(ben())
    shell.SendKeys("{ENTER}")

def openFullCherwell():
    os.startfile(r"C:\Program Files\Cherwell Software\Cherwell Service Management\Trebuchet.App.exe")
    shell = win32com.client.Dispatch("WScript.Shell")
    win32api.Sleep(2500)
    shell.SendKeys(ben())
    shell.SendKeys("{ENTER}")

def openFLIR(): #tab 23 times before entering username
    link = "http://10.109.157.7/WebClient/#/preview"

    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Edge(options=options)
    driver.get(link)
    win32api.Sleep(5000)
    for i in range(23):
        win32api.Sleep(200)
        keyboard.send_keys("{TAB}")
    keyboard.send_keys('ehduser')
    win32api.Sleep(1000)
    keyboard.send_keys("{TAB}")
    win32api.Sleep(1000)
    keyboard.send_keys('HelpDesk8000')
    win32api.Sleep(500)
    keyboard.send_keys("{ENTER}")
    win32api.Sleep(500)

    keyboard.send_keys("{VK_LWIN down}{UP}")
    for i in range(2):
        win32api.Sleep(700)
        keyboard.send_keys("{RIGHT}")
    win32api.Sleep(500)
    keyboard.send_keys("{UP}")
    win32api.Sleep(500)
    keyboard.send_keys("{UP}")
    keyboard.send_keys("{VK_LWIN up}")

    driver.fullscreen_window()

def openITvideo():
    filePath = r"C:\Users\svc_dhs.uscehdmon\Desktop\VIDEOFINAL IT_EHD_Collage_Motion_03.mp4"
    os.startfile(filePath)
    #win32api.Sleep(15000)
    '''
    keyboard.send_keys("{VK_LWIN down}{UP}")
    for i in range(5):
        win32api.Sleep(700)
        keyboard.send_keys("{LEFT}")

    keyboard.send_keys("{VK_LWIN up}")
    '''

def openITKnowledgeBase():
    link = "https://lacounty.sharepoint.com/sites/dhs-lageneral-is-itk/SitePages/TrainingHome.aspx"
    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=options)
    driver.get(link)

    keyboard.send_keys("{VK_LWIN down}{RIGHT}{VK_LWIN up}")


def RUN_ALL():
    openSolars()
    #openTelex()
    #openLink()
    #openLink()
    #openSplunk()
    #openControl()
    #iDashboards()
    #openMLKServerRoom()
    #openDashboardViewerServer()
    #openMetaSysLauncher()

def RUN_IN_ORDER():
    openTelex()
    openDashboardViewerServer()
    openSplunk1()
    openSplunk2()
    openSolar1()
    openSolar2()
    openSolar3()
    openSolar4()
    openSolar5()
    openLink1()
    openLink2()
    openControl()
    iDashboards()
    openMLKServerRoom()
    openMLKServerRoom()
    openMetaSysLauncher()
    openITvideo()
    openFLIR()


if __name__ == '__main__':
    #RUN_IN_ORDER()

    #openTelex() #GOOD
    #openDashboardViewerServer() #takes too long to open
    openSolar1() #GOOD
    #openSolar2() #GOOD
    #openSolar3() #GOOD
    #openSolar4() #GOOD
    #openSolar5() #GOOD
    #openLink1() #GOOD
    #openLink2() #GOOD
    #openSplunk1() #GOOD
    #openSplunk2() #GOOD, but slow for some reason
    #openMetaSysLauncher() #GOOD, just need to click CRAC, then zoom in button
    #iDashboards() #GOOD
    #openControl() #GOOD
    #openMLKServerRoom1() #GOOD
    #openMLKServerRoom2() #GOOD
    #openITvideo() #GOOD
    #openFLIR() #GOOD









