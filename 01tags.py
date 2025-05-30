import requests

from bs4 import BeautifulSoup

with open("sample.html", "r") as f:
    html_doc = f.read()


soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())
# print(soup.title, type(soup.title.string))
# print(soup.div)
# print(soup.find_all("div")) # list of all divs

# for link in soup.find_all("a"):
    # print(link)
    # print(link.get("href"))
    # print(link.get_text())

# s=soup.find(id="link3")
# print(s)
# print(s.get("href"))

# print(soup.select("div.italic"))
# print(soup.select("span#italic"))
# print(soup.span.get("class"))

# print(soup.find_all(class_="italic"))
# print(soup.find(id="italic"))

# for child in soup.find(class_="container").children:
#     print(child)

# for parent in soup.find(class_="box").parents:
#     print(parent)

cont = soup.find(class_="container")
# cont.name = "span"        # element with class = "container" converts into span
# cont["class"] = "myClass cllassss"
# cont.string = "I am a string"     # changes the text of the element
# print(cont)


# ulTag = soup.new_tag("ul")

# liTag = soup.new_tag("li")
# liTag.string = "Home"
# ulTag.append(liTag)

# liTag = soup.new_tag("li")
# liTag.string = "About"
# ulTag.append(liTag)

# soup.html.body.insert(0, ulTag)
# with open("modified.html", "w") as f:
#     f.write(str(soup))


# soup.find(class_="container")
# print(cont.has_attr("id")) # false
# print(cont.has_attr("class")) # true
# print(cont.has_attr("contenteditable")) # true


def has_class_but_not_id(tag):
    return not tag.has_attr("class") and not tag.has_attr("id")

def has_content(tag):
    return tag.has_attr("content")

results = soup.find_all(has_class_but_not_id);
# print(results)

for res in results:
    print(res, "\n\n")