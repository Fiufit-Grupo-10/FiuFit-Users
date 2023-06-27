from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError


def raise_integrity_error(
    e: IntegrityError,
    uid: int | None,
    username: str | None,
    email: str | None,
    type: str,
):
    if "uid" in str(e.orig.args):
        detail = f"{type} with uid: {uid} already exists"
    elif "username" in str(e.orig.args):
        detail = f"{type} with username: {username} already exists"
    else:
        detail = f"{type} with email: {email} already exists"
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=detail)
