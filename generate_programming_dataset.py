#!/usr/bin/env python3
"""
Генератор синтетического датасета по программированию.
Формат: JSONL (один JSON-объект на строку).

Запуск:
    python generate_programming_dataset.py

Результат:
    programming_dataset_1m.jsonl  (~470 МБ)
"""

import json
import random
from pathlib import Path

# ====================== НАСТРОЙКИ ======================
TOTAL_RECORDS = 1_000_000
OUTPUT_FILE = "programming_dataset_1m.jsonl"
SEED = 42

# ====================== ДАННЫЕ ======================
LANGUAGES = [
    "Python", "JavaScript", "TypeScript", "Java", "C++", "C#",
    "Go", "Rust", "Kotlin", "Swift", "PHP", "Ruby", "Scala", "Dart",
]

TOPICS = [
    "algorithms", "data_structures", "oop", "functional_programming",
    "web_development", "api_design", "databases", "concurrency",
    "testing", "design_patterns", "system_design", "networking",
    "security", "performance", "debugging", "refactoring",
]

DIFFICULTIES = ["easy", "medium", "hard"]

QUESTION_TEMPLATES = [
    "Напиши функцию на {lang}, которая {task}.",
    "Реализуй на языке {lang}: {task}.",
    "Как правильно реализовать на {lang}: {task}?",
    "Напиши пример кода на {lang} для задачи: {task}.",
    "Объясни и покажи код на {lang}: {task}.",
    "Сделай на {lang} с использованием лучших практик: {task}.",
    "Напиши unit-тест на {lang} для функции, которая {task}.",
    "Оптимизируй на {lang} следующий подход: {task}.",
]

TASKS = [
    "находит факториал числа",
    "проверяет, является ли строка палиндромом",
    "сортирует массив чисел",
    "находит максимальный элемент в списке",
    "реализует бинарный поиск",
    "считает количество гласных в строке",
    "переворачивает связанный список",
    "проверяет сбалансированность скобок",
    "находит НОД двух чисел",
    "генерирует последовательность Фибоначчи",
    "удаляет дубликаты из списка",
    "реализует очередь на двух стеках",
    "проверяет, является ли число простым",
    "считает сумму цифр числа",
    "находит пересечение двух массивов",
    "реализует простой кэш LRU",
    "парсит JSON-строку вручную",
    "проверяет валидность email",
    "считает частоту слов в тексте",
    "реализует простой HTTP-клиент",
    "находит все анаграммы слова",
    "сортирует список словарей по ключу",
    "реализует декоратор для логирования",
    "проверяет наличие цикла в связанном списке",
    "считает глубину бинарного дерева",
]

CODE_SNIPPETS = {
    "Python": [
        "def factorial(n):\n    return 1 if n <= 1 else n * factorial(n - 1)",
        "def is_palindrome(s):\n    return s == s[::-1]",
        "def binary_search(arr, target):\n    left, right = 0, len(arr) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1",
        "from collections import Counter\ndef word_freq(text):\n    return Counter(text.split())",
    ],
    "JavaScript": [
        "function factorial(n) {\n  return n <= 1 ? 1 : n * factorial(n - 1);\n}",
        "const isPalindrome = s => s === s.split('').reverse().join('');",
        "function binarySearch(arr, target) {\n  let left = 0, right = arr.length - 1;\n  while (left <= right) {\n    const mid = Math.floor((left + right) / 2);\n    if (arr[mid] === target) return mid;\n    if (arr[mid] < target) left = mid + 1;\n    else right = mid - 1;\n  }\n  return -1;\n}",
    ],
    "Go": [
        "func factorial(n int) int {\n    if n <= 1 {\n        return 1\n    }\n    return n * factorial(n-1)\n}",
        "func isPalindrome(s string) bool {\n    runes := []rune(s)\n    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {\n        if runes[i] != runes[j] {\n            return false\n        }\n    }\n    return true\n}",
    ],
    "Rust": [
        "fn factorial(n: u64) -> u64 {\n    match n {\n        0 | 1 => 1,\n        _ => n * factorial(n - 1),\n    }\n}",
        "fn is_palindrome(s: &str) -> bool {\n    s.chars().eq(s.chars().rev())\n}",
    ],
}

DEFAULT_SNIPPET = "// implement me\nfunction example() {\n  // TODO\n}"

EXPLANATIONS = [
    "Классическое рекурсивное решение. Для больших n лучше использовать итеративный подход или мемоизацию.",
    "Простое и читаемое решение. В production-коде стоит добавить проверку входных данных.",
    "Эффективный алгоритм с временной сложностью O(log n).",
    "Использует стандартную библиотеку языка для чистоты и скорости.",
    "Решение следует принципам чистого кода и SOLID.",
    "Хороший пример для изучения рекурсии и базовых структур данных.",
    "Оптимизировано по памяти и времени. Подходит для интервью.",
    "Демонстрирует идиоматичный стиль выбранного языка.",
]


def get_code_snippet(lang: str) -> str:
    snippets = CODE_SNIPPETS.get(lang)
    if snippets:
        return random.choice(snippets)
    return DEFAULT_SNIPPET


def generate_record(idx: int) -> dict:
    lang = random.choice(LANGUAGES)
    topic = random.choice(TOPICS)
    difficulty = random.choice(DIFFICULTIES)
    task = random.choice(TASKS)
    template = random.choice(QUESTION_TEMPLATES)

    question = template.format(lang=lang, task=task)
    code = get_code_snippet(lang)
    explanation = random.choice(EXPLANATIONS)

    return {
        "id": idx,
        "language": lang,
        "topic": topic,
        "difficulty": difficulty,
        "question": question,
        "code_snippet": code,
        "explanation": explanation,
        "tags": [lang.lower(), topic, difficulty],
    }


def main() -> None:
    random.seed(SEED)
    output_path = Path(OUTPUT_FILE)

    print(f"Генерирую {TOTAL_RECORDS:,} записей → {output_path}")
    print("Это займёт 1–3 минуты...")

    with output_path.open("w", encoding="utf-8") as f:
        for i in range(1, TOTAL_RECORDS + 1):
            record = generate_record(i)
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

            if i % 100_000 == 0:
                print(f"  готово {i:,} записей")

    size_mb = output_path.stat().st_size / 1024 / 1024
    print(f"\nГотово!")
    print(f"Файл: {output_path.resolve()}")
    print(f"Размер: {size_mb:.1f} МБ")
    print(f"Записей: {TOTAL_RECORDS:,}")


if __name__ == "__main__":
    main()
