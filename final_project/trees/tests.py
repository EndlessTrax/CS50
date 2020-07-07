from .models import Tree


def test_tree_creation(db):
    tree = Tree.objects.create(
        name="Old Juniper",
        species="Juniper",
        description="This is an old tree",
        location="VA",
        price=100,
        picture='../static/imgs/juniper-bonsai.jpg'
    )

    assert tree.name == "Old Juniper"
