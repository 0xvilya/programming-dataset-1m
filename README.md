# Programming Dataset 1M

Синтетический датасет по программированию на **1 000 000** записей в формате JSONL.

## Структура записи

```json
{
  "id": 1,
  "language": "Python",
  "topic": "algorithms",
  "difficulty": "medium",
  "question": "Напиши функцию на Python, которая находит факториал числа.",
  "code_snippet": "def factorial(n):\n    return 1 if n <= 1 else n * factorial(n - 1)",
  "explanation": "Классическое рекурсивное решение...",
  "tags": ["python", "algorithms", "medium"]
}
```

## Файлы в репозитории

| Файл | Описание |
|------|----------|
| `generate_programming_dataset.py` | Генератор полного датасета (1 000 000 записей) |
| `dataset_50.jsonl` | Пример на 50 записей |
| `README.md` | Этот файл |

## Как сгенерировать полный датасет (1 000 000 записей)

```bash
python generate_programming_dataset.py
```

Скрипт создаст файл `programming_dataset_1m.jsonl` (~470 МБ).  
Генерация занимает примерно 1–2 минуты.

> **Почему не лежит полный файл на 1 000 000 записей?**  
> GitHub жёстко ограничивает размер одного файла **100 МБ**. Полный датасет весит ~470 МБ, поэтому в репозитории лежит генератор + небольшой пример. Ты можешь за 1–2 минуты создать полный файл у себя локально одной командой.

## Поля

- `id` — уникальный номер
- `language` — язык программирования
- `topic` — тема (algorithms, oop, web_development и т.д.)
- `difficulty` — easy / medium / hard
- `question` — формулировка задачи
- `code_snippet` — пример кода
- `explanation` — краткое пояснение
- `tags` — список тегов

## Лицензия

MIT (можно использовать свободно)
