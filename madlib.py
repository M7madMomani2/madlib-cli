import re
# solution
def read_template(path):
    with open(path, 'r') as file:
        content = file.read()
        return content.strip()
             
def parse_template(content,user_input=True):
    counter=1
    fixed_data=[]
    data = re.findall(r"\{(.*?)\}",content)
    # print(f'For This Game You Will Be Asked {len(data)} Qustion\n')
    # if user_input ==True:
    #     print('################################################################\n')
    #     for i in data:
    #         user_input=input(f'{counter}) Please Insert {i} \n')
    #         fixed_data.append(user_input)   
    #         counter+=1
    #     print('################################################################')
    # else:
    
    return data 
    # merge(fixed_data,content)
    # return fixed_data    

# merge("It was a { } and { } { }.", ("dark", "stormy", "night"))
def merge(content ,fixed_data):
    cont=0
    data = re.findall(r"\{(.*?)\}",content)

    for i in fixed_data:
        content=content.replace(data[cont],i,1)
        cont+=1
    content=content.replace('{','')
    content=content.replace('}','')

    with open('assets/user_input.txt', 'w') as input_content:
        # print(f"im in {content}")
        input_content.write(content)

    print('################################################################\n')
    return content

# print(read_template('assets/dark_and_stormy_night.txt'))
# parse_template(read_template('assets/dark_and_stormy_night.txt'))
# print(f" {read_template2('assets/user_input.txt')}")


print(merge("It was a {} and {} {}.", ["dark", "stormy", "night"]))