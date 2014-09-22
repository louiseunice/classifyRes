__author__="yiwan.lu"
__date__ ="September 18, 2014 12:51 PM"

import os
import shutil
import codecs

src = r"C:\WebAppSource\app"

def classify(category):
	config_p = r"configs\\"+ category + ".txt"
	data=codecs.open(config_p, 'r', encoding='utf-8')
	cur_p = os.getcwd()
	if category == "common":
		for line in data:
			line = line.strip()
			filename = os.path.basename(line)	
			to_p1 = cur_p + '\\'+ 'target' + '\\' + category
			to = line.replace(src, to_p1)
			to_p = os.path.dirname(to)
			if not os.path.exists(to_p):
				os.makedirs(to_p)
			to = to_p + '\\' + filename
			shutil.copyfile(line, to)
	elif category == "global" or category == "HomeTab" or category == "LogInLogOut" or category == "ManageUsers" or category == "Search" :
		for line in data:
			line = line.strip()
			filename = os.path.basename(line)	
			to_p = cur_p + '\\'+ 'target' + '\\' + category
			if not os.path.exists(to_p):
				os.makedirs(to_p)
			to = to_p + '\\' + filename
			shutil.copyfile(line, to)
	data.close()

if __name__ == "__main__":
	category_array = ["common", "global", "HomeTab", "LogInLogOut", "ManageUsers", "Search"]
	for item in category_array:
		classify(item)
