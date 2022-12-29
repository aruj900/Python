from fastapi import APIRouter,Depends,status,Response,HTTPException
from typing import List
from .. import schemas, database,models,oauth2
from sqlalchemy.orm import Session

router= APIRouter(
    tags=['Blogs'],
    prefix='/blog'
)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create_blog(request:schemas.Blog,db: Session = Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    new_blog = models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db: Session = Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(id,request:schemas.Blog,db: Session = Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available")
    blog.update({"title": request.title, "body": request.body})
    db.commit()
    return 'updated'

@router.get('/',response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog,)
def show(id,response: Response, db: Session = Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with the id {id} is not available"}
    return blog 