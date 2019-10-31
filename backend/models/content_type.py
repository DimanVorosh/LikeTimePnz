from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import String, BigInteger, Boolean
from models.meta import Base


class ContentType(Base):
    __tablename__ = "content_type"

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    name = Column(String)
    color = Column(String(7))
    active = Column(Boolean(), default=True, nullable=False)

    deleted = Column(Boolean(), default=False, nullable=False)

    @staticmethod
    def get_by_id(id):
        return ContentType.query.filter(
            ContentType.id == id,
            ContentType.deleted.is_(False)
        ).one_or_none()
