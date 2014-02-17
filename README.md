vokativ
=======

#### Oslovte své uživatele správně!


Instalace
=========

    $ pip install vokativ

Podporované verze Pythonu 2.6, 2.7, 3.x.

Použití
=======

```
>>> from vokativ import vokativ
>>> vokativ('Michal')
u'michale'
>>> vokativ('Petr')
u'petře'
>>> vokativ('Adriana', woman=True)
u'adriano'
>>> vokativ(u'Fialová', woman=True, last_name=True)
u'fialová'
```

Funkce *vokativ()* bere jako první argument vlastní jméno v 1. pádu jednotného čísla a vrátí ho vyskloňované v 5. pádu.
Návratová hodnota funkce je vždy řetězec s malými písmeny typu *unicode*.
Upozorňujeme, že funkce nemusí správně fungovat pro cizí jména.

### Další argumenty jsou:

#### woman 
*(výchozí hodnota False)*

Použijte True, pokud si přejete skloňovat ženská jména.

#### last_name
*(výchozí hodnota False)*

Použijte True, pokud si přejete skloňovať příjmení. Pro ženská jména se pak
skloňování chová malinko jinak (viz níže).


Algoritmus skloňování
=====================

### Mužská jména

Skloňování mužských jmen je založeno na koncovkách slov. V souboru [vokativ/man_suffixes](https://github.com/Mimino666/vokativ/blob/master/vokativ/man_suffixes)
je seznam pravidel, podle kterých se skloňuje. Například pravidlo: ```tr tře``` znamená, že pokud
zadané jméno končí na písmena "tr", tak je nahradíme písmeny "tře". Podle tohoto pravidla se
skloňuje například:
```
    Petr      =>  Petře
    Silvestr  =>  Silvestře
```

Pravidla zkoušíme v pořadí od nejdelších po nejkratší. Proto má pravidlo ```gintr gintre``` přednost před pravidlem ```tr tře```.
Pokud žádné pravidlo není možné aplikovat, k zadanému jménu připojíme "e". Například:
```
    Helmut    =>  Helmute
```


### Ženská jména

Pro ženská jména je situace velmi jednoduchá. Pokud se jedná o křestní jméno,
skloňujeme jen jména končící na "a".
Například:
```
    Jana      =>  Jano
    Tereza    =>  Terezo
```
ale už ne:
```
    Dagmar    =>  Dagmar
    Marie     =>  Marie
```


V případě příjmení nedochází ke skloňování nikdy:
```
    Nováková  =>  Nováková
    Ivanova   =>  Ivanova
```
