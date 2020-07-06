# Alt+3 Studio
# by Ilya Katkov
# VKCB

# import modules
from tkinter import *
from tkinter import messagebox as mb
import pyperclip
import webbrowser
import os
import sys
import psutil

main_window, f1_window = 0, 0  # count for windows

true_alphabet = ['q', 'w', 'e', 'r', 't', 
                'y', 'u', 'i', 'o', 'p', 
                'a', 's', 'd', 'f', 'g',
                'h', 'j', 'k', 'l', 'z',
                'x', 'c', 'v', 'b', 'n', 
                'm', '-', '_', '+', '!',
                '\'', '@', '№', '$', ';',
                '(', ')', '^', '&', ' ',
                '[', ']', '{', '}', ',',
                '0', '1', '2', '3', '4',
                '5', '6', '7', '8', '9']

# check opened programs "vkcb.exe"
for proc in psutil.process_iter():
    name = proc.name()
    if name == "vkcb.exe":
        main_window += 1
        if main_window > 2:
            sys.exit()


# f1 window
def info_window_f1(event):
    global f1_window
    f1_window += 1
    if f1_window > 1:
        return print("---F1---")

    # exit
    def info_window_close():
        global f1_window
        f1_window = 0
        info_window.destroy()

    def info_window_enter(event):
        global f1_window
        f1_window = 0
        info_window.destroy()

    # ilkatkov vk.com CLICK
    def vk(event):
        webbrowser.open_new(r"http://vk.com/ilkatkov")

    # Alt+3 Studio vk.com CLICK
    def vk_alt3s(event):
        webbrowser.open_new(r"http://vk.com/alt3s")

    # readme.txt
    def readme():
        try:
            os.startfile(r'readme.txt')
        except FileNotFoundError:
            return print("---Файл readme.txt не найден!---\n")

    # settings f1
    info_window = Toplevel(root)
    x = (info_window.winfo_screenwidth() - info_window.winfo_reqwidth()) / 2
    y = (info_window.winfo_screenheight() - info_window.winfo_reqheight()) / 2
    info_window.wm_geometry("+%d+%d" % (x - 160, y - 120))
    info_window.geometry("320x240")
    info_window.resizable(0, 0)
    info_window.title("VKCB v.0.2")
    info_window.iconbitmap('icon.ico')
    info_window.focus_set()
    info_window.bind("<Return>", info_window_enter)
    info_window.protocol("WM_DELETE_WINDOW", info_window_close)

    vkcb_label_f1 = Label(info_window,
                          text="VKCB",
                          fg="steel blue",
                          font="Impact 50")
    vkcb_label_f1.place(x=90, y=-7)

    author_label_f1 = Label(info_window,
                            text="Автор:",
                            font="Calibri 10",
                            justify=CENTER)
    author_label_f1.place(x=106, y=70)

    ilkatkov_f1 = Label(info_window,
                        text="Илья Катков",
                        font="Calibri 10",
                        fg="blue",
                        justify=CENTER)  # ilkatkov
    ilkatkov_f1.place(x=145, y=70)
    ilkatkov_f1.bind("<Button-1>", vk)

    alt3s_f1 = Label(info_window,
                     text="Alt+3 Studio",
                     font="Calibri 10",
                     fg="blue",
                     justify=CENTER)  # Alt+3 Studio
    alt3s_f1.place(x=128, y=90)
    alt3s_f1.bind("<Button-1>", vk_alt3s)

    info_label_f1 = Label(info_window, text="Бесплатная утилита для создания\nчат-ботов в Вконтакте.",
                          font="Calibri 10", justify=CENTER)
    info_label_f1.place(x=65, y=120)

    ok_btn = Button(info_window,
                    text="OK",
                    width=10,
                    font="Calibri 11",
                    command=info_window_close)
    ok_btn.place(x=40, y=190)

    readme_btn = Button(info_window,
                    text="Открыть Readme",
                    width=16,
                    font="Calibri 11",
                    command=readme)
    readme_btn.place(x=150, y=190)

