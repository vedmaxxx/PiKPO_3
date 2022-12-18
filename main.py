# Подключаем приложение Flask из пакета labapp
from labapp import app

"""
Этот файл запускает приложение
"""

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
