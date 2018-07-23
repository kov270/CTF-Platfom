from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import os
import yaml


# task keyboard
def tasks(category):
    task_keyboard = []
    path_cfg = "C:\\users\\kov27\\PycharmProjects\\CTF_PLATFORM\\tasks"
    dirs_cfg = os.listdir(path_cfg)

    task = []
    for name in dirs_cfg:
        file_cfg = open(path_cfg + '\\' + name + '\\' + 'config.yml', 'r', encoding='utf8')
        file = yaml.load(file_cfg)
        name_task = (file['name'])
        category_task = file['category']
        if category_task == category:
            task.append(InlineKeyboardButton(name_task, callback_data=name_task))
            # sort by 3 item in string
            if len(task) == 3:
                task_keyboard.append(task)
                task = []
            elif len(task) <3:
                task_keyboard.append(task)

    task_markup = InlineKeyboardMarkup(task_keyboard, one_time_keyboard=True)
    return task_markup

