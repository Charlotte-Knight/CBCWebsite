from website import *
from body import *
import os

website = Website("style_template.html")
homepage = website.addNewPage("CBC Analysis")
website.setHomepage(homepage)

subdirs = ["yieldPlots", "errorBitPlots", "I2CPlots/I2C", "I2CPlots/VDDA"]
basedir = ""
dirs = [basedir + subdir for subdir in subdirs]

for subdir in subdirs:
  page = website.addNewPage(subdir.replace("/", " "))
  body = BodyFromDir(os.path.join(basedir,subdir))
  page.setBody(body)

def hasImagesIn(directory):
  for path in os.listdir(directory):
    if (".png" in path) or (".jpg" in path) or (".jpeg" in path):
      return True
  return False

basedir = "wt_analysis_for_firstbackup/data"
subdirs = [name for name in os.listdir(basedir) if os.path.isdir(os.path.join(basedir,name)) and hasImagesIn(os.path.join(basedir,name))]
print(subdirs)
for subdir in subdirs:
  page = website.addNewPage(subdir.replace("/", " "))
  body = BodyFromGitlabDir(os.path.join(basedir,subdir))
  page.setBody(body)

website.writeHTML()