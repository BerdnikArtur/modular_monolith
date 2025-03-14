from ...application.dtos.user_management import UserDTO
from ..entities.user_management import User as UserEntity

from abc import ABC, abstractmethod
import uuid

class IUserACL(ABC):
    @abstractmethod
    def fetch_by_uuid(self, inner_uuid: uuid.UUID = None, public_uuid: uuid.UUID = None) -> UserDTO:
        pass

    @abstractmethod
    def guest(self) -> UserEntity:
        pass