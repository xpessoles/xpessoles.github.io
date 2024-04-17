---
title: Divers, Bac à sable
---


:material-information-outline:{ title="Important information" }

[Hover me][example]

  [example]: https://example.com "I'm a tooltip!"

Coucouucu

 
[Exemple a][exa]

  [exa]: https://example.com "I'm a tooltip! ![Image title](https://dummyimage.com/120x80/eee/aaa){ align=left }"


## TEST

- [Abbreviations]
- [Attribute Lists]
- [Snippets]

  [Abbreviations]: Divers/python-markdown.md#abbreviations
  [Attribute Lists]: Divers/python-markdown.md#attribute-lists
  [Snippets]: Divers/extensions/python-markdown-extensions.md#snippets
 

## FIN TEST

blabla




## Configuration
* mkdocs-material
* Github
* Visualisation en local 
## Bac à sable


Du `Python`

## Encore du code
``` 
def coucou(): # Rien
    return True
```

``` py
def coucou(): # py
    return True
```

``` py title="titre"
def coucou(): # py
    return True
```

``` py linenums="1"
def coucou(): # py
    return True
```


``` py linenums="1",title="Titre + numérotation"
def coucou(): # py
    return True
```


``` tex
def coucou(): % tex
    return True
```


!!! tip Test admonition 
Test
!!!


??? tip Test admonition 
Test

???



For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
