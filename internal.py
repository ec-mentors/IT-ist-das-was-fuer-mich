#%%
participants = [
"Ash-Abdel-Aziz",
"Loli-Amin",
"Mariam-Barakzai",
"Eda-Demirel",
"Muki-Erkan",
"Nana-Erkhembayarova",
"Ashley-Gravogel",
"Šejla-Hodović",
"Ash-Hohenberger",
"Zaira-Kamurkaeva",
"Ana-Lazic",
"Andjela-Rozic",
"Sani-Toor",
"Andja-Vencic-Peric"
]
#%%
import os

for participant in participants  :
    path = f"{os.path.join('source/participants', participant)}.md"

    title = participant.replace('-', ' ')
    title = title.title()
    with open(path, 'w') as fh:
        fh.write(f'# {title}')


# %%
