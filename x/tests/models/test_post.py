import pytest

from x_blog.factories import PostFactory

@pytest.fixture
def post_publised():
    return PostFactory(title='pytest with factory')

@pytest.mark.django_db
def test_create_published_post(post_publised):
    assert post_publised.title == 'pytest with factory'