from core.utils.application.base_dto import BaseDTO
from core.cart_management.domain.aggregates.cart_management import Cart as CartEntity, CartItem as CartItemEntity, Wishlist as WishlistEntity, WishlistItem as WishlistItemEntity
from core.utils.domain.value_objects.common import ForeignUUID

from pydantic import Field
import uuid

class BaseItemDTO(BaseDTO):
    pub_uuid: uuid.UUID = Field(default=None)
    color: str = Field(default='Black')
    qty: int = Field(default=0)

    size: uuid.UUID = Field(default=None)
    size_snapshot: dict = Field(default=None)

class CartItemDTO(BaseItemDTO):
    @staticmethod
    def from_entity(entity: CartItemEntity) -> 'CartItemDTO':
        return CartItemDTO(
            color=entity.color,
            qty=entity.qty,
            size=entity.size.public_uuid,
            size_snapshot=entity.size_snapshot,
        )

class WishlistItemDTO(BaseItemDTO):
    @staticmethod
    def from_entity(entity: WishlistItemEntity) -> 'WishlistItemDTO':
        return WishlistItemDTO(
            color=entity.color,
            qty=entity.qty,
            size=entity.size.public_uuid,
            size_snapshot=entity.size_snapshot,
        )

class BaseItemCollectionDTO(BaseDTO):
    pub_uuid: uuid.UUID = Field(default=None)
    total_price: int = Field(default=0)
    quantity: int = Field(default=0)

    items: list[CartItemDTO] = Field(default_factory=list)

    user: uuid.UUID | ForeignUUID = Field(default=None)


class CartDTO(BaseItemCollectionDTO):
    @staticmethod
    def from_entity(entity: CartEntity) -> 'CartDTO':
        return CartDTO(
            total_price=entity.total_price,
            quantity=entity.quantity,
            items=[CartItemDTO.from_entity(item) for item in entity.items] if entity.items else [],
            user=entity.user.public_uuid,
            pub_uuid=entity.public_uuid,
        )
    

class WishlistDTO(BaseItemCollectionDTO):
    @staticmethod
    def from_entity(entity: WishlistEntity) -> 'WishlistDTO':
        return WishlistDTO(
            total_price=entity.total_price,
            quantity=entity.quantity,
            items=[WishlistItemDTO.from_entity(item) for item in entity.items] if entity.items else [],
            user=entity.user.public_uuid,
            pub_uuid=entity.public_uuid,
        )