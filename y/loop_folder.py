__author__="yiwan.lu"
__date__ ="September 18, 2014 12:51 PM"

import os
import codecs
src = r"C:\WebAppSource\app"
res_list = "enRes.txt"

def find_res():
	outfile = codecs.open(res_list, 'w', encoding = 'utf-8')
	num = 0
	for root, dirs, files in os.walk(src):
		if num > 10:
			break
		for filename in files:
			exts = filename.split('.')
			if len(exts) > 1:
				if exts[-1] == "resx":
					if exts[-2] == "de" or exts[-2] == "es" or exts[-2] == "fr" or exts[-2] == "ja"\
					or exts[-2] == "ko" or exts[-2] == "nl" or exts[-2] == "pt-BR" or exts[-2] == "ru"\
					or exts[-2] == "es-MX" or exts[-2] == "Resources" or exts[-2] == "zh-CN":
						continue
					else:
						filepath = os.path.join(root, filename)
						outfile.write("%s\r\n" %filepath)
	outfile.close()
if __name__ == "__main__":
	find_res()