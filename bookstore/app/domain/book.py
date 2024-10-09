import datetime

from dataclasses import dataclass

# Простой датакласс с полями нашей центральной модели
@dataclass
class Book:
    title: str
    description: str
    publish_year: int
    pages_count: int
    created_at: datetime.datetime
