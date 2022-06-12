from bs4 import BeautifulSoup
soup=BeautifulSoup(open('./index.m3u8').read(),'xml')
# open('./a.xml','w').write(soup.prettify())
print(soup.Period)