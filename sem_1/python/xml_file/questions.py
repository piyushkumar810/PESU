# Write Python code to print all employee names using ElementTree.

import xml.etree.ElementTree as ET

tree = ET.parse("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//xml_file//companydData.xml")
root = tree.getroot()

for emp in root:
    print(emp.find("name").text)


'''
🧠 Explanation:

getroot() → top node
find() → child tag
.text → data inside tag
'''