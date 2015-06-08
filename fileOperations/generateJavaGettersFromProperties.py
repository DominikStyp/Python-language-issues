'''
Give it a file like:

ChangeNames=asdfvc
GiveRegexFrom=fsdfsf

And it will generate Java getters like:

	public String getChangeNames() {
		return this.getKey("ChangeNames");
	}

	public String getGiveRegexFrom() {
		return this.getKey("GiveRegexFrom");
	}

'''

def generateJavaGetters(filePath):
	f = open(filePath,"r")
	for line in f.readlines():
		first = line.split("=")[0]
		stri = "public String get"+first+"(){\n\t\treturn this.getKey(\""+first+"\");\n}"
		print(stri)

# example
generateJavaGetters("C:\Users\Dominik\Desktop\JavaProperties.txt")