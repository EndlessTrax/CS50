from .models import CustomUser, Transaction


def test_user_creation(db):
    user = CustomUser.objects.create_user(
        username="testuser",
        password="nottelling",
        display_name="Test User"
    )

    assert user.username == "testuser"
    assert user.check_password("nottelling")
    assert user.display_name == "Test User"