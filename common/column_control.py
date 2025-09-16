class ColumnSelector:
    # ホワイトリスト
    ALLOWED_COLUMNS = {
        "date_set": "date_set"
    }

    @classmethod
    def get_column(cls, key: str) -> str:
        if key not in cls.ALLOWED_COLUMNS:
            raise ValueError(f"不正なカラム名: {key}")
        return cls.ALLOWED_COLUMNS[key]
