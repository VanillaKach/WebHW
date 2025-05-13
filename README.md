# WebHW
Веб-приложение с Bootstrap и Flask
Это простое веб-приложение, созданное в рамках учебного задания, которое демонстрирует:

Верстку страниц с использованием Bootstrap

Базовую работу с Flask

Обработку GET и POST запросов

Структура проекта
project/
├── templates/
│   ├── contacts.html  # Страница "Контакты"
│   ├── home.html      # Главная страница
│   └── menu.html      # Страница меню
├── app.py             # Основное Flask-приложение
├── requirements.txt   # Зависимости
└── README.md          # Этот файл
Функциональность
Основные возможности:
На любые GET-запросы возвращается страница "Контакты"

Поддержка POST-запросов с выводом полученных данных в консоль

Три готовых шаблона страниц:

Контакты

Главная страница интернет-магазина

Меню

Особенности реализации:
Использование Bootstrap 5 для стилизации

Адаптивный дизайн

Простая структура для удобства изучения

Установка и запуск
Клонируйте репозиторий:

bash
git clone <адрес репозитория>
cd <папка проекта>
Создайте и активируйте виртуальное окружение:

bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Установите зависимости:

bash
pip install -r requirements.txt
Запустите приложение:

bash
python app.py
Откройте в браузере:

http://localhost:5000
Тестирование POST-запросов
Вы можете протестировать обработку POST-запросов с помощью:

cURL:

bash
curl -X POST -d "test=data&example=123" http://localhost:5000
Или создав HTML-форму:

html
<form action="http://localhost:5000" method="POST">
  <input type="text" name="field1">
  <input type="text" name="field2">
  <button type="submit">Отправить</button>
</form>
Технологии
Python 3

Flask

Bootstrap 5

HTML5
