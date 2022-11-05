from random import choice
from glob import glob


def comment_avatar():

    avatars_images = [
        "avartar1.PNG",
        "avartar2.PNG",
        "avartar3.PNG",
        "avartar4.PNG",
        "avartar5.PNG",
        "avartar6.PNG",
    ]

    return choice(avatars_images)


random_picture = comment_avatar()

print(random_picture)
