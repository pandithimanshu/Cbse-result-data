#this will also shows you print on screen
print('welcome') 

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pickle

result_file = open('result cbse 12th.txt','a')

stu_marks = {}
driver = webdriver.Chrome('C:/Users/user/PycharmProject/mydjango/misson pisa/chromedriver.exe')
driver.get("https://www.cbseresults.nic.in/class12/Class12th21.htm")
time.sleep(2)
if driver.current_url =='https://www.cbseresults.nic.in/class12/Class12th21.htm':
    driver.find_element_by_xpath('//*[@id="details-button"]').click()
    driver.find_element_by_xpath('//*[@id="proceed-link"]').click()
for i in range(25658116,25658196):
    driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td/font/center[2]/form/div[1]/center/table/tbody/tr[1]/td[2]/input').send_keys(i)
    driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td/font/center[2]/form/div[1]/center/table/tbody/tr[2]/td[2]/input').send_keys(84042)
    driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td/font/center[2]/form/div[1]/center/table/tbody/tr[3]/td/input[1]').click()
    page_source = driver.page_source
    soup = BeautifulSoup(page_source,'html.parser')
    print(soup) 

    #best way to get subject wise data 

      # subject wise data
    for j in range(1,9):
        sub = soup.find_all('table')[5].find_all('tbody')[0].find_all('tr')[j]
        if j ==1:
            sub_code_ = sub.find_all('td')[0].text
            if sub_code_ =='301':
                print('cs student found !!!!!!!')
                practicles_marks = open('practicles marks 12th.txt', 'a')
                practicles_marks.write(f"{t1.find_all('tr')[1].find_all('td')[0].text} = {t1.find_all('tr')[1].find_all('td')[1].text} ")
                practicles_marks.write(f"{sub.find_all('td')[3].text} \n")
                practicles_marks.close()

        for k in range(6):
            result_file.write(f"{sub.find_all('td')[k].text} | ")
            print(sub.find_all('td')[k].text,end=' | ')
            if k ==1:
                print((20-int(len(sub.find_all('td')[k].text))) * ' ',end='')
        result_file.write('\n')
        print(end = '\n')
    try:
        sub = soup.find_all('table')[5].find_all('tbody')[0].find_all('tr')[10]
        for k in range(6):
            print(sub.find_all('td')[k].text,end = ' | ')
            result_file.write(f"{sub.find_all('td')[k].text} | ")
        print(end = '\n')
        result_file.write('\n')
    except:
        print('student have only 5 subjects not 6')





    driver.find_element_by_xpath('/html/body/div/p[1]/b/a/font').click()
    # head_6 = soup.find_all('table')[i].find_all('tbody')[0].find_all('tr')[5].find_all('td')[0].text
    # data_6 = soup.find_all('table')[i].find_all('tbody')[0].find_all('tr')[5].find_all('td')[1].text
    # head_7 = soup.find_all('table')[i].find_all('tbody')[0].find_all('tr')[6].find_all('td')[0].text
    # data_7 = soup.find_all('table')[i].find_all('tbody')[0].find_all('tr')[6].find_all('td')[1].text
    # head_8 = soup.find_all('table')[i].find_all('tbody')[0].find_all('tr')[7].find_all('td')[0].text
    # data_8 = soup.find_all('table')[i].find_all('tbody')[0].find_all('tr')[7].find_all('td')[1].text



    # print(head_6,data_6)
    # print(head_7,data_7)
    # print(head_8,data_8)

     # eske source code me 4th td tag me hai students data
=======
#<<<<<<< patch-2
    print(student_info)
        result_file.write(f'{student_info}\n')
  #headings
    head = soup.find_all('table')[5].find_all('tbody')[0].find_all('tr')[0]
    for j in range(6):
        headings = f"{head.find_all('td')[j].text} |"
        result_file.write(f'{headings}')
        print(headings,end='')
    print(end='\n')


#this will shows all the data in console

    print('\n'*10,'now td (data of student) comes\n')
    cs_practicles = {}
  # student information
    t1 = soup.find_all('table')[4].find_all('tbody')[0]
    for y in range(5):
        student_info= f"{t1.find_all('tr')[y].find_all('td')[0].text} = {t1.find_all('tr')[y].find_all('td')[1].text}"
#main
#>>>>>>> main
print('\n'*10,'now td (data of student) comes\n')

    cs_practicles = {}

  # student information

    t1 = soup.find_all('table')[4].find_all('tbody')[0]

    for y in range(5):

        student_info= f"{t1.find_all('tr')[y].find_all('td')[0].text} = {t1.find_all('tr')[y].find_all('td')[1].text}"

#main

