from comment.models import Comment
from photos.models import Photos
from django.contrib.auth.models import User


def create_user_test1():
    # create user_1 for test
    user_1 = create_test_user('test1', 'test1', 'lastname-test1')
    photo_1 = create_test_photo(user_1, '/url/test1/')
    comment_1 = create_test_comment(photo_1, 'good!!')

def create_user_test2():
    #create user_2 for test
    user_2 = create_test_user('test2', 'test2', 'lastname-test2')
    photo_2 = create_test_photo(user_2, '/url/test2/')
    comment_2 = create_test_comment(photo_2, 'good good!!')

def create_test_user(username, firstname, lastname):
    user = User(username=username, first_name=firstname, last_name=lastname)
    user.save()
    return user


def create_test_photo(user, url):    
    photo = Photos(user=user, url=url)
    photo.save()
    return photo


def create_test_comment(photo, comment):
    comment = Comment(photo=photo, comment=comment)
    comment.save()
    return comment
