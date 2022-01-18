from website import *
import os

lots = ["lot%d"%i for i in range(1,9)]

wafers = {'lot1': ['A3QIWQH', 'ALQJ04H', 'AWQIWXH'],
          'lot2': ['V1CYTAH', 'V1CYWRH', 'VVCZ0UH'],
          'lot3': ['V9CYE9H', 'VRCYF9H', 'VTCYEQH', 'VUCYCQH', 'VWCYGLH', 'VXCYD4H'],
          'lot4': ['V2D7Q1H', 'V2D7THH', 'V3D7RHH', 'V3D7TGH', 'VPD7TVH', 'VYD7TLH'],
          'lot5': ['V0D6AUH', 'V7D638H', 'VFD68FH', 'VUD662H', 'VWD6AYH'],
          'lot6': ['V0D7KNH', 'V1D7KMH', 'VLD6LKH', 'VZD7H8H', 'VZD7KPH'],
          'lot7': ['V0D7N4H', 'V1D7S1H', 'VCD7SQH', 'VZD7N5H', 'VZD7W1H'],
          'lot8': ['V2D879H', 'V3D878H', 'V4D877H', 'V6D875H', 'V7D874H', 'V8D873H', 'V9D891H']}

class BodyFromDir(Body):
  def __init__(self, directory):
    Body.__init__(self, objects=[])
    self.__directory = directory
    self.createObjects()

  def createObjects(self):
    for lot in lots:
      self += '<a class=anchor id="%s"></a>'%lot
      self += '<h2>%s</h2>'%(lot)
      
      for wafer in wafers[lot]:
        self += '<a href="#%s">%s</a><br>\n'%(wafer, wafer)

      images_paths = os.listdir(os.path.join(self.__directory, lot))
      for wafer in wafers[lot]:
        for path in images_paths:
          if wafer in path:
            self += '<a class=anchor id="%s"> </a>\n'%wafer
            self += '<h3>%s: %s</h3>'%(lot, wafer)

            self += Image(os.path.join(self.__directory, lot, path), "".join(path.split(".")[:-1]))

class BodyFromGitlabDir(Body):
  def __init__(self, directory):
    Body.__init__(self, objects=[])
    self.__directory = directory
    self.createObjects()

  def createObjects(self):
    images_paths = filter(lambda x: (".png" in x) or (".jpg" in x) or (".jpeg" in x), os.listdir(self.__directory))

    for lot in lots:
      self += '<a class=anchor id="%s"></a>'%lot
      self += '<h2>%s</h2>'%(lot)
      
      for wafer in wafers[lot]:
        self += '<a href="#%s">%s</a><br>\n'%(wafer, wafer)

      for wafer in wafers[lot]:
        for path in images_paths:
          if wafer in path:
            self += '<a class=anchor id="%s"> </a>\n'%wafer
            self += '<h3>%s: %s</h3>'%(lot, wafer)

            self += Image(os.path.join(self.__directory, path), "".join(path.split(".")[:-1]))