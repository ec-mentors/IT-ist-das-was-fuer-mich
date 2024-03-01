#%%
participants = [
"özlem-celik",
"rasha-aboeed",
"rama-al jaradat",
"edel-faizief",
"razia-nazari",
"aleksandra-skrodziuk",
"lesina-haicharoeva",
"fehime-gül-dikmen",
"michelle-lehner",
"fatima-haidari",
"hadischat-rashapova",
"michelle-chvojka",
"nyima-conteh",
"sarah-amjad-bhatti",
"kenda-tahle",
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
