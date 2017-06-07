# django-api


Pour appel à l'API Youtube

https://developers.google.com/youtube/v3/docs/search/list
envoyer en parametre q= "nom de la chanson"
type peut être nul.
récupere le premier videoId trouvé et cela donne l'url de la vidéo : https://www.youtube.com/watch?v=videoID


url exemple qui fonctionne : https://www.googleapis.com/youtube/v3/videos?id=Z_XwtGvpEIs&part=snippet,contentDetails,statistics&key=AIzaSyCkORoK67IHPIpryEg1ajQxCGz_Fc6rz0g
