from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.api.users import crud, schemas
from app.dependencies import get_db


router = APIRouter(tags=["users"])


@router.post("/users", response_model=schemas.UserReturn, status_code=201)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@router.post(
    "/users/{user_id}/followers", response_model=schemas.FollowerReturn, status_code=201
)
def add_user_follower(
    user_id: str, follower: schemas.Follower, db: Session = Depends(get_db)
):
    followerreturn = jsonable_encoder(
        crud.add_user_follower(db=db, followed_uid=user_id, follower=follower)
    )
    return JSONResponse(content=followerreturn, status_code=201)


@router.get("/users/{user_id}/followers", response_model=list[str], status_code=200)
def get_users_followers(user_id: str, db: Session = Depends(get_db)):
    followers = crud.get_users_followers(db=db, uid=user_id)
    followers = [follower.follower_uid for follower in followers]
    followers = jsonable_encoder(followers)
    return JSONResponse(content=followers, status_code=200)


@router.get("/users/{user_id}/following", response_model=list[str], status_code=200)
def get_users_following(user_id: str, db: Session = Depends(get_db)):
    following = crud.get_users_following(db=db, uid=user_id)
    following = [follower.followed_uid for follower in following]
    following = jsonable_encoder(following)
    return JSONResponse(content=following, status_code=200)


@router.put("/users/{user_id}", response_model=schemas.UserReturn)
def update_user(user: schemas.UserRequest, user_id: str, db: Session = Depends(get_db)):
    if crud.get_user(db=db, user_id=user_id) is None:
        detail = f"User {user_id} not found"
        raise HTTPException(status_code=404, detail=detail)
    return crud.update_user(db=db, user=user, uid=user_id)


@router.get("/users/{user_id}", response_model=schemas.UserReturn)
def get_user(user_id: str, db: Session = Depends(get_db)):
    user = crud.get_user(db=db, user_id=user_id)
    if user is None:
        detail = f"User {user_id} not found"
        raise HTTPException(status_code=404, detail=detail)
    return user


@router.get("/users", response_model=list[schemas.UserReturn])
def get_users(
    username: str = None,
    admin: bool = True,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    if admin:
        return crud.get_users(db=db, skip=skip, limit=limit)

    if not username:
        users = crud.get_users(db=db, skip=skip, limit=limit)
    else:
        users = crud.get_users_by_username(
            db=db, skip=skip, limit=limit, username=username
        )

    users = jsonable_encoder(
        users, include={"username", "birthday", "user_type", "image_url"}
    )
    return JSONResponse(content=users, status_code=200)