# open help for token
def token_web(event):
    webbrowser.open_new(r'https://vk.com/dev/access_token?f=2.%20Ключ%20доступа%20сообщества')


# open vkcb
def vkcb_web(event):
    webbrowser.open_new(r'https://vk.com/vkcb_app')


# open alt3s
def alt3s_web(event):
    webbrowser.open_new(r'https://vk.com/alt3s')


# insert token from clipboard
def token_clip():
    token_entry.delete(0, END)
    token_entry.insert(0, pyperclip.paste())


string = "keyboard = {\"one_time\": False, \"buttons\": ["


# create new .py chat-bot
def create():
    try:
        global if_count
        global key_count

        # all in white
        def all_white():
            name_entry['bg'] = 'white'
            token_entry['bg'] = 'white'
            first_if_user_word['bg'] = "white"
            first_if_bot_word['bg'] = "white"
            for i in range(2, if_count + 1):
                exec("if_user_word_{0}[\'bg\'] = \"white\"".format(str(i)), globals())
                exec("if_bot_word_{0}[\'bg\'] = \"white\"".format(str(i)), globals())
            for i in range(1, key_count + 1):
                exec("key_{0}[\'bg\'] = \"white\"".format(str(i)), globals())
            else_entry_bot_word['bg'] = "white"

        all_white()

        imports_file = open('codes/imports.py', 'r')
        imports_code = imports_file.readlines()
        imports_file.close()

        get_button_file = open('codes/samples/sample_get_button.py', 'r')
        get_button_code = get_button_file.readlines()
        get_button_file.close()

        sample_begin_file = open('codes/samples/sample_begin.py', 'r')
        sample_begin_code = sample_begin_file.readlines()
        sample_begin_file.close()

        sample_end_file = open('codes/samples/sample_end.py', 'r')
        sample_end_code = sample_end_file.readlines()
        sample_end_file.close()

        check_name = True
        for symbol in name_entry.get().strip().lower():
            if symbol not in true_alphabet:
                check_name = False
                break

        if name_entry.get().strip() == "":
            name_entry['bg'] = "tomato"
            return mb.showerror("VKCB", "Добавьте имя чат-бота!")
        elif check_name == False:
            name_entry['bg'] = "tomato"
            return mb.showerror("VKCB", "Имя бота может состоять только из латинских букв, цифр и знаков:\n-,  _, +, !, ', @, №, $, ;, (, ), ^, &, [, ], {, }.")
        elif token_entry.get().strip() == "":
            token_entry['bg'] = "tomato"
            return mb.showerror("VKCB", "Добавьте API-ключ!")
        elif first_if_user_word.get().strip() == "":
            first_if_user_word['bg'] = "tomato"
            return mb.showerror("VKCB", "Заполните пустой ввод пользователя!")
        elif first_if_bot_word.get().strip() == "":
            first_if_bot_word['bg'] = "tomato"
            return mb.showerror("VKCB", "Заполните пустой ответ бота!")
        elif else_entry_bot_word.get().strip() == "":
            else_entry_bot_word['bg'] = "tomato"
            return mb.showerror("VKCB", "Заполните пустой ответ бота!")
        else:
            for i in range(2, if_count + 1):
                exec("if_user_word = if_user_word_{0}.get().strip()".format(str(i)), globals())
                exec("if_bot_word = if_bot_word_{0}.get().strip()".format(str(i)), globals())
                if if_user_word == "":
                    exec("if_user_word_{0}[\'bg\'] = \"tomato\"".format(str(i)), globals())
                    return mb.showerror("VKCB", "Заполните пустой ввод пользователя!")
                elif if_bot_word == "":
                    exec("if_bot_word_{0}[\'bg\'] = \"tomato\"".format(str(i)), globals())
                    return mb.showerror("VKCB", "Заполните пустой ответ бота!")

            for i in range(1, key_count + 1):
                exec("key_entry = key_{0}.get().strip()".format(str(i)), globals())
                if key_entry == "":
                    exec("key_{0}[\'bg\'] = \"tomato\"".format(str(i)), globals())
                    return mb.showerror("VKCB", "Заполните имя кнопки!")

            name_entry['bg'] = 'green yellow'
            token_entry['bg'] = 'green yellow'
            first_if_user_word['bg'] = "green yellow"
            first_if_bot_word['bg'] = "green yellow"
            for i in range(2, if_count + 1):
                exec("if_user_word_{0}[\'bg\'] = \"green yellow\"".format(str(i)), globals())
                exec("if_bot_word_{0}[\'bg\'] = \"green yellow\"".format(str(i)), globals())
            for i in range(1, key_count + 1):
                exec("key_{0}[\'bg\'] = \"green yellow\"".format(str(i)), globals())
            else_entry_bot_word['bg'] = "green yellow"

            way = 'chatbots\\vkcb_{0}.py'.format(name_entry.get().strip())
            new_file = open(way, 'w', encoding="utf-8")

            # write info
            new_file.write(f"# {name_entry.get().strip()}\n")
            new_file.write("# Made by VKCB\n")
            new_file.write('\n')

            # write imports..
            for line in imports_code:
                new_file.write(line)
            new_file.write('\n')

            # write api-key
            new_file.write(
                f'\ntoken = \"{token_entry.get().lower().strip()}\" # api-key\nvk = vk_api.VkApi(token=token)\nvk._auth_token()\n')
            new_file.write('\n')

            # write get_button..
            if key_count != 0:
                for line in get_button_code:
                    new_file.write(line)
                new_file.write('\n\n')

                global string

                for i in range(1, key_count + 1):
                    exec("key = key_{0}.get().strip()".format(str(i)), globals())
                    exec(
                        "string = string + \"[get_button(label = \"\"\'{0}\'\"\", color = \"\"\'default\'\"\")],\"".format(
                            str(key)), globals())

                string = string[0:len(string) - 1]
                string += "]}"
                new_file.write(string)
                string = "keyboard = {\"one_time\": False, \"buttons\": ["
                new_file.write("\n")
                new_file.write(
                    "keyboard = json.dumps(keyboard, ensure_ascii=False).encode(\'utf-8\')\nkeyboard = str(keyboard.decode(\'utf-8\'))")
                new_file.write("\n\n")

            # write name
            new_file.write(f"print(\"\\n---VKCB---\")\n")
            new_file.write(f"print(\"{name_entry.get().strip()}" + ": ON\")\n")
            new_file.write('\n')

            # write begin...
            for line in sample_begin_code:
                new_file.write(line)

            # write first if...
            new_file.write(
                "\n                    if user_word.lower() == \"" + first_if_user_word.get().strip().lower() + "\":\n                        " + "vk.method(\"messages.send\", {\"peer_id\": id, \"message\": \"" + first_if_bot_word.get().strip() + "\", \"keyboard\": keyboard, \"random_id\": random.randint(1, 2147483647)})")

            # write all elif...
            for i in range(2, if_count + 1):
                exec("if_user_word = if_user_word_{0}.get().strip()".format(str(i)), globals())
                exec("if_bot_word = if_bot_word_{0}.get().strip()".format(str(i)), globals())
                new_file.write(
                    "\n                    elif user_word.lower() == \"" + if_user_word.lower() + "\":\n                        " + "vk.method(\"messages.send\", {\"peer_id\": id, \"message\": \"" + if_bot_word + "\", \"keyboard\": keyboard, \"random_id\": random.randint(1, 2147483647)})")

            # write else...
            new_file.write(
                "\n                    else:\n                        " + "vk.method(\"messages.send\", {\"peer_id\": id, \"message\": \"" + else_entry_bot_word.get().strip() + "\", \"keyboard\": keyboard, \"random_id\": random.randint(1, 2147483647)})")
            new_file.write('\n')

            # write end...
            for line in sample_end_code:
                new_file.write(line)

            new_file.close()

            mb.showinfo("VKCB", "Чат-бот успешно создан!")
            ans = mb.askyesno("VKCB", "Показать чат-бота?")
            if ans == True:
                os.system('explorer /select, \"' + way + "\"")
            all_white()
    except FileNotFoundError:
        mb.showerror("VKCB", "Проверьте целостность файлов программы!\nРекомендуется переустановить VKCB.")


