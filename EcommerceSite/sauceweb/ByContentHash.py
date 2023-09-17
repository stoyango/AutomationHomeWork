# import urllib.request
# import hashlib
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# def hash_it(path):
#     with open(path, 'rb') as f:
#         hasher = hashlib.md5()
#         hasher.update(f.read())
#         return hasher.hexdigest()
#
# directory = 'EcommerceSite/sauceweb/Specific/screenshots'
# remote_img = "{}/{}".format(directory, "remote.png")
# local_img = "{}/{}".format(directory, "logged_in_items.png")
# firefox = webdriver.Firefox()
# firefox.get("https://www.saucedemo.com/")
# # firefox.find_element(By.ID, "user-name").send_keys(standard_user)
# # firefox.find_element(By.ID, "password").send_keys(secret_sauce)
# # firefox.find_element(By.ID, "login-button").click()
# logo = firefox.find_element(By.ID, "login-button").get_attribute("src")
# urllib.request.urlretrieve(logo, remote_img)
# local_img_hash = hash_it(local_img)
# remote_img_hash = hash_it(remote_img)
# assert local_img_hash == remote_img_hash, "not equal".format((local_img_hash, remote_img_hash))
