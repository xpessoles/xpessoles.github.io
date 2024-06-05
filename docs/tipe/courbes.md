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

Il existe plusieurs méthodes permettant de charger un fichier `csv` :
 * lecture et parsage du fichier texte;
 * chargement du fichier avec `laoadtxt` de la bibliothèque `numpy`;
 * utiliser `panda`. 



### Conversion des `,` en `.`
Pour plus de facilité lors de l'import, il est préférable de remplacer toutes les virgules par des points avant l'import sur Python.

### Chargement du fichier avec `laoadtxt`

``` py title="Chargement du fichier avec des ."
import numpy as np 
t,x,y =np.loadtxt("data_02.txt", dtype=float, skiprows=2, delimiter="\t", unpack=True, usecols=(0,1,2))
``` 

Les options choisies ici sont les suivantes :
 * `dtype` : typage des variables en flottants;
 * `skiprows=2` : on saute 2 lignes car il y a du texte sur ces deux lignes;
 * `delimiter="\t"` : les champs sont séparés par des tabulations;
 * `unpack=True` : séparer les colonnes dans des variables différentes;
 * `usecols=(0,1,2)` : sélection des colonnes à charger.