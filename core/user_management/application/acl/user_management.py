from ...infrastructure.repositories.user_management import DjangoUserRepository
from ..dtos.user_management import UserDTO
from ...domain.interfaces.i_acls import IUserACL

import uuid

class UserACL(IUserACL):
    def __init__(self, user_repository: DjangoUserRepository):
        self.user_rep = user_repository

    def fetch_by_uuid(self, inner_uuid: uuid.UUID = None, public_uuid: uuid.UUID = None) -> UserDTO:
        return UserDTO.from_entity(self.user_rep.find_by_uuid(inner_uuid=inner_uuid, public_uuid=public_uuid))