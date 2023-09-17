# import unittest
# import json
# from selenium import webdriver
# from EcommerceSite.sauceweb.Specific.sauce_login_page import LoginPage
# from EcommerceSite.sauceweb.Specific.sauce_logged_in_page import LoggedInPage
# from EcommerceSite.sauceweb.Specific.sauce_login_page_selectors import SauceWebLoginPageSelectors
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import os
# from datetime import datetime
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
#
#
#
# class LoginTest(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Firefox()
#         cls.driver.get("https://www.saucedemo.com/")
#         # cls.driver.get(drivers_config["URL"])
#         cls.driver.maximize_window()
#
#
#     def test_01_login(self):
#         try:
#             login = LoginPage(self.driver)
#             login.is_login_modal_displayed()
#             login.login_flow("standard_user", "secret_sauce")
#             logged_in = LoggedInPage(self.driver)
#             logged_in.is_header_logged_displayed()
#         except:
#             raise Exception ('was no able to complete login flow')

# The following script gets 2 folders as input and
# compares the images with each other. Possible
# differences are stored in a new folder starting
# with compresult_
# usage: python imgCompare.py -f folder1 -s folder2
import cv2
import argparse
import os
from datetime import datetime
from PIL import Image, ImageChops

parser = argparse.ArgumentParser()
parser.add_argument("--first",  "-f", help="path to the first folder for image comparison", required=True)
parser.add_argument("--second", "-s", help="path to the second folder for image comparison", required=True)
args = parser.parse_args()

dir1 = args.first
dir2 = args.second

outputdir = "compresult_" + datetime.now().strftime("%Y%m%d_%H%M%S")

for filename in os.listdir(dir1):
    file1 = os.path.join(dir1, filename)
    file2 = os.path.join(dir2, filename)

    if not os.path.exists(file2):
        print("File " + file2 + " does not exist in second folder. Skip image")
        continue

    im1 = Image.open(file1)
    im2 = Image.open(file2)

    # print("Compare " + filename + " (" + file1 + " AND " + file2 + ")")

    diff_img = ImageChops.difference(im1, im2).convert("RGB")
    if diff_img.getbbox():
        outpath = outputdir + "/" + filename + "-s.png"
        print(" [\033[91m\u2717\033[0m] Images (" + filename + ") are different, store difference in " + outpath)
        os.makedirs(outputdir , exist_ok=True)
        diff_img.save(outpath)
    else:
        print(" [\033[92m\N{check mark}\033[0m] Images (" + filename + ") are equal")
