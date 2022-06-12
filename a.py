from bs4 import BeautifulSoup
soup=BeautifulSoup(open('./index.m3u8').read())
print(soup.prettify())