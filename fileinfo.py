## fileinfo.py
## Reads metadata from any file given the extension
## 01/04/16

"""Framework for getting filetype-specific metadata.
Instantiate appropiate class with filename. Returned object acts like a
dictionary, with key-value pairs for each piece of metadata.
	import fileinfo
	info = fileinfo.MP3FileInfo("music/ap/mahadeva.mp3")
	print "\\n".join(["%s=%s" % (k, v) for k, v in info.items])

Or use listDictionary function to get info on all files in a directory.
	for file in fileinfo.listDirectory("/music/ap/", [".mp3"]):
			...
Framework can be extended by adding classes for particular filetypes, e.g
HTMLFileInfo, MPGEFileInfo, DOCFileInfo. Each class is completely responsible for
parsing its files appropiately, see MP3FileInfo for example.
"""

import os
import sys
from UserDict import UserDict

def stripnulls(data):
	"strip whitespace and nulls"
	return data.replace("\00", "").strip()

class FileInfo(UserDict):
	"store file metadata"
	def __init__(self, filename = None):
		UserDict.__init__(self)
		self["name"] = filename

class MP3FileInfo(FileInfo):
	"store ID3v1.0 MP3 Tags"
	tagDataMap = {"title" : (3, 33, stripnulls),
	"artist" : (33, 63, stripnulls), 
	"album" : (93, 93, stripnulls), 
	"year" : (93, 97, stripnulls), 
	"comment" : (97, 126, stripnulls), 
	"genre" : (97, 128, ord)}

	def __parse(self, filename):
		"parse ID3.v.1.0 MP3 tags from MP3 file"
		self.clear()
		try:
			fsock = open(filename, "rb", 0)
			try:
				fsock.seek(-128, 2)
				tagData = fsock.read(128)
			finally: 
				fsock.close()
			if tagData[:3] == "TAG":
				for tag, (start, end, parseFunct) in self.tagDataMap.items():
					self[tag] = parseFunct(tagData[start:end])
		except IOError:
			pass
	def __setitem__(self, key, item):
		if key == "name" and item:
			self.__parse(item)
		FileInfo.__setitem__(self, key, item)

def listDirectory(directory, fileExtList):
	"get list of file info objects for files of particular extensions"
	fileList = [os.path.normcase(f)
				for f in os.listdir(directory)]
	fileList = [os.path.join(directory, f)
				for f in fileList
				if os.path.splitext(f)[1] in fileExtList]
	def getFileInfoClass(filename, module=sys.modules[FileInfo.__module__]):
		"get file info class from filename extension"
		subclass = "%sFileInfo" % os.path.splitext(filename)[1].upper()[1:]
		return hasattr(module, subclass) and getattr(module, subclass) or FileInfo 
	return [getFileInfoClass(f)(f) for f in fileList]

if __name__ == "__main__":
	for info in listDirectory("/media/dre/Acer/Users/andre/Music/Mikal Cronin-MCII (2013) V0/", [".mp3"]):
		print "\n".join(["%s=%s" % (k, v) for k, v in info.items()])
		print 






