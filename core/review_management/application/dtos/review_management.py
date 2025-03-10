from pydantic import BaseModel, Field
from typing import Generic
from datetime import datetime
from decimal import Decimal
import uuid

from core.utils.application.base_dto import BaseEntityDTO, DTO
from core.review_management.domain.value_objects.review_management import ReviewCollection
from core.review_management.domain.entities.review_management import Review as ReviewEntity
from core.review_management.domain.aggregates.review_management import ProductRating as ProductRatingEntity
from ...infrastructure.dtos.review_management import PaginatedReviewsDTO

class ReviewDTO(BaseEntityDTO):
    text: str
    rating: int
    date_created: datetime

    user: None = None

    uuid: uuid.UUID

    @staticmethod
    def from_entity(review: ReviewEntity) -> 'ReviewDTO':
        return ReviewDTO(
            uuid=review.public_uuid,
            text=review.text,
            rating=review.rating,
            date_created=review.date_created,
            user=None,
        )
    
    @staticmethod
    def from_entities(reviews: list[ReviewEntity]) -> list['ReviewDTO']:
        return [ReviewDTO.from_entity(review) for review in reviews]


class ReviewCollectionDTO(BaseModel, Generic[DTO]):
    reviews: list[ReviewDTO] = Field(default=list())
    current_page: int = Field(default=0)
    num_pages: int = Field(default=0)
    has_previous: bool = Field(default=False)
    has_next: bool = Field(default=False)
    total_count: int = Field(default=0)

    @staticmethod
    def from_paginated_data(paginated_reviews: PaginatedReviewsDTO) -> 'ReviewCollectionDTO':
        return ReviewCollectionDTO(
            reviews=ReviewDTO.from_entities(paginated_reviews.reviews),
            current_page=paginated_reviews.current_page,
            num_pages=paginated_reviews.num_pages,
            has_previous=paginated_reviews.has_previous,
            has_next=paginated_reviews.has_next,
            total_count=paginated_reviews.total_count,
        )

class ProductRatingDTO(BaseEntityDTO):
    rating: Decimal | None = Decimal("0.0")
    reviews: ReviewCollection[ReviewDTO] | list[ReviewDTO] | None
    product: uuid.UUID | None

    uuid: uuid.UUID | None

    @staticmethod
    def from_entity(product_rating: ProductRatingEntity | None, pagination: dict | None = None) -> 'ProductRatingDTO':
        # if not product_rating or product_rating.inner_uuid is None and product_rating.public_uuid is None:
        #     return None
        
        return ProductRatingDTO(
            rating=product_rating.rating,
            reviews=ReviewCollectionDTO.from_paginated_data(product_rating.reviews, pagination) if pagination else ReviewDTO.from_entities(product_rating.reviews),
            product=product_rating.product,
            uuid=product_rating.public_uuid,
        )