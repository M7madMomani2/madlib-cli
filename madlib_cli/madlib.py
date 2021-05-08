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
    raise FileNotFoundError


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
    for i in fixed_data:
        content=content.replace(data[cont],i,1)
        cont+=1
     
    with open('assets/user_input.txt', 'w') as input_content:
        input_content.write(content)
    return content



def play(file_path):
    input_req=input(f'Do you want to play ? (Y/N)')
    print(input_req.upper())
    if input_req.upper()=="Y":
        actual = read_template(file_path)


        pure_text, missing_word = parse_template(actual)
        print(pure_text)

        user_input=[]
        print("=======================================")
        for i in missing_word:
            element=input(f"Please Enter {i} : ")
            user_input.append(element)
        print("=======================================")
        final_result=merge(pure_text, user_input)
        print(final_result)

# file_path="assets/make_me_a_video_game.txt"
file_path="assets/dark_and_stormy_night.txt"


# play(file_path)

