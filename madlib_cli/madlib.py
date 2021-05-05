import re
# solution
def read_template(path):
    with open(path, 'r') as file:
        content = file.read()
        return content.strip()
             

def parse_template(content):
    cont=0
    fixed_data=[]
    data = re.findall(r"\{(.*?)\}",content)
    for i in data:
        content=content.replace(data[cont],"",1)
        cont+=1
    return content,data

def merge(content ,fixed_data):
    cont=0
    data = re.findall(r"\{\}",content)
    print(data)
    for i in fixed_data:
        content=content.replace(data[cont],i,1)
        cont+=1
     
    with open('assets/user_input.txt', 'w') as input_content:
        input_content.write(content)
    return content

