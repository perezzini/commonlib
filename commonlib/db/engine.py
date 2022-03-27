from sqlalchemy.future import Engine
from sqlmodel import Session, SQLModel, create_engine, select


def create_engine_(path: str, echo: bool) -> Engine:
    """Create DB engine

    Args:
        path (str): Conn
        echo (bool): Whether to print logs (must be False in prod)

    Returns:
        Engine: A DB engine
    """
    return create_engine(path, echo=echo)


def create_db_and_tables(engine: Engine) -> None:
    """Create tables from specified models

    Args:
        engine (Engine): A DB engine
    """
    SQLModel.metadata.create_all(engine)


def default_check(session: Session) -> bool:
    """Default health check against DB

    Args:
        session (Session): A DB session

    Returns:
        bool: Query result
    """
    stmt = select(1)

    return bool(session.exec(stmt))
