# Эмоциональная окраска текста на корейском языке

Приложение использует модель KR-FinBert-SC для анализа эмоциональной окраски текста на корейском языке.

## API

### `GET /`

Возвращает приветственное сообщение.

### `POST /predict/`

Принимает текст на корейском языке и возвращает эмоциональную окраску текста (positive, neutral или negative).

### `GET /emotions/`

Возвращает список всех эмоций, поддерживаемых моделью.