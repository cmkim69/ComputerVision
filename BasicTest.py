import urllib.request
import re
from bs4 import BeautifulSoup as bs
import json

# download file from URL
# url="http://catalogue.pearsoned.ca/assets/hip/ca/hip_ca_pearsonhighered/preface/013608592X.pdf"
# print("downloading...")
# fname, header = urllib.request.urlretrieve(url, 'test.pdf')
# print("download complete")
# print(fname, header)

# regular expression : word extraction
# url="http://ktnet.com"
# source=urllib.request.urlopen(url)
# source_contents = str(source.read().decode("ms949"))
# print(source_contents)
#
# id_results = re.findall("(<meta.+((http:)|(https:)).+\>)", source_contents)
# print(id_results)

# xml parsing
# with open("xmltest.xml", "r", encoding="utf8") as books_file:
#     books_xml = books_file.read()
#
# soup = bs(books_xml, "lxml")
# for book_info in soup.find_all("book"):
#     print("author : ", book_info.find("author").get_text())
#     print("title : ", book_info.find("title").get_text())

with open("jsontest.json","r", encoding="utf8") as json_file:
    contents=json_file.read()
    json_data = json.loads(contents)
    print(type(json_data["books"]["book"]))
    print(json_data["books"]["book"][0]["author"])