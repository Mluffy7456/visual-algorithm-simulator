import json
from pathlib import Path

from config.settings_manager import SettingsManager


class LanguageManager:
    _translations = {}
    _current_language = "en"

    _languages_path = (
        Path(__file__).parent / "languages"
    )

    @classmethod
    def load(cls):
        """Загружает язык из настроек."""

        language = SettingsManager.get(
            "language",
            "en"
        )

        cls.set_language(language)

    @classmethod
    def set_language(cls, language):
        """Устанавливает текущий язык."""

        path = cls._languages_path / f"{language}.json"

        if not path.exists():
            path = cls._languages_path / "en.json"
            language = "en"

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:
            cls._translations = json.load(file)

        cls._current_language = language

        SettingsManager.set(
            "language",
            language
        )

        SettingsManager.save()

    @classmethod
    def get(cls, key):
        """Возвращает перевод по ключу."""

        return cls._translations.get(key, key)

    @classmethod
    def current_language(cls):
        """Текущий язык."""

        return cls._current_language


def tr(key):
    return LanguageManager.get(key)