# add if_block
def plus_if():
    global if_count
    global if_next_y
    if if_count == 6:
        if_plus_button['state'] = DISABLED
    if if_count != 7:
        if_count += 1
        exec("if_label_{0} = Label(text = \"Если пользователь написал:\t\t\t   , то\", font = \"Calibri 10\")".format(
            str(if_count)), globals())
        exec("if_label_{0}.place(x = 315, y = {1})".format(str(if_count), str(if_next_y)), globals())
        exec("if_user_word_{0} = Entry(width = 20)".format(str(if_count)), globals())
        exec("if_user_word_{0}.place(x = 480, y = {1})".format(str(if_count), str(if_next_y)), globals())
        exec("if_label2_{0} = Label(text = \"ответить:\", font = \"Calibri 10\")".format(str(if_count)), globals())
        exec("if_label2_{0}.place(x = 315, y = {1})".format(str(if_count), str(if_next_y + 25)), globals())
        exec("if_bot_word_{0} = Entry(width = 20)".format(str(if_count)), globals())
        exec("if_bot_word_{0}.place(x = 370, y = {1})".format(str(if_count), str(if_next_y + 25)), globals())
        else_label.place_forget()
        else_label2.place_forget()
        else_entry_bot_word.place_forget()
        if_plus_button.place_forget()
        if_minus_button.place_forget()
        else_label.place(x=315, y=if_next_y + 100)
        else_label2.place(x=315, y=if_next_y + 120)
        else_entry_bot_word.place(x=370, y=if_next_y + 120)
        if_minus_button.place(x=425, y=if_next_y + 48)
        if_minus_button['state'] = NORMAL
        if_plus_button.place(x=315, y=if_next_y + 48)
        if_next_y += 50
    else:
        pass


