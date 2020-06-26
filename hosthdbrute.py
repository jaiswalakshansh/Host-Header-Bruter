import requests
import argparse
import os

parser=argparse.ArgumentParser()
parser.add_argument('-u',help='Full Url',dest='url')
parser.add_argument('-he',help='Header File',dest='header_file')
argument=parser.parse_args()
url=argument.url
header_file=argument.header_file

headers = []

if header_file:
        with open(header_file, 'r', encoding="utf8") as file:
            for line in file:
                headers.append(line.strip('\n'))



if url:
 FinalResult=[]
 for header in headers:
 	page = requests.get(url,header)
 	FinalResult.append(page.text)
 	
print(*FinalResult,sep="\n\n")


testp='output/'
isFile = os.path.isfile(testp)
if not isFile:
    try:
         os.mkdir(testp)
    except OSError as exc: 
        if exc.errno != errno.EEXIST:
            raise         
    	
       
if url:
 count = 0   
 for item in FinalResult:
    count += 1
    filename = testp+'{}.txt'.format(count)
    with open(filename, 'w') as f:
        f.write('{}\n'.format(item))
