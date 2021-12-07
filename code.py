# Settings

## Install packages

pip install selenium
pip install webdriver_manager
pip install pyautogui

## Import packages

import selenium
PATH = "my_path/chromedriver"

from selenium import webdriver
import pyautogui

from time import strftime
from datetime import datetime
import time
import os

# Préfecture de Paris

driver = webdriver.Chrome(PATH)

## Paris (hors AES travail)

driver.get("https://pprdv.interieur.gouv.fr/Rendez-vous-demarches-prefecture-de-police")
# print(driver.title)

### Liste des liens
liens = ["Demande de premier titre de séjour « étudiant » réservée aux étudiants non munis d’un VLS-TS",
        "Demande de titre de séjour pour raisons médicales (Truffaut)",
        "Demande de titre de séjour pour raisons médicales (Charcot)",
        "Demande d’admission exceptionnelle au séjour au titre de la situation personnelle et familiale (CRE Truffaut)",
        "Demande d’admission exceptionnelle au séjour au titre de la situation personnelle et familiale (CRE Charcot)",]

date = str(datetime.now())[0:10]
#### Scroll fin de la page
for L in liens:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # Clic premier lien 
    link = driver.find_element_by_link_text(L)
    link.click()
    # Scroll fin de la page
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # Cocher les conditions d'utilisation
    accept = driver.find_element_by_id("condition")
    accept.click()
    # Cliquer sur le bouton de prise de rendez-vous
    demande = driver.find_element_by_name("nextButton")
    demande.click()
    # Capture d'écran
    myScreenshot = pyautogui.screenshot()
    # Enregistrement
    path = f'/Users/julia/Nextcloud/Thèse/2020-2021/J2P/Captures/Préfecture de Paris/{L}'
    filename = f'{date}.png'
    filename = os.path.join(path, filename)
    myScreenshot.save(filename)
    time.sleep(2)
    driver.back()
    driver.back()

## Préfecture Paris : AES au regard du travail 
# (car lien bugue sur la page précédente, mal attribué dans le code html)

### Liste des liens
dicliens = {"https://pprdv.interieur.gouv.fr/booking/create/885":"Demande d'admission exceptionnelle au séjour au regard du travail (Charcot)",
           "https://pprdv.interieur.gouv.fr/booking/create/876":"Demande d'admission exceptionnelle au séjour au regard du travail (Truffaut)"}

for l in dicliens:
    L = dicliens[l]
    driver.get(l)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # Cocher les conditions d'utilisation
    accept = driver.find_element_by_id("condition")
    accept.click()
    # Cliquer sur le bouton de prise de rendez-vous
    demande = driver.find_element_by_name("nextButton")
    demande.click()
        #### Charcot : il y a 2 boutons supplémentaires
    if L == "Demande d'admission exceptionnelle au séjour au regard du travail (Charcot)": 
        select2 = {"planning886": "salarie", "planning1043": "salarie2"}
        for s in select2:
            k = select2[s]
            # Cliquer sur le 2ème sélecteur salarié / salarié 2
            selecteur = driver.find_element_by_id(s)
            selecteur.click()
            # Cliquer sur le bouton de prise de rendez-vous
            demande = driver.find_element_by_name("nextButton")
            demande.click()
            # Capture d'écran
            myScreenshot = pyautogui.screenshot()
            # Enregistrement
            path = f'/Users/julia/Nextcloud/Thèse/2020-2021/J2P/Captures/Préfecture de Paris/{L}'
            filename = f'{date}_{k}.png'
            filename = os.path.join(path, filename)
            myScreenshot.save(filename)
            time.sleep(2)
            driver.back()
                #### Truffaut : il n'y a pas les 2 boutons supplémentaires comme pour Charcot
    if L == "Demande d'admission exceptionnelle au séjour au regard du travail (Truffaut)":
        # Capture d'écran
        myScreenshot = pyautogui.screenshot()
        # Enregistrement
        path = f'/Users/julia/Nextcloud/Thèse/2020-2021/J2P/Captures/Préfecture de Paris/{L}'
        filename = f'{date}.png'
        filename = os.path.join(path, filename)
        myScreenshot.save(filename)
        time.sleep(2)
        driver.back()
        

    
# Bobigny
    
driver.get("https://www.seine-saint-denis.gouv.fr/Prendre-un-rendez-vous")
# print(driver.title)


# Liste des localisations du lien
lien = "Demande d'admission exceptionnelle au séjour"
nbliens = driver.find_elements_by_link_text(lien)
n = len(nbliens)


# self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)

date = str(datetime.now())[0:10]

i = 0
for k in range(n):
    listloc = []
    listloc = driver.find_elements_by_link_text(lien)
  #  print(listloc)
    L = listloc[k]
  #  print(L)
    lieu = "Raincy"
    if i == 0:
        lieu = "Bobigny"
        
        
    # this scrolls untill the element is in the middle of the page
    desired_y = (L.size['height'] / 2) + L.location['y']
    current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
    scroll_y_by = desired_y - current_y
    driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
    
    
    # Clic premier lien 
    link = driver.find_element_by_link_text(lien)
    link.click()
    # Capture d'écran
    myScreenshot = pyautogui.screenshot()
    # Enregistrement
    path = f'/Users/julia/Nextcloud/Thèse/2020-2021/J2P/Captures/Préfecture de Bobigny/{lieu}'
    filename = f'{date}.png'
    filename = os.path.join(path, filename)
    myScreenshot.save(filename)
    time.sleep(2)
    driver.back()
    # Scroll haut de la page
    driver.execute_script("window.scrollTo(0, 0);")
    i = i + 1
    
driver.quit()
