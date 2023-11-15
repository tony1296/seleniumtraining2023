#get commands or Information commands are get(),title,current_url,page_source,text
#get() is used to call the url
#title is used to call the title of the page
#current_url is used to call the url of the page
#page_source is used to get the source code of the page
#text is used to call the inner text of the page

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://google.com")
title=driver.title
print(title)
curl =driver.current_url
print(curl)
ps=driver.page_source
print(ps)