def Question1(correct_answer):
    print('#'*40)
    python_invector = int(input('Who invented Python language?\n\
    1 - Steve Jobs.\n\
    2 - Mark Zuckeberg.\n\
    3 - Guido van Rossum.\n\
    4 - Donald Trump.\n'))
    
    if python_invector == 3:
        print(f"Correct answer!\nGuido van Rossum invented Python programming language in 1980's")
        correct_answer += 1
        return correct_answer # Serve para atualizar
    else:
        print(f"Worng answer. :/\n\
        Guido van Rossum invented Python programming language in 1980's")
    
def Question2(correct_answer):
    print('#'*40)
    name_meaning = int(input("Why Python have this name?\n\
    1 - It's a honor to Mounty Python, a comedy program.\n\
    2 - I'ts a honor to Python snake.\n\
    3 - It's a honor to creator.\n\
    4 - Because yes.\n"))
    
    if name_meaning == 1:
        print(f"Correct answer!\nGuido Van Rossum loved Mounty Python comedy programm, honoring your favorite comedy group in your own programming language.\n\
        Curiosity: When the Python guide was published, he's launched with Python snake, and since then is used to represent language.")
        correct_answer += 1
        return correct_answer
    elif name_meaning == 2:
        print(f"As incredible as it may seems, Python not was batizaded in honor of Python snake!\n\
        Guido Van Rossum loved Mounty Python comedy programm, honoring your favorite comedy group in your own programming language.\n\
        But when the Python guide was published, he's launched with Python snake, and since then is used to represent language.")
    else:
        print(f"Wrong answer! :/\n\
        Guido Van Rossum loved Mounty Python comedy programm, honoring your favorite comedy group in your own programming language.")
    

def Question3(correct_answer):
    print('#'*40)
    python_quality = int(input("Which options below is a Python qualitie?\n\
    1 - Complex syntax.\n\
    2 - Very heavy to run in computers.\n\
    3 - Little librariy quantities.\n\
    4 - Simple syntax.\n"))
    
    if python_quality == 4:
        print(f'Correct answer! Python have simple syntax, what help the programmers to develop your systems and applications, specially beginners.')
        correct_answer += 1
        return correct_answer
    else:
        print(f'Wrong answer! :/\n\
        Python have simple syntax, what help the programmers to develop your systems and applications, specially beginners.')