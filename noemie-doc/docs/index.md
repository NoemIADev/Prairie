# Bienvenue dans la prairie

Ce site sert a documenté tout les projets fait au cours de ma formation de DEV IA.

## Comment mettre à jour ma doc ?

* Pour mettre à jour la documentation, il suffit de modifier ou d’ajouter des fichiers Markdown (`.md`) dans le dossier `docs`.

Pour visualiser les modifications en local :
`python -m mkdocs serve`

* Une fois les changements terminés, il faut les publier en ligne :

```bash 
git add .
git commit -m "Mise à jour de la documentation"
git push
python -m mkdocs gh-deploy
```
Une fois fini la console vous indiquera la lien de la page.
