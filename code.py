# Settings

## Install packages

pip install selenium
pip install webdriver_manager
pip install pyautogui

## Import packages

import selenium
PATH = "/Users/julia/Nextcloud/Thèse/2020-2021/J2P/Captures/chromedriver"

from selenium import webdriver
import pyautogui

from time import strftime
from datetime import datetime
import time
import os

## Create directories 


PARIS = "/Users/julia/Nextcloud/Thèse/2020-2021/J2P/Captures/Préfecture de Paris"

DIR_ETU = os.path.join(PARIS, "Demande de premier titre de séjour « étudiant » réservée aux étudiants non munis d’un VLS-TS")
DIR_TRAV_TRU = os.path.join(PARIS, "Demande d'admission exceptionnelle au séjour au regard du travail (CRE Truffaut))")
DIR_TRAV_CHA = os.path.join(PARIS, "Demande d'admission exceptionnelle au séjour au regard du travail (CRE Charcot))")
DIR_VPF_TRU = os.path.join(PARIS, "Demande d’admission exceptionnelle au séjour au titre de la situation personnelle et familiale (CRE Truffaut))")
DIR_VPF_CHA = os.path.join(PARIS, "Demande d’admission exceptionnelle au séjour au titre de la situation personnelle et familiale (CRE Charcot))")
DIR_MEDI_CHA = os.path.join(PARIS, "Demande de titre de séjour pour raisons médicales (Charcot)")
DIR_MEDI_TRU = os.path.join(PARIS, "Demande de titre de séjour pour raisons médicales (Truffaut)")


# Préfecture de Paris

driver = webdriver.Chrome(PATH)
driver.get("https://pprdv.interieur.gouv.fr/Rendez-vous-demarches-prefecture-de-police")
# print(driver.title)

# Liste des liens
liens = ["Demande de premier titre de séjour « étudiant » réservée aux étudiants non munis d’un VLS-TS",
        "Demande de titre de séjour pour raisons médicales (Truffaut)",
        "Demande de titre de séjour pour raisons médicales (Charcot)",
        "Demande d’admission exceptionnelle au séjour au titre de la situation personnelle et familiale (CRE Truffaut)",
        "Demande d’admission exceptionnelle au séjour au titre de la situation personnelle et familiale (CRE Charcot)",
        "Demande d'admission exceptionnelle au séjour au regard du travail (Truffaut)",
        "Demande d'admission exceptionnelle au séjour au regard du travail (Charcot)"]

date = str(datetime.now())[0:10]
# Scroll fin de la page
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

    
# Préfecture de Bobigny