# remove if_block
def minus_if():
    global if_count
    if if_count == 2:
        if_minus_button['state'] = DISABLED
    if if_count != 1:
        global if_next_y
        exec("if_label_{0}.place_forget()".format(str(if_count)), globals())
        exec("if_label2_{0}.place_forget()".format(str(if_count)), globals())
        exec("if_user_word_{0}.place_forget()".format(str(if_count)), globals())
        exec("if_bot_word_{0}.place_forget()".format(str(if_count)), globals())
        else_label.place_forget()
        else_label2.place_forget()
        else_entry_bot_word.place_forget()
        if_plus_button.place_forget()
        if_minus_button.place_forget()
        if_minus_button.place(x=425, y=if_next_y - 52)
        if_plus_button.place(x=315, y=if_next_y - 52)
        if_plus_button['state'] = NORMAL
        else_label.place(x=315, y=if_next_y)
        else_label2.place(x=315, y=if_next_y + 20)
        else_entry_bot_word.place(x=370, y=if_next_y + 20)
        if_count -= 1
        if_next_y -= 50
    else:
        if_minus_button['state'] = DISABLED


# add key
def key_plus():
    global key_count
    global key_next_y
    key_minus_button['state'] = NORMAL
    key_count += 1
    key_plus_button.place_forget()
    key_minus_button.place_forget()
    exec("key_{0} = Entry(width = 39)".format(str(key_count)), globals())
    exec("key_{0}.place(x = 30, y = key_next_y)".format(str(key_count)), globals())
    key_plus_button.place(x=30, y=key_next_y + 23)
    key_minus_button.place(x=152, y=key_next_y + 23)
    key_next_y += 30
    if key_count == 7:
        key_plus_button['state'] = DISABLED


# remove key
def key_minus():
    global key_count
    global key_next_y
    key_plus_button.place_forget()
    key_minus_button.place_forget()
    exec("key_{0}.place_forget()".format(str(key_count)), globals())
    key_plus_button.place(x=30, y=key_next_y - 37)
    key_plus_button['state'] = NORMAL
    key_minus_button.place(x=152, y=key_next_y - 37)
    key_count -= 1
    key_next_y -= 30
    if key_count == 0:
        key_minus_button['state'] = DISABLED


