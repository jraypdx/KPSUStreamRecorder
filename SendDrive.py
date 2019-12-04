from selenium import webdriver
import os
import time
import pyautogui

def sendDrive(fileName, showName, emailTo):
    emailTo = emailTo.split(",")
    emailSubject = showName + " " + time.strftime('%b-%d-%Y')
    emailBody = (showName
                 + "\n" + time.strftime('%b-%d-%Y')
                 + "\n\n11/29/10 UPDATE:"
                 + "\nUsing Google Drive now, hopefully it will be more reliable.  (Please still save and rehost somewhere else)"
                 + "\nQuestions/Issues: jray@pdx.edu")

    driver = webdriver.Chrome()
    driver.get("https://mail.google.com")
    time.sleep(5)
    pyautogui.typewrite("*OMITTED*")
    pyautogui.press('enter')
    time.sleep(6)
    pyautogui.typewrite("*OMITTED*")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(8)
    driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
    time.sleep(5)

    for emails in emailTo:
        pyautogui.typewrite(emails)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
    time.sleep(2)
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.typewrite(emailSubject)
    time.sleep(2)
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.typewrite(emailBody)
    time.sleep(2)
    driver.find_element_by_xpath("//div[@aria-label='Attach files']").click()
    time.sleep(5)
    pyautogui.typewrite(os.path.abspath("Streams/" + fileName))
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(60)
    pyautogui.hotkey('ctrl', 'enter')
    time.sleep(3)
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@title='Sharing']"))
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div[3]/div").click()
    time.sleep(3)
    print (showName + " has been sent without catching any errors")
    time.sleep(3)
    driver.close()
