import json
from pathlib import Path


class SettingsManager:
    _settings = {}

    _settings_path = (
        Path(__file__).parent / "settings.json"
    )

    DEFAULT_SETTINGS = {
        "language": "en",
        "theme": "dark",

        "window": {
            "width": 1600,
            "height": 900,
            "fullscreen": False
        },

        "animation": {
            "speed": 40,
            "smooth": True
        },

        "array": {
            "size": 60
        },

        "interface": {
            "show_legend": True,
            "show_statistics": True,
            "show_algorithm_info": True,
            "show_step_explanation": True,
            "show_console": True
        },

        "sound": {
            "enabled": False
        }
    }

    @classmethod
    def load(cls):
        if not cls._settings_path.exists():
            cls._settings = json.loads(
                json.dumps(cls.DEFAULT_SETTINGS)
            )
            cls.save()
            return

        try:
            with open(
                cls._settings_path,
                "r",
                encoding="utf-8"
            ) as file:
                cls._settings = json.load(file)

        except Exception:
            cls._settings = json.loads(
                json.dumps(cls.DEFAULT_SETTINGS)
            )
            cls.save()

    @classmethod
    def save(cls):
        with open(
            cls._settings_path,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                cls._settings,
                file,
                indent=4,
                ensure_ascii=False
            )

    @classmethod
    def get(cls, key, default=None):
        value = cls._settings

        for part in key.split("."):
            if not isinstance(value, dict):
                return default

            if part not in value:
                return default

            value = value[part]

        return value

    @classmethod
    def set(cls, key, value):
        parts = key.split(".")
        data = cls._settings

        for part in parts[:-1]:
            if part not in data:
                data[part] = {}

            data = data[part]

        data[parts[-1]] = value

    @classmethod
    def reset(cls):
        cls._settings = json.loads(
            json.dumps(cls.DEFAULT_SETTINGS)
        )
        cls.save()