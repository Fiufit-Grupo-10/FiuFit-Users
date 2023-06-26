import pytest
from starlette.testclient import TestClient
from app.api.training_types import models as training_models
from app.api.users import models as users_models
from app.api.admins import models as admins_models
from app.api.certificates import models as certificates_models
from app.config.database import Base
from app.dependencies import get_db

from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        # Base.metadata.create_all(bind=engine)
        yield db
    finally:
        db.close()


db = TestingSessionLocal()
db.add(
    training_models.TrainingType(
        name="Cardio", descr="Entrenamientos relacionados a la resistencia aerobica"
    )
)
db.add(
    training_models.TrainingType(
        name="Fuerza", descr="Entrenamientos relacionados a ganar fuerza"
    )
)
db.commit()
db.close()

app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client


@pytest.fixture(autouse=True, scope="function")
def cleanup():
    yield
    db = TestingSessionLocal()

    tables_to_clean = [
        admins_models.Admin,
        users_models.User,
        users_models.UserTrainingType,
        users_models.FollowingRelationship,
        certificates_models.Certificate,
    ]

    for table in tables_to_clean:
        db.query(table).delete()

    db.commit()
    db.close()
