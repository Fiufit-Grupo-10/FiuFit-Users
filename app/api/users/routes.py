from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.api.users import crud, schemas
from app.api.users.utils import raise_integrity_error
from app.dependencies import get_db
from app.api.users import services
from sqlalchemy.exc import IntegrityError
from app.config.config import logger

router = APIRouter(tags=["users"])


@router.post(
    "/users", response_model=schemas.UserReturn, status_code=status.HTTP_201_CREATED
)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    logger.info("Post User Request", uid=user.uid)
    try:
        return crud.create_user(db=db, user=user)
    except IntegrityError as e:
        logger.info(
            "Post User Request Failed: integrity error",
            uid=user.uid,
            email=user.email,
            username=user.username,
        )
        raise_integrity_error(
            e, uid=user.uid, username=user.username, email=user.email, type="User"
        )
    except Exception:
        logger.info("Training Type Not found", uid=user.uid)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="TrainingType not found"
        )


@router.put(
    "/users/{user_id}",
    response_model=schemas.UserReturn,
    status_code=status.HTTP_200_OK,
)
def update_user(user: schemas.UserRequest, user_id: str, db: Session = Depends(get_db)):
    logger.info("Put User Request", uid=user_id)
    if crud.get_user(db=db, user_id=user_id) is None:
        logger.info("User Not found", uid=user_id)
        detail = f"User {user_id} not found"
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
    try:
        logger.info("Updating user", uid=user_id)
        return crud.update_user(db=db, user=user, uid=user_id)
    except IntegrityError as e:
        logger.info(
            "Put User Request Failed: integrity error",
            uid=user_id,
            email=user.email,
            username=user.username,
        )
        raise_integrity_error(
            e, uid=user_id, username=user.username, email=user.email, type="User"
        )
    except Exception:
        logger.info("Training Type Not found", uid=user_id)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="TrainingType not found"
        )


@router.patch(
    "/users", response_model=list[schemas.UserReturn], status_code=status.HTTP_200_OK
)
def update_users_block(users: list[schemas.UserBlock], db: Session = Depends(get_db)):
    logger.info("Block/Unblock User Request")
    return crud.update_user_block(users=users, db=db)


@router.get(
    "/users/{user_id}",
    response_model=schemas.UserReturn,
    status_code=status.HTTP_200_OK,
)
def get_user(user_id: str, db: Session = Depends(get_db)):
    logger.info("Get User Request", uid=user_id)
    user = crud.get_user(db=db, user_id=user_id)
    if user is None:
        logger.info("User Not found", uid=user_id)
        detail = f"User {user_id} not found"
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
    return user


@router.get(
    "/users", response_model=list[schemas.UserReturn], status_code=status.HTTP_200_OK
)
def get_users(
    username: str | None = None,
    admin: bool = True,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    logger.info(
        "Get Users Request", admin=admin, username=username, skip=skip, limit=limit
    )
    if admin:
        return crud.get_users(db=db, skip=skip, limit=limit)

    if username is None:
        users = crud.get_users(db=db, skip=skip, limit=limit)
    else:
        users = crud.get_users_by_username(
            db=db, skip=skip, limit=limit, username=username
        )

    users = jsonable_encoder(
        users,
        include={
            "uid",
            "username",
            "birthday",
            "user_type",
            "image_url",
            "gender",
            "email",
            "token",
            "certified",
        },
    )
    return JSONResponse(content=users, status_code=status.HTTP_200_OK)


@router.post(
    "/users/{user_id}/followers/{follower_id}",
    response_model=schemas.FollowerReturn,
    status_code=status.HTTP_201_CREATED,
)
def add_user_follower(user_id: str, follower_id: str, db: Session = Depends(get_db)):
    logger.info("Add user follower request", uid=user_id, follower_id=follower_id)
    user = crud.get_user(db=db, user_id=user_id)
    if user is None:
        logger.info("User Not found", uid=user_id)
        detail = f"User {user_id} not found"
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
    follower = crud.get_user(db=db, user_id=follower_id)
    if follower is None:
        logger.info("Follower Not found", follower_id=follower_id)
        detail = f"Follower {follower_id} not found"
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
    followerreturn = jsonable_encoder(
        crud.add_user_follower(db=db, followed_uid=user_id, follower_uid=follower_id)
    )
    return JSONResponse(content=followerreturn, status_code=status.HTTP_201_CREATED)


@router.delete(
    "/users/{user_id}/followers/{follower_id}", status_code=status.HTTP_200_OK
)
def delete_user_follower(user_id: str, follower_id: str, db: Session = Depends(get_db)):
    logger.info("Delete user follower request", uid=user_id, follower_id=follower_id)
    crud.delete_user_follower(followed_uid=user_id, follower_uid=follower_id, db=db)
    return JSONResponse(content=None, status_code=status.HTTP_200_OK)


@router.get(
    "/users/{user_id}/followers",
    response_model=list[str],
    status_code=status.HTTP_200_OK,
)
def get_users_followers(user_id: str, db: Session = Depends(get_db)):
    logger.info("Get user followers request", uid=user_id)
    user = crud.get_user(db=db, user_id=user_id)
    if user is None:
        logger.info("User Not found", uid=user_id)
        detail = f"User {user_id} not found"
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
    followers = crud.get_users_followers(db=db, uid=user_id)
    followers = [follower.follower_uid for follower in followers]
    followers = jsonable_encoder(followers)
    return JSONResponse(content=followers, status_code=status.HTTP_200_OK)


@router.get(
    "/users/{user_id}/following",
    response_model=list[str],
    status_code=status.HTTP_200_OK,
)
def get_users_following(user_id: str, db: Session = Depends(get_db)):
    logger.info("Get user following request", uid=user_id)
    user = crud.get_user(db=db, user_id=user_id)
    if user is None:
        logger.info("User Not found", uid=user_id)
        detail = f"User {user_id} not found"
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
    following = crud.get_users_following(db=db, uid=user_id)
    following = [follower.followed_uid for follower in following]
    following = jsonable_encoder(following)
    return JSONResponse(content=following, status_code=status.HTTP_200_OK)


@router.get(
    "/users/{user_id}/trainers",
    response_model=list[schemas.UserReturn],
    status_code=status.HTTP_200_OK,
)
def filter_trainers_by_distance(
    user_id: str, distance: float, db: Session = Depends(get_db)
):
    logger.info("Filter trainers by distance", uid=user_id)
    user = crud.get_user(db=db, user_id=user_id)
    if user is None:
        logger.info("User Not found", uid=user_id)
        detail = f"User {user_id} not found"
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
    logger.info("Reaching trainers by distance", uid=user_id)
    trainers = services.filter_trainers_by_distance(user=user, distance=distance, db=db)
    return trainers
