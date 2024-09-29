import pandas as pd
from sqlmodel import Session, create_engine

from app.core.config import settings
from app.services.rag.vectorstores import init_db_with_csv

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))

def init_db(session: Session) -> None:
    with Session(engine) as session:
        init_db_with_csv(settings.CSV_DATASET_PATH, session)