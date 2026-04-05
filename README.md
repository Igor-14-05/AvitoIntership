# AvitoIntership


```bash
git clone https://github.com/Igor-14-05/AvitoIntership.git
cd ad-moderation-tests

# Установка
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install --with-deps chromium

# Запуск всех тестов
pytest -v --html=report.html --self-contained-html

# Только десктоп
pytest tests/desktop/ -v

# Только мобильная тема
pytest tests/mobile/ -v