import requests


def download_clip(video_link, video_name):
    response = requests.get(video_link)

    if response.status_code == 200:

        contenu_video = response.content
        with open("twitch/videos/" + video_name + ".mp4", "wb") as f:
            f.write(contenu_video)
        print("La vidéo a été téléchargée avec succès.")

    else:
        print("La requête a échoué avec le code d'erreur :", response.status_code)
