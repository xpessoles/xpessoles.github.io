---
title: Tracer de courbes En construction.
---

[comment]: <> (Page manuelle)


Il y a de grandes chances pour que vous ayez besoin de tracer des courbes dans le cadre de votre TIPE.
Plus que jamais, je vous conseille d'utiliser `Python` et `Matplotlib`. 

Le rendu des courbes réalisées avec Regressi est assez souvent décevant.




## Chargement d'un fichier csv

Un fichier [csv]("comma separated values") est un fichier texte dans lequel les données sont séparées par des virgules, des point-virgules, des tabulations (ou d'autres caractères).
Prenons par exemple les premières lignes d'un fichier de mesure. 

```
	masse A		
t	x	y	
0,000	-4,796	13,51
0,033	-6,786	11,37
``` 

La première ligne contient une information générale.
La deuxième ligne contient le titre des colonnes. Les lignes suivantes contiennent les données. Ces données sont des nombres, dont le séparateur est la virgules. Les données sont séparées par des tabulations. 

Il existe plusieurs méthodes permettant de charger un fichier `csv`

### Conversion des `,` en `.
Pour plus de facilité lors de l'import,   