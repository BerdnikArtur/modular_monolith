from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from core.shop_management.domain.entities.shop_management import ProductSize, ProductImage

from core.utils.domain.value_objects.common import BaseEntityCollection


MIN_SIZES = 0
MAX_SIZES = 5
MIN_IMAGES = 0
MAX_IMAGES = 10


class ProductSizesCollection(BaseEntityCollection['ProductSize']):
    def __post_init__(self):
        self.validate_length(min_length=MIN_SIZES, max_length=MAX_SIZES)

    def validate_length(self, min_length: int, max_length: Optional[int] = None) -> None:
        if len(self._entities) < min_length:
            raise ValueError(f"{self.__class__.__name__}  contains fewer than {min_length} entities.")
        if max_length is not None and len(self._entities) > max_length:
            raise ValueError(f"{self.__class__.__name__}  contains more than {max_length} entities.")


class ProductImagesCollection(BaseEntityCollection['ProductImage']):
    def __post_init__(self):
        self.validate_length(min_length=MIN_IMAGES, max_length=MAX_IMAGES)

    def validate_length(self, min_length: int, max_length: Optional[int] = None) -> None:
        if len(self._entities) < min_length:
            raise ValueError(f"{self.__class__.__name__} contains fewer than {min_length} entities.")
        if max_length is not None and len(self._entities) > max_length:
            raise ValueError(f"{self.__class__.__name__} contains more than {max_length} entities.")