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
>>> vokativ('Petr')
u'petře'
>>> vokativ(u'Novák')
u'nováku'
>>> vokativ('Adriana')
u'adriano'
>>> vokativ(u'Fialová')
u'fialová'
```

Funkce **vokativ()** bere jako první argument vlastní jméno v 1. pádu jednotného čísla a vrátí ho vyskloňované v 5. pádu.
Návratová hodnota funkce je vždy řetězec s malými písmeny typu *unicode*.
Upozorňujeme, že funkce nemusí fungovat správně pro jména cizího původu.

### Další volitelné argumenty jsou:

#### woman

Použijte *True*, pokud si přejete zadané jméno skloňovat jako ženské.

Použijte *False*, pokud si přejete zadané jméno skloňovat jako mužské.

Ve výchozím případě je pohlaví detekováno automaticky.

```
>>> vokativ('Michel')  # automaticky skloňuje jako mužské jméno
u'micheli'
>>> vokativ('Michel', woman=False)
u'micheli'
>>> vokativ('Michel', woman=True)
u'michel'
```

#### last_name

Použijte *True*, pokud si přejete zadané jméno skloňovat jako příjmení.

Použijte *False*, pokus si přejete zadané jméno skloňovat jako křestní jméno.

Ve výchozím případě je typ jména detekován automaticky.

Hodnota tohoto parametru ovlivňuje pouze skloňování ženských jmen.

```
>>> vokativ('Ivanova')  # automaticky skloňuje jako příjmení
u'ivanova'
>>> vokativ('Ivanova', last_name=True)
u'ivanova'
>>> vokativ('Ivanova', last_name=False)
u'ivanovo'
```

Automatická detekce pohlaví
===========================

Knihovna **vokativ** poskytuje taky jednoduchou funkci na detekci pohlaví podle křestního jména či příjmení.
Pro četnosti jmen v ČR podle [statistického úřadu](http://www.mvcr.cz/clanek/cetnost-jmen-a-prijmeni-722752.aspx)
funkce funguje správně v 99.7% případů.

```
>>> from vokativ import sex
>>> sex('Michal')
'm'
>>> sex('Novák')
'm'
>>> sex('Tereza')
'w'
>>> sex(u'Nováková')
'w'
```