# user interface
root = Tk()
root.geometry("900x500")
root.resizable(0, 0)
root.title("VKCB - бесплатные чат-боты")
root.iconbitmap('icon.ico')
root.bind("<F1>", info_window_f1)  # F1

# keyboard
key_count = 0
key_next_y = 235

keyboard_frame = Frame(height=280, width=268, relief=RAISED, borderwidth=2)
keyboard_frame.place(x=20, y=193)
keyboard_label = Label(text="Кнопки:", font="Calibri 15")
keyboard_label.place(x=30, y=195)
key_plus_button = Button(text="Добавить кнопку", width=15, command=key_plus)
key_plus_button.place(x=30, y=228)
key_minus_button = Button(text="Удалить кнопку", width=15, command=key_minus, state=DISABLED)
key_minus_button.place(x=152, y=228)

# programming
if_count = 1
if_next_y = 90

program_label = Label(text="Программирование бота:", font="Calibri 15")
program_label.place(x=315, y=10)

first_if_label = Label(text="Если пользователь написал:\t\t\t   , то", font="Calibri 10")
first_if_label.place(x=315, y=40)
first_if_user_word = Entry(width=20)
first_if_user_word.place(x=480, y=40)
first_if_label2 = Label(text="ответить:", font="Calibri 10")
first_if_label2.place(x=315, y=65)
first_if_bot_word = Entry(width=20)
first_if_bot_word.place(x=370, y=65)

if_plus_button = Button(text="Добавить фразу", font="Calibri 10", command=plus_if)
if_plus_button.place(x=315, y=88)

if_minus_button = Button(text="Удалить фразу", font="Calibri 10", command=minus_if, state=DISABLED)
if_minus_button.place(x=425, y=88)

else_label = Label(text="Если бот не знает введенной фразы, то", font="Calibri 10")
else_label.place(x=315, y=140)
else_label2 = Label(text="ответить:", font="Calibri 10")
else_label2.place(x=315, y=160)
else_entry_bot_word = Entry(width=20)
else_entry_bot_word.place(x=370, y=160)

# guide
guide_frame_right = Frame(height=650, width=250, bg="steel blue")
guide_frame_right.place(x=670, y=0)
guide_label_right = Label(
    text="Особенности ввода сообщений:\n\n" + r"Переход на новую строку - \n" + "\n" + r"Табуляция - \t " + "\n\n" + r"Двойные кавычки - \”" + "\n" + r"Апостроф - \’",
    font="Calibri 10", justify=LEFT)
guide_label_right.place(x=693, y=10)
guide_frame_left = Frame(height=185, width=268, relief=RAISED, borderwidth=2)
guide_frame_left.place(x=20, y=5)

# name of bot
name_label = Label(text="Имя чат-бота:", font="Calibri 15")
name_label.place(x=30, y=10)

name_entry = Entry(width=39)
name_entry.place(x=30, y=40)

# api-key
token_label = Label(text="API-ключ:", font="Calibri 15")
token_label.place(x=30, y=77)

token_entry = Entry(width=39)
token_entry.place(x=30, y=107)

token_pst = Button(text="Вставить из буфера", font="Calibri 11", command=token_clip)
token_pst.place(x=30, y=130)

token_help = Label(text="Где найти?", font="Calibri 8", fg="blue")
token_help.place(x=30, y=162)
token_help.bind("<Button-1>", token_web)

vkcb_label = Label(text="VKCB", font="Impact 60", bg="steel blue", fg="whitesmoke")
vkcb_label.place(x=700, y=125)
vkcb_label.bind("<Button-1>", vkcb_web)
alt3s_label = Label(text="Alt+3 Studio", font="Calibri 16", bg="steel blue", fg="whitesmoke")
alt3s_label.place(x=730, y=215)
alt3s_label.bind("<Button-1>", alt3s_web)

# finish
finish = Button(text="Создать чат-бота", font="Calibri 11", command=create)
finish.place(x=730, y=450)

root.mainloop()