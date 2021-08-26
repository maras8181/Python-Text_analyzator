Engeto: Project 1
===
První program na online python akademii od Engeta.
Tento program je psán na základě zkušeností nabraných za 1 měsíc studia python Akademie. Psaní kódu trvalo 10 hodin.

Popis zadání
---
Tento program slouží k analyzování textů, kde uživatel má na vyběr 1 ze tří možností. Tyto texty jsou dostupné [zde](https://engeto.com/files/task_template.py)
1. Vyžádá si od uživatele přihlašovací jméno a heslo.
2. Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů v předem definovaném slovníku.
3. Pokud je uživatel registrovaný, pozdrav jej a umožni mu analyzovat texty. Pokud není, upozorni jej a ukonči program.
4. Program nechá uživatel vybrat mezi třemi texty, uloženými v proměnné TEXTS. Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí. Pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.
6. Pro vybraný text spočítá následující statistiky:
  - počet slov,
  - počet slov začínajících velkým písmenem,
  - počet slov psaných velkými písmeny,
  - počet slov psaných malými písmeny,
  - počet čísel (ne cifer),
  - sumu všech čísel (ne cifer) v textu.
7. Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. Například takto:
```
username:bob
password:123
----------------------------------------
Welcome to the app, bob
We have 3 texts to be analyzed.
----------------------------------------
Enter a number btw. 1 and 3 to select: 1
----------------------------------------
There are 54 words in the selected text.
There are 12 titlecase words.
There are 1 uppercase words.
There are 38 lowercase words.
There are 3 numeric strings.
The sum of all the numbers 8510
----------------------------------------
LEN|  OCCURENCES  |NR.
----------------------------------------
  1|*             |1
  2|*********     |9
  3|******        |6
  4|***********   |11
  5|************  |12
  6|***           |3
  7|****          |4
  8|*****         |5
  9|*             |1
 10|*             |1
 11|*             |1
```

Popis programu:
---
ř. 32 - ř. 49
Na začátku programu jsem postupoval tak, že jsem vyzval uživatele, aby zadal vstupní data. Těmito daty je jméno a heslo uživatele. Tyto dva vstupy jsem obalil do ```while``` smyčky, která skončí ve chvíli, kdy uživatel nezadá prázdný řetězec. Jakmile se vyskočí ze smyčky ven, následuje podmínka, která ověřuje, zda je jméno uživatele registrované v předem daném slovníku. V opačném případě program uživatele upozorní a následně skončí.

ř. 53 - ř. 75
V další části programu je od uživatele vyžadováno zadání celého čísla v rozmezí 1-3. Každé číslo určuje jeden ze tří textů. Tato část kódu je obalena do ```while``` smyčky, kderá se přeruší ve chvíli, kdy uživatel nezadá prázdný text. Následně se oveřuje zadaný vstup pomocí podmínky ```if```. Program pokračuje ve chvíli, zda vstup odpovídá číslu v rozmezí 1-3. V opačném případě je uživatel upozorněn a program skončí.

ř. 76 - ř. 83
Následné probíhá výcuc slov ze zvoleného textu.
Nejprve si rozdělíme text na jednotlivá slova. Ty pak očistíme od interpunkcí a přidáme do listu ```splited_text_clear```. Tento list projíždíme ```for``` cyklem a do jednotlivých listů přiřazujeme jak délku jednotlivého slova, tak i ```stringy```, které jsou psané malýmy písmeny, velkými, a které mají velké pouze počáteční písmeno. Přidáváme ale i numerické ```stringy```, které převedeme na datový typ ```integer``` a později tento list sečteme pomocí funkce ```sum()```.

ř. 95
V poslední části kódu si převedeme list ```numbers_of_length``` na množinu, která nám vymaže duplicity. Následně tuto množinu projížíme ```for``` cyklem, kde zjišťujeme četnost t jednotlivého čísla právě z listu ```numbers_of_length```, tohle číslo pak přidáme do listu ```frequency_numbers```. Z tohoto listu si zjistíme největší číslo, bude nám určovat, kolikrát se má vypsat mezera a hvězdička.
Nyní projedeme množinu čísel ```for``` cyklem. Dalším příkazem si zjistíme počet mezer. Počet mezer určuje zarovnanost našeho grafu. Nakonec se tedy vypíše na každý řádek hvězdička tolikrát, kolikrát je dané číslo v mnnožině obsazeno v listu ```numbers_of_length```. Zbylé znaky budou obsahovat právě mezery, který se rovná rozdílu nejvyššího čísla v  listu ```frequency_numbers``` a počtu výskytů množinového čísla v listu ```numbers_of_length```.
