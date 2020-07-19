import pytest
from .models import Tree
from users.models import CustomUser


def test_tree_creation(db):
    user = CustomUser.objects.create_user(
        username="testuser", 
        password="nottelling", 
        display_name="Test User"
    )
    tree = Tree.objects.create(
        name="Old Juniper",
        species="Juniper",
        description="This is an old tree",
        location="VA",
        price=100,
        picture='../static/imgs/juniper-bonsai.jpg',
        owner_id=user
    )

    assert tree.name == "Old Juniper"
    assert tree.owner_id.username == "testuser"


def test_edit_a_tree(db):
    user = CustomUser.objects.create_user(
        username="testuser", 
        password="nottelling", 
        display_name="Test User"
    )
    tree = Tree.objects.create(
        name="Old Juniper",
        species="Juniper",
        description="This is an old tree",
        location="VA",
        price=100,
        picture='../static/imgs/juniper-bonsai.jpg',
        owner_id=user

    )

    tree.price = 200
    tree.description = "Its not that old, actually."

    assert tree.price == 200
    assert tree.description != "This is an old tree"
