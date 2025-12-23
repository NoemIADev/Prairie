# Comprendre une requête HTTP
Internet est largement utilisé pour permettre aux machines de communiquer entre elles.
Voici un exemple de requête HTTP :
```bash 
GET https://dummyjson.com:443/recipes?limit=10 HTTP/2
```
L’objectif est d’analyser la nature, le type et le format des éléments de cette requête.
## **Qu'est-ce qu’une requête HTTP ?**

Une requête HTTP est un **message envoyé par un client à un serveur** afin de demander une action précise, comme récupérer des données, envoyer des informations ou modifier une ressource.

## **Qu'est-ce qu’un DNS ?**

Le *DNS* (Domain Name System) est un système qui permet de traduire un **nom de domaine** lisible par l’humain (ex : dummyjson.com) en **adresse IP** compréhensible par les machines.

## **Qu'est-ce que GET ?**

*GET* est une méthode HTTP.
Elle sert à demander des données au serveur sans modifier l’état des ressources.

### **mais c'est quoi une methode http ?**

👉 Une méthode HTTP indique **l’action que le client demande au serveur**.

Par exemple :

GET : demander des informations

POST : envoyer des informations

UDAPTE : mettre à jours des informations

DELETE : supprimer des informations

Il en existe plusieurs, mais pour faire court, cela veut dire : « je veux faire ça ».

## **Qu'est-ce que HTTPS ?**

*HTTPS* est la **version sécurisée** du protocole HTTP.
Les échanges entre le client et le serveur sont chiffrés, ce qui garantit la confidentialité et l’intégrité des données échangées.
**Version courte**: HTTPS, c’est comme dire : “coucou, confirme-moi que c’est bien toi, et parlons en privé”.

## **Qu'est-ce que dummyjson.com ?**

*dummyjson.com* est le nom de domaine du serveur ciblé par la requête,tout simplement.

## **Qu'est-ce que le port 443 ?**

Le port *443* est le port standard utilisé pour les communications HTTPS.
Il **indique** au serveur **sur quel canal réseau** la communication doit avoir lieu.
**version courte**: Tu frappes à la porte 443 parce que c’est la porte d’entrée du HTTPS.

## **Qu'est-ce que recipes ?**

*Recipes*, c’est ce que l’on veut “*GET*” sur le serveur.C'est **ce qu'on demande**.

## **Qu'est-ce que "?" ?**

Le caractère *?* indique que l’on va **ajouter des précisions** à la demande.
c’est comme dire : “*je veux ça, mais avec ces détails*”.

## **Qu’est-ce que limit ?**

*limit* est un paramètre de requête.
Il permet d’indiquer une **contrainte** sur la réponse attendue, par exemple le nombre maximum d’éléments.

## **Qu’est-ce que 10 ?**

*10* est la valeur **associée** au paramètre *limit*.
Cela signifie que la requête **demande un maximum de 10 éléments** dans la réponse.

## **Qu’est-ce que HTTP/2 ?**

HTTP/2 est la version du protocole HTTP utilisée pour la communication

### En conclusion

À quoi ça sert ? Pas forcément à grand-chose au quotidien.
Mais savoir ce que l’on tape aide à comprendre ce que l’on fait, à éviter les erreurs et à ne pas agir “au hasard”.