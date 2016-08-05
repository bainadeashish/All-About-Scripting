from tika import parser
import pdb
from nltk.tokenize import word_tokenize,sent_tokenize
keys=set(['Phone','email','skill'])
File_Name=r'C:\Users\Ashish.Bainade@infovisionlabs.com\Desktop\vikas patil.doc'
text = parser.from_file(File_Name)
content = text['content']
#words=word_tokenize(content)
#sentences=sent_tokenize(content)
sentences=set(content.splitlines())
for each_sentence in sentences:
	for key in keys:
		
		if key.lower() in each_sentence.strip('\n').lower():
			print key , each_sentence.strip('\n')

