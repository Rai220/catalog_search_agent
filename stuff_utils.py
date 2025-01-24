from typing import List, Literal

from pydantic import BaseModel, Field

class StuffDesc(BaseModel):
    """Описание товара"""

    stuff_id: str = Field(description="Идентификатор товара", default=None)
    desc: str = Field(description="Описание товара", default=None)
    brand: str = Field(description="Торговая марка", default=None)
    price: float = Field(description="Цена (руб.)", default=None)
    min_store_temperature: int = Field(description="Минимальная температура хранения", default=None)
    max_store_temperature: int = Field(description="Максимальная температура хранения", default=None)
    shelf_life: int = Field(description="Срок годности (мес.)", default=None)
    type_of_packing: Literal[
        "n/a",
        "пластиковая бутылка",
        "стеклянная бутылка",
        "пакет",
        "железная банка",
        "алюминиевая банка",
        "коробка",
        "другое",
    ] = Field(description="Тип упаковки", default=None)
    mass_fraction_of_fat_min: float = Field(description="Массовая доля жира (мин.)", default=None)
    mass_fraction_of_fat_max: float = Field(description="Массовая доля жира (макс.)", default=None)
