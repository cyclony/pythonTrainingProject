from lxml import etree
import re
with open('example.xml','r', encoding='utf8') as f:
    data = f.read()
    xml = etree.fromstring(data)

class xml_Doc:
    def __init__(self, xml_str):

        def tag_upper(matched):
            return matched.group(0).lower()

        self.xml_str = xml_str
        re_tag = re.compile('</?([A-z]+)>')
        self.xml_str = re_tag.sub(tag_upper, xml_str)
        self.root = xmlbean(etree.fromstring(self.xml_str))
        print(self.xml_str)
        
        
    def get_root(self):
        return self.root

class xmlbean:
    def __init__(self, xml_element):
        self.xml_element = xml_element
        self.name = self.xml_element.tag
    
    def __setattr__(self, name, value):
        if name == 'xml_element' or name == 'name':
            self.__dict__[name] = value
            return
        result = self.__dict__['xml_element'].xpath(name)
        if len(result) == 1 and len(result[0].getchildren())==0:
            result[0].text = value
            return
        raise AttributeError('not able to set value to attr:', name)

    def __getattr__(self, name):
        result = self.xml_element.xpath(name)
        if len(result)>1:
            return (xmlbean(element) for element in result)
        if len(result) == 1:
            if len(result[0].getchildren()) ==0:
                return result[0].text
            else:
                return xmlbean(result[0])
        raise AttributeError('does not exist such attr: '+name)

doc = xml_Doc(data)
root = doc.get_root()
print('title', 'artist', 'country', sep='\t\t\t')
for cd in root.cd:
    cd.artist = 'cyc'
    print(cd.artist)

print(etree.tostring(doc.root.xml_element))