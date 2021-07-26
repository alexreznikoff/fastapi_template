import sqlalchemy as sa

metadata = sa.MetaData()

STRING_LENGTH = 255

USER_TABLE_NAME = "user"


user_table = sa.Table(
    USER_TABLE_NAME,
    metadata,
    sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
    sa.Column("name", sa.String(STRING_LENGTH), nullable=False),
)
