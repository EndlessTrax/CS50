from .models import CustomUser, Transaction
from .forms import CustomUserChangeForm


def test_user_creation(db):
    user = CustomUser.objects.create_user(
        username="testuser", password="nottelling", display_name="Test User"
    )

    assert user.username == "testuser"
    assert user.check_password("nottelling")
    assert user.display_name == "Test User"


def test_transaction_creation(db):
    transaction = Transaction.objects.create(user_id=1, tree_id=1, sold=True)

    assert transaction.tree_id == 1
    assert transaction.sold == True
