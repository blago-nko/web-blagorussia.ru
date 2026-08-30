---
title: "Программное обеспечение комплексного расчета транспортных систем городов"
date: 2020-11-04
description: "Предыдущая страница Оглавление Следующая страница Программное обеспечение комплексного расчета транспортных систем городов В г. Воронеже пос..."
aliases:
  - "/2020/11/programmnoe-obespecenie-kompleksnogo-rasceta-transportnyh-sistem-gorodov.html"
url: "/programmnoe-obespecenie-kompleksnogo-rasceta-transportnyh-sistem-gorodov/"
---

|  |  |  |
| --- | --- | --- |
| [Предыдущая страница](http://www.blagorussia.ru/generalnyj-plan-goroda-voronez/metodika-rasceta-passaziro--i-avtomobilepotokov-v-kts-na-osnove-komputernyh-tehnologij) | [Оглавление](http://www.blagorussia.ru/generalnyj-plan-goroda-voronez/tom-i-cast-2) | [Следующая страница](http://www.blagorussia.ru/generalnyj-plan-goroda-voronez/harakteristika-transportnyh-podrajonov-goroda-voroneza-po-osnovnym-pokazatelam-dla-provedenia-rasceetov-passaziro--i-avtomobilepotokov) |

## **Программное обеспечение комплексного расчета транспортных систем городов**

В г. Воронеже постоянно растет количество новых жилых районов и, соответственно, число новых жителей, которым просто необходимо ездить на работу, по делам, за покупками и т. д… Для решения многих проблем распределения транспортных потоков и перевозок, а также облегчения анализа уже созданных проектов транспортных сетей городов, экономии времени проектировщиков-градостроителей при рассмотрении вариантов, и повышения эффективности проектирования дорожно-транспортных магистралей в городах была разработана программа – “ПЕРЕВОЗКИ XXI” (далее Программа).

 Непосредственно Программа предназначена для расчета перевозок пассажиров в городах, по дорогам, магистралям а, также, на скоростных видах транспорта: железные дороги, скоростной трамвай, метрополитен, монорельс, “лёгкого метро” и др.

Программа базируется на языке программирования Бейсик (Basic) для операционной системы “Windows”. Ранее расчёты кратчайших путей производились по “Волновому” методу, – который оказался наименее пригоден для разработки эффективной и работоспособной программы на ПК.

В настоящее время, для поиска кратчайших путей в Программе используется ***модифицированный для ПК***алгоритм “Форда”

Вышеуказанный алгоритм нахождения кратчайших путей является наилучшим для ручного расчета, но для расчета на ПК он был “упрощён” до матричной модификации метода “Форда”

В результате расчета создаётся матрица из N\*N точек - содержащая все кратчайшие пути (в модифицированном варианте) и матрица всех затрат между точками.

Далее по суммам прибытия и убытия по районам рассчитываются перевозки и выдаются все окончательные результаты в виде матриц и таблиц.

Все расчеты записываются в постоянную память (на жесткий диск), после чего Программа может в реальном времени отображать всю необходимую статистическую информацию по любой схеме (а их количество практически ограничено только ресурсами компьютера) в виде таблиц и графиков, а также в реальном времени отображать саму схему в любом масштабе с требуемыми параметрами.

На данный момент Программа разработана на нескольких языках программирования:

1. В основном для удобства управления, интерфейса  и быстрого изменения возможных недостатков используется язык высокого уровня “Microsoft Visual Basic V5.0 professional” (или аналогичном, но более поздней версии).
2. Для ускорения вывода всей графической информации используются так называемые функции (API-Windows) –  Application Programming Interface. Это особая категория библиотек функций написанных разработчиками Windows-подобных систем на языках низкого уровня - что позволяет использовать их практически во всех приложениях. Такие API-функции стандартизированы для любой версии Windows и существенно влияют на производительность разработанной Программы
3. Все расчеты разработаны (и запрограммированы)  на языке Delphi 5.0 (или более высокой версии), который является самым эффективным языком для производства большого, циклического или рекурсивного количества расчетов с плавающей точкой. Эффективность данного языка программирования была проверена экспериментальным методом на большинстве современных языков программирования

Программа постоянно совершенствуется и является уникальной и наиболее быстродействующей программой на сегодняшний день для просчета всевозможных вариантов транспортных сетей города.

Числовые данные частично вводятся вручную. Схема вводится посредством обвода нужной схемы города с автоматическим вводом точек и ребер.

Для начала расчетов были произведены следующие основные действия  по схеме города г. Воронежа:

* занесена схема города в ПК вручную по координатам или в автоматическом режиме;
* созданы связи (ребра) между всеми необходимыми точками;
* введены все точки входящие в определённые условные районы

> введены суммы по прибытию и убыванию для каждого района;

* проверка введенных данных (корректировка данных);

Для города Воронежа ввод информации  занял в около 3 часов чистого времени при готовой цифровой схеме которая была преобразована в цифровой вид с помощью специальных программных средств.

 Для проведения расчета были использованы следующие данные по городу Воронежу:

1. Транспортная сеть в координатах (ГПТ и МУДС) в г. Воронеже в М. 1:25 000.
2. Подразделение города на укрупненные транспортно-планировочные  районы (70 районов).
3. Количество населения, проживающего в расчетных подрайонах.
4. Количество градообразующих и обслуживающих кадров.
5. Удельные веса подрайонов по прибытию по культурно-бытовым передвижениям (см. данные, приводимые в таблице № 1).
6. Количество отправлений в средние сутки или в часы “пик” по трудовым и культурно-бытовым целям
7. Количество прибытий в районы по трудовым и культурно-бытовым передвижениям в средние сутки года, или в часы “пик”.
8. Количество прибывающих в город из других городов и из пригородной зоны по видам транспорта со схемой железнодорожных станций, автовокзалов и подъездов к аэропортам.

В процессе работы с программой были введены номера точек, их координаты в реальном масштабе, цвет - для вывода на экран, скорость на каждом ребре в км/час, суммарная численность населения каждой точке, а также коэффициенты грузового транспорта.

На основе введенных данных были рассчитаны:

1. Кратчайшие пути из всех точек к любым другим точкам следования на основе реальных заданных координат точек в городе и скоростей движения между ними.
2. Величины корреспонденций пассажиров в зависимости от населённости районов и кратчайших путей. Расчет пассажироперевозок производится с учетом коэффициента пользования транспортом.
3. Затем была произведена обработка данных в интерактивном режиме, при этом Программа позволяет:

1. Рассчитывать необходимое количество схем или различных вариантов одной схемы (дублировать схемы, а также копировать и видоизменять данные)
2. Редактировать, дополнять, просматривать и выводить  любые уже введенные и рассчитанные данные на экран монитора, принтер, или в файл (графический или текстовый в зависимости от типа данных).
3. При выводе результатов на экран в виде графов осуществляется возможность интерактивного изменения масштаба, сканируемых скоростей и выбранных категорий магистральных улиц.
4. При выводе на экран программа позволяет интерактивно удалять и вставлять точки, ребра, вводить новые скорости по ребрам, находить кратчайшие пути из одной точки схемы в другую путем ввода только этих номеров точек.
5. Выводить картограммы по городу или его части  с выводом потоков транспорта в графическом виде, которые отражаются на экране монитора в разных цветах, в зависимости от направления движения (к центру или от центра) и в разном масштабе, а также с различными числовыми характеристиками.
6. Выводить картограмму потоков транспорта по интервалам (задаются интерактивно)
7. Выводить гистограмму по средним и средневзвешенным, с возможностью добавления нескольких схем одного города (вариантов) для сравнения.

  

|  |  |  |
| --- | --- | --- |
| [Предыдущая страница](http://www.blagorussia.ru/generalnyj-plan-goroda-voronez/metodika-rasceta-passaziro--i-avtomobilepotokov-v-kts-na-osnove-komputernyh-tehnologij) | [Оглавление](http://www.blagorussia.ru/generalnyj-plan-goroda-voronez/tom-i-cast-2) | [Следующая страница](http://www.blagorussia.ru/generalnyj-plan-goroda-voronez/harakteristika-transportnyh-podrajonov-goroda-voroneza-po-osnovnym-pokazatelam-dla-provedenia-rasceetov-passaziro--i-avtomobilepotokov) |

Поделиться

* Получить ссылку
* Facebook
* X
* Pinterest
* Электронная почта
* Другие приложения

Ярлыки:
[Воронеж](https://www.blagorussia.ru/search/label/%D0%92%D0%BE%D1%80%D0%BE%D0%BD%D0%B5%D0%B6)
[Генеральный план](https://www.blagorussia.ru/search/label/%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%BF%D0%BB%D0%B0%D0%BD)



### Комментарии

#### Отправить комментарий




### Популярные сообщения

[![Изображение](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhgSG21PyW3uyy9gRIrJtKW_kUnhoRKQurEbbgh3AB-QeObd1PbPEJRfpRUp9UIrPeFQOTuRwP57ZdPHiApc4O5ia53BfnKXH4T9ulanGJb0CnYM09ADPmPMVUJdSlrdiYmlnG66QCLYgep/s1600/%25D0%25BA%25D0%25BB%25D1%258E%25D1%2587%25D1%258C.jpg)](https://www.blagorussia.ru/2021/01/vidy-vlasti.html)

Автор:


[Александр Бобров](https://www.blogger.com/profile/03771662766477114754 "author profile")


[апреля 10, 2021](https://www.blagorussia.ru/2021/01/vidy-vlasti.html "permanent link")

### [Виды власти](https://www.blagorussia.ru/2021/01/vidy-vlasti.html)

Поделиться

* Получить ссылку
* Facebook
* X
* Pinterest
* Электронная почта
* Другие приложения

[Отправить комментарий](https://www.blagorussia.ru/2021/01/vidy-vlasti.html#comments)

[![Изображение](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_ubOiunilK6EZiGZ_dU5Aoe5XVQgssjrALIzVaevG80XhPSKgUXXp75O5K9kgXdgg19w_XCQSN3H1nm2zEPt6fLeGz3QpSC1LrrzXTrQo0_lLa-n9grMNG2vKBNaugXNxkxVH5DC0Wqe3/w458-h640/%25D0%25B3%25D0%25B5%25D0%25BD%25D0%25BF%25D0%25BB%25D0%25B0%25D0%25BD.jpg)](https://www.blagorussia.ru/2020/06/generalnyj-plan-goroda-voronezh.html)

Автор:


[Александр Бобров](https://www.blogger.com/profile/03771662766477114754 "author profile")


[июня 03, 2020](https://www.blagorussia.ru/2020/06/generalnyj-plan-goroda-voronezh.html "permanent link")

### [Генеральный план города Воронеж](https://www.blagorussia.ru/2020/06/generalnyj-plan-goroda-voronezh.html)

Поделиться

* Получить ссылку
* Facebook
* X
* Pinterest
* Электронная почта
* Другие приложения

[Отправить комментарий](https://www.blagorussia.ru/2020/06/generalnyj-plan-goroda-voronezh.html#comments)

[![Изображение](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjI2tQMIKYVOeVrTEtKwdxrWMdy2vtZO3e_zbzC7dlH0gy-lhqUg8gDi-hBwg5YtWv66MvzEXUtE_fGmlzsFAwC1gWn9XEkKlCTZUBI64vCwrw0TCfWnZuAMUCTEI_8kzIdBMLswxP7TkrpL8g-azifWE7y-PkDapSeYuS4m6G-C3QX6tRtKcNTjCBdWH8/w640-h640/kandinsky-download-1695312877484.png)](https://www.blagorussia.ru/2023/09/osnovnoe-primenenie-informacionnyh-tekhnologij-v-psihologii.html)

Автор:


[Артем Диденко](https://www.blogger.com/profile/04844297396744788167 "author profile")


[сентября 21, 2023](https://www.blagorussia.ru/2023/09/osnovnoe-primenenie-informacionnyh-tekhnologij-v-psihologii.html "permanent link")

### [Основное применение информационных технологий в психологии](https://www.blagorussia.ru/2023/09/osnovnoe-primenenie-informacionnyh-tekhnologij-v-psihologii.html)

Поделиться

* Получить ссылку
* Facebook
* X
* Pinterest
* Электронная почта
* Другие приложения

[Отправить комментарий](https://www.blagorussia.ru/2023/09/osnovnoe-primenenie-informacionnyh-tekhnologij-v-psihologii.html#comments)

Автор:


[Александр Бобров](https://www.blogger.com/profile/03771662766477114754 "author profile")


[мая 21, 2020](https://www.blagorussia.ru/2020/05/bankovskaa-sistema-osnovnoj-potrebitel-uslug-tajnyh-pokupatelej.html "permanent link")

### [Банковская система основной потребитель услуг тайных покупателей](https://www.blagorussia.ru/2020/05/bankovskaa-sistema-osnovnoj-potrebitel-uslug-tajnyh-pokupatelej.html)

Поделиться

* Получить ссылку
* Facebook
* X
* Pinterest
* Электронная почта
* Другие приложения

[Отправить комментарий](https://www.blagorussia.ru/2020/05/bankovskaa-sistema-osnovnoj-potrebitel-uslug-tajnyh-pokupatelej.html#comments)

Автор:


[Александр Бобров](https://www.blogger.com/profile/03771662766477114754 "author profile")


[января 04, 2021](https://www.blagorussia.ru/2021/01/tom-i-cast-1.html "permanent link")

### [Том I часть 1](https://www.blagorussia.ru/2021/01/tom-i-cast-1.html)

Поделиться

* Получить ссылку
* Facebook
* X
* Pinterest
* Электронная почта
* Другие приложения

[Отправить комментарий](https://www.blagorussia.ru/2021/01/tom-i-cast-1.html#comments)

[![Изображение](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUjVMbfqHU9nc38wl7TjcJJSDVYaeyv-ajtATvLZovQa_xmta6nlzf9HjGtmmUlvgmxm46CCsBsco0aGu5oyY2BwYHyoz6Ad2gKDKidUjhxV-KaEUTJgXn3MmZ5_N21PPeAIfv1x-FTNXA/w458-h640/%25D1%2581%25D1%2585+%25D0%25B3%25D0%25BE%25D1%2580%25D0%25BE%25D0%25B4%25D1%2581%25D0%25BA+%25D0%25BF%25D0%25B0%25D1%2581%25D1%2581%25D0%25B0%25D0%25B6%25D0%25B8%25D1%2580%25D1%2581%25D0%25BA%25D0%25BE%25D0%25B3%25D0%25BE+%25D1%2582%25D1%2580%25D0%25B0%25D0%25BD%25D1%2581%25D0%25BF.jpg)](https://www.blagorussia.ru/2020/11/sh-gorodsk-passazirskogo-transporta.html)

Автор:


[Александр Бобров](https://www.blogger.com/profile/03771662766477114754 "author profile")


[ноября 24, 2020](https://www.blagorussia.ru/2020/11/sh-gorodsk-passazirskogo-transporta.html "permanent link")

### [Схема городского пассажирского транспорта](https://www.blagorussia.ru/2020/11/sh-gorodsk-passazirskogo-transporta.html)

Поделиться

* Получить ссылку
* Facebook
* X
* Pinterest
* Электронная почта
* Другие приложения

[Отправить комментарий](https://www.blagorussia.ru/2020/11/sh-gorodsk-passazirskogo-transporta.html#comments)

Автор:


[Александр Бобров](https://www.blogger.com/profile/03771662766477114754 "author profile")


[июля 09, 2020](https://www.blagorussia.ru/2020/07/zilye-zony.html "permanent link")

### [Жилые зоны](https://www.blagorussia.ru/2020/07/zilye-zony.html)

Поделиться

* Получить ссылку
* Facebook
* X
* Pinterest
* Электронная почта
* Другие приложения

[Отправить комментарий](https://www.blagorussia.ru/2020/07/zilye-zony.html#comments)

Автор:


[Александр Бобров](https://www.blogger.com/profile/03771662766477114754 "author profile")


[сентября 19, 2020](https://www.blagorussia.ru/2020/09/karty-gradostroitelnogo-zonirovania.html "permanent link")

### [карты градостроительного зонирования](https://www.blagorussia.ru/2020/09/karty-gradostroitelnogo-zonirovania.html)

Поделиться

* Получить ссылку
* Facebook
* X
* Pinterest
* Электронная почта
* Другие приложения

[Отправить комментарий](https://www.blagorussia.ru/2020/09/karty-gradostroitelnogo-zonirovania.html#comments)

Автор:


[Александр Бобров](https://www.blogger.com/profile/03771662766477114754 "author profile")


[июня 12, 2020](https://www.blagorussia.ru/2020/06/11-inzenernaa-podgotovka-territorii.html "permanent link")

### [11. Инженерная подготовка территории](https://www.blagorussia.ru/2020/06/11-inzenernaa-podgotovka-territorii.html)

Поделиться

* Получить ссылку
* Facebook
* X
* Pinterest
* Электронная почта
* Другие приложения

[Отправить комментарий](https://www.blagorussia.ru/2020/06/11-inzenernaa-podgotovka-territorii.html#comments)

Автор:


[Александр Бобров](https://www.blogger.com/profile/03771662766477114754 "author profile")


[января 05, 2021](https://www.blagorussia.ru/2021/01/harakteristika-i-ocenka-ekologiceskogo-sostoania-vodnyh-obektov-g-voroneza.html "permanent link")

### [Характеристика и оценка экологического состояния водных объектов г. Воронежа](https://www.blagorussia.ru/2021/01/harakteristika-i-ocenka-ekologiceskogo-sostoania-vodnyh-obektov-g-voroneza.html)

Поделиться

* Получить ссылку
* Facebook
* X
* Pinterest
* Электронная почта
* Другие приложения

[Отправить комментарий](https://www.blagorussia.ru/2021/01/harakteristika-i-ocenka-ekologiceskogo-sostoania-vodnyh-obektov-g-voroneza.html#comments)




[Политика конфиденциальности](http://partnerstvo.blagorussia.ru/politika-konfidencialnosti)

![](https://mc.yandex.ru/watch/21798445)

![Top.Mail.Ru](https://top-fwz1.mail.ru/counter?id=2347426;js=na)

[Технологии Blogger](https://www.blogger.com)

@ 2010 - 2025 года





### Перевести - Translate

### Навигация по сайту

* [Главная страница](https://blagorussia.blogspot.com/)
* [Новости](https://novosti.blagorussia.ru/)
* [О проекте](https://blagorussia.blogspot.com/2021/01/home.html)

### Разделы

* [Архивы75](https://www.blagorussia.ru/search/label/%D0%90%D1%80%D1%85%D0%B8%D0%B2%D1%8B)
* [Бесплатные курсы3](https://www.blagorussia.ru/search/label/%D0%91%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D1%8B%D0%B5%20%D0%BA%D1%83%D1%80%D1%81%D1%8B)
* [Воронеж582](https://www.blagorussia.ru/search/label/%D0%92%D0%BE%D1%80%D0%BE%D0%BD%D0%B5%D0%B6)
* [Генеральный план490](https://www.blagorussia.ru/search/label/%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%BF%D0%BB%D0%B0%D0%BD)
* [Демография1](https://www.blagorussia.ru/search/label/%D0%94%D0%B5%D0%BC%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%8F)
* [Идеология48](https://www.blagorussia.ru/search/label/%D0%98%D0%B4%D0%B5%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F)
* [Италия1](https://www.blagorussia.ru/search/label/%D0%98%D1%82%D0%B0%D0%BB%D0%B8%D1%8F)
* [Новости241](https://www.blagorussia.ru/search/label/%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8)
* [Партнерство79](https://www.blagorussia.ru/search/label/%D0%9F%D0%B0%D1%80%D1%82%D0%BD%D0%B5%D1%80%D1%81%D1%82%D0%B2%D0%BE)
* [Психология1](https://www.blagorussia.ru/search/label/%D0%9F%D1%81%D0%B8%D1%85%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F)

* [Содействие занятости1](https://www.blagorussia.ru/search/label/%D0%A1%D0%BE%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%B8%D0%B5%20%D0%B7%D0%B0%D0%BD%D1%8F%D1%82%D0%BE%D1%81%D1%82%D0%B8)
* [Статистика107](https://www.blagorussia.ru/search/label/%D0%A1%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B0)
* [Технологии2](https://www.blagorussia.ru/search/label/%D0%A2%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8)
* [Цифровые профессии1](https://www.blagorussia.ru/search/label/%D0%A6%D0%B8%D1%84%D1%80%D0%BE%D0%B2%D1%8B%D0%B5%20%20%D0%BF%D1%80%D0%BE%D1%84%D0%B5%D1%81%D1%81%D0%B8%D0%B8)

Показать больше
Показать меньше

### Соцсети

* [Группа Google](https://groups.google.com/g/BlagoRussia)
* [Дзен](https://dzen.ru/blagorussia)

### ВКонтакте

### Одноклассники

### Нас просмотрело:

## Постоянные читатели

### [Сообщить о нарушении](https://www.blogger.com/go/report-abuse)

### Facebook

> [Общественное благополучие](https://www.facebook.com/blagorussia)
