1.play.py - это консольная игра, написанная в основном без использования библиотек.

использовона библиотека random для рандомизации характеристик враждебных персонажей (здоровье, броня, атака, деньги), чтобы игра была разнообразной и интересной.
Библиотека time используется для отслеживания времени прохождения игры.
В игре представлен выбор из 4 персонажей.
Игра на данный момент не отбалансирована.

2.tanks.py - это 2D игра про танки, написанная с использованием библиотеки pygame.

Библиотека random используется для создания случайных карт.
В игре есть несколько типов блоков (стен): 
  а) Вода - это барьер, через который танк не может проехать, но через который могут пролететь пули.   
  б) Кирпичная стена - танк врезается в нее и останавливается, но ее можно разрушить снарядом.
  в) Кусты - можно в них спрятаться. г) Металлический контейнер - говорят, он сделан из вибраниума (его нельзя сломать). 
  д) Деревянные коробки - пытался сделать так, чтобы их можно было двигать, но не получилось, как и взрыв танка на мине.
В игре есть некоторые баги и недоработки.