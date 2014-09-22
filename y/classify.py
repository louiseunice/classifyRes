__author__="yiwan.lu"
__date__ ="September 18, 2014 12:51 PM"

import os
import shutil
import codecs

src = r"C:\WebAppSource\app"

class resClassify(object):
	def factory(category):
		if category == "common": 
			return replaceClassify()
		else:
			return copyClassify()
	factory = staticmethod(factory)

class replaceClassify(object):
 	"""docstring for replaceClassify"""
 	def classify(self, data, to_p1):
		for line in data:
			line = line.strip()
			filename = os.path.basename(line)	
			to = line.replace(src, to_p1)
			to_p = os.path.dirname(to)
			if not os.path.exists(to_p):
				os.makedirs(to_p)
			to = to_p + '\\' + filename
			shutil.copyfile(line, to)
		data.close()

class copyClassify(object):
 	"""docstring for copyClassify"""
 	def classify(self, data, to_p):
		for line in data:
			line = line.strip()
			filename = os.path.basename(line)	
			if not os.path.exists(to_p):
				os.makedirs(to_p)
			to = to_p + '\\' + filename
			shutil.copyfile(line, to)
		data.close()

if __name__ == "__main__":
	category_array = ["common", "global", "HomeTab", "LogInLogOut", "ManageUsers", "Search"]
	cur_p = os.getcwd()
	for category in category_array:
		config_p = r"configs\\"+ category + ".txt"
		data = codecs.open(config_p, 'r', encoding='utf-8')
		to = cur_p + '\\'+ 'target' + '\\' + category
		clf = resClassify.factory(category)
		clf.classify(data, to)