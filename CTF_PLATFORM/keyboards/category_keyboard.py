from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import os
import yaml

# category keyboard
category_keyboard = []
path_cfg = "C:\\users\\kov27\\PycharmProjects\\CTF_PLATFORM\\tasks"
dirs_cfg = os.listdir(path_cfg)


category = []
kostyl = []
for name in dirs_cfg:
    file_cfg = open(path_cfg + '\\' + name + '\\' + 'config.yml', 'r', encoding='utf8')
    name_category = str(yaml.load(file_cfg)['category'])
    # delete the same item
    if name_category in kostyl:
        pass
    else:
        kostyl.append(name_category)
        category.append(InlineKeyboardButton(name_category, callback_data=name_category))
        # sort by 3 item in string
        if len(category) == 3:
            category_keyboard.append(category)
            category = []

category_markup = InlineKeyboardMarkup(category_keyboard, one_time_keyboard=True)



