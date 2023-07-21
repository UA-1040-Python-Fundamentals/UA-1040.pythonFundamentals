the_zen_of_python = """Гарне краще за потворне.
Очевидне краще за неочевидне.
Просте краще за складне.
Складне краще за заплутане.
Плоске краще за вкладене.
Розділене є кращим за щільне.
Легкість читання має значення.
Особливі випадки не є настільки особливими, щоб порушувати правила.
Хоча практичність є важливішою за бездоганність.
Помилки ніколи не повинні бути замовчуваними.
Хіба що замовчуваними відверто.
Зустрівши двозначність, відкиньмо спокусу вгадати.
Має бути один — і, бажано, тільки один — очевидний спосіб зробити це.
Хоча спочатку він може бути й не очевидним, якщо ви не голландець.
Зараз — краще, ніж ніколи.
Хоча ніколи, найчастіше, — краще, ніж просто зараз.
Якщо реалізацію важко пояснити — задум поганий.
Якщо реалізацію легко пояснити — можливо, задум добрий.
Простори імен — чудова річ, тож робімо їх більше! """

краще = the_zen_of_python.count("краще")
ніколи = the_zen_of_python.count("ніколи")
є = the_zen_of_python.count("є")
print(краще)
print(ніколи)
print(є)

перетворення = the_zen_of_python.upper()
print(перетворення)

the_zen_of_python_replace = the_zen_of_python.replace("і" , "&")
print(the_zen_of_python_replace)

