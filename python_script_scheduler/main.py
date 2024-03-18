print('hello world')
#step 1: generate a file to attach in the email
import requests
import PyPDF2
from requests import HTTPError
import subprocess

try:
    res=requests.get(url='https://official-joke-api.appspot.com/jokes/random')
except HTTPError as ex:
    print(ex)
# print(f'the respose is {res.status_code} with data {res.text}')
# print(res.json()['setup'])
# print('the Answer is  ? :'+res.json()['punchline'])

setup=res.json()['setup']
punchline=res.json()['punchline']

#Now dump the contents over the file 

# with open("YOUR_DAILY_FEED.pdf",'wb') as pdf:
#     pdf_writer=PyPDF2.PdfWriter()
#     pdf_writer.add_blank_page(width=595,height=842)
#     #pdf_writer.add_page_label(0,"page1")
#     #now write the contents 
#    # Get the page
#     page = pdf_writer.pages[0]

#     # Access the content stream of the page
#     page.add

#     print(type(page))

with open('YOUR_FEED.txt','w+') as file:
    file.write(setup+"\n"+punchline)

#Now send the file through mail
    
# Call the demo-email.py script
subprocess.run(["python", "D:\Python-Programming\projects\python_script_scheduler\demo-email.py"])


#######
print('End of process .............. ✉️📩')


