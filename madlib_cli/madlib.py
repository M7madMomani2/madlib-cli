import re
# solution
print("""
    **************************************
    **    Welcome to the Madlib game!   **
    **    do you want to play?.    **
    **************************************
    """)


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


# Stretch Goals
# def parse_template(content,user_input=True):
#     counter=1
#     fixed_data=[]
#     data = re.findall(r"\{(.*?)\}",content)
    # print(f'For This Game You Will Be Asked {len(data)} Qustion\n')
    # if user_input ==True:
    #     for i in data:
    #         user_input=input(f'{counter}) Please Insert {i} \n')
    #         fixed_data.append(user_input)   
    #         counter+=1
    # else:
    #   return data 
    # merge(fixed_data,content)
    # return content,fixed_data    