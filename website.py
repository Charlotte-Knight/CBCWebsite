class Image:
  def __init__(self, image_path, title=None):
    self.image_path = image_path
    self.title = title

  def __str__(self):
    string = '<p>%s</p>\n'%self.title
    string += '<img style="max-width:100%%", src="%s">\n'%self.image_path
    return string

class Body:
  def __init__(self, objects=[]):
    self.__objects = objects

  def addObjects(self, objects):
    if type(objects) == list:
      self.__objects.extend(objects)
    else:
      self.__objects.append(objects)

  def __add__(self, other):
    self.addObjects(other)
    return self

  def __str__(self):
    return "\n".join([str(obj) for obj in self.__objects])

  def generateHTML(self):
    return str(self)

class Navbar:
  def __init__(self, pages=[]):
    self.__pages = pages

  def addPages(self, pages):
    if type(pages) == list:
      self.__pages.extend(pages)
    else:
      self.__pages.append(pages)

  def generateHTML(self):
    html_str = ""
    html_str += '<div class="navbar">\n'
    for page in self.__pages:
      html_str += '<a href="%s">%s</a>\n'%(page.getHTMLPath(), page.getTitle())
    html_str += '</div>\n'
    return html_str

class Page:
  def __init__(self, title, style_template, navbar, body=None, html_path=None):
    self.__title = title
    self.__style_template = style_template
    self.__navbar = navbar
    self.initBody(body)
    self.initHTMLPath(html_path)    
  
  def initBody(self, body):
    if body != None:
      self.__body = body
    else:
      self.__body = Body()

  def setHTMLPath(self, html_path):
    self.__html_path = html_path

  def initHTMLPath(self, html_path):
    if html_path != None:
      self.setHTMLPath(html_path)
    else:
      self.setHTMLPath(self.getTitle().replace(" ", "_") + ".html")

  def getHTMLPath(self):
    return self.__html_path

  def getTitle(self):
    return self.__title

  def generateSideNavHTML(self):
    html_str = ""
    
    html_str += '<div class="sidenav">\n'
    lots = ["lot%d"%i for i in range(1,9)]
    for lot in lots:
      html_str += '<a href="#%s">%s</a> <br>\n'%(lot, lot)
    html_str += "</div>\n"
    return html_str

  def setBody(self, body):
    if isinstance(body, Body):
      self.__body = body
    else:
      raise Excpetion("Body must be of type Body")

  def generateHTML(self):
    html_str = ""

    html_str += "<!DOCTYPE html>\n"
    html_str += "<html>\n"
    html_str += "<head>\n"
    html_str += "<title>%s</title>\n"%self.getTitle()
    html_str += self.__style_template
    html_str += "</head>\n"

    html_str += "<body>\n"

    html_str += self.generateSideNavHTML()
    html_str += self.__navbar.generateHTML()

    html_str += '<div class="main">\n'
    html_str += self.__body.generateHTML()
    html_str += '</div>\n'

    html_str += "</body>\n"
    html_str += "</html>\n"
    return html_str

  def writeHTML(self):
    with open(self.__html_path, "w") as f:
      f.write(self.generateHTML())

class Website:
  def __init__(self, style_template_path):
    self.__navbar = Navbar()
    self.__pages = []
    self.initStyleTemplate(style_template_path)
    self.__homepage = None

  def initStyleTemplate(self, style_template_path):
    with open(style_template_path, "r") as f:
      self.__style_template = f.read()

  def addNewPage(self, title):
    for page in self.getPages():
      if title == page.getTitle():
        raise Exception("Page called '%s' already exists"%title)
    
    new_page = Page(title, self.__style_template, self.__navbar)
    self.__pages.append(new_page)
    self.__navbar.addPages(new_page)
    return new_page

  def getPages(self):
    return self.__pages

  def getPage(self, title):
    for page in self.__getPages():
      if title == page.getTitle():
        return page

  def setHomepage(self, homepage):
    page_exists = False
    if isinstance(homepage, Page):      
      for page in self.getPages():
        if homepage == page:
          #page exists in website
          self.__homepage = page
          self.__homepage.setHTMLPath("index.html")
          return None
      
      raise Exception("Page does not exist in this website")
    
    elif type(homepage) == str:
      for page in self.getPages():
        if homepage.getTitle() == page.getTitle():
          self.__homepage = page
          self.__homepage.setHTMLPath("index.html")
          return None

      raise Exception("Page does not exist in this website")

    else:
      raise Exception("homepage argument must be of type Page or str")
    
  def getHomepage(self):
    return self.__homepage

  def writeHTML(self):
    for page in self.getPages():
     page.writeHTML()

class Test:
  def __init__(self):
    self.contents = "hello"

  def generateHTML(self):
    return self.contents
  
  def __str__(self):
    return self.generateHTML()

  def __add__(self, other):
    return str(other) + "\n" + str(self)

if __name__=="__main__":
  website = Website("style_template.html")
  homepage = website.addNewPage("CBC Analysis")
  website.setHomepage(homepage)
  website.writeHTML()

