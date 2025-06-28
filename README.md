# Telegram Bot for Render.com

## Как использовать

1. Скопируй `.env.example` в `.env` и вставь свой токен бота.
2. Установи зависимости:
   ```
   pip install -r requirements.txt
   ```
3. Запусти бота:
   ```
   python bot.py
   ```

## Для деплоя на [Render.com](https://render.com)

1. Залей этот репозиторий на GitHub.
2. Создай новый Web Service на Render.
3. Укажи **Start Command**: `python bot.py`
4. Добавь переменную окружения `TELEGRAM_TOKEN` в настройках Render.
