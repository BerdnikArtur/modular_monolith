from abc import abstractmethod

from core.utils.domain.interfaces.i_repositories.base_repository import BaseRepository
from core.cart_management.domain.aggregates.cart_management import Wishlist as WishlistEntity
from core.cart_management.domain.entities.cart_management import Cart as CartEntity, WishlistItem as WishlistItemEntity

import uuid

class IWishlistRepository(BaseRepository):
    @abstractmethod
    def fetch_wishlist_by_user(self, public_uuid: uuid.UUID = None) -> WishlistEntity:
        pass

    @abstractmethod
    def save(self, wishlist: WishlistEntity = None, wishlist_items: list[WishlistItemEntity] = None) -> None:
        pass

class IWishlistItemRepository(BaseRepository):
    pass

class ICartRepository(BaseRepository):
    @abstractmethod
    def fetch_cart(self) -> CartEntity:
        pass

    @abstractmethod
    def save(self, cart_entity: CartEntity) -> None:
        pass
 
class ICartItemRepository(BaseRepository):
    pass