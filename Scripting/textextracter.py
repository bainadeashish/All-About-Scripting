from tika import parser
import pdb
from nltk.tokenize import word_tokenize,sent_tokenize
keys=set(['Phone'])
File_Name=r'C:\Users\Ashish.Bainade@infovisionlabs.com\Desktop\vikas patil.doc'
text = parser.from_file(File_Name)
content = text['content']
#words=word_tokenize(content)
counter=0
sentences=sent_tokenize(content)
for each_sentence in sentences:
	counter+=1
	for key in keys:
		if key.lower() in each_sentence.strip('\n').lower():
			print key ,counter , each_sentence.strip('\n')

