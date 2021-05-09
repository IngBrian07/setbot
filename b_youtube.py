from selenium import webdriver
import time
from random import randrange

time_visit=10 #Visit Time of the navigator in seconds
l_nav=[]

nav1=webdriver.Chrome(executable_path='./chromedriver.exe')

l_nav.append(nav1)

for n in l_nav:
    n.get('https://www.youtube.com/watch?v=CgpPEHZXcUI') #Enter the navegador
while(True):
    n_rad=randrange(0,len(l_nav))
    l_nav[n_rad].refresh()
    print('Navegator number:', n_rad, 'Update')
    time.sleep(time_visit)

