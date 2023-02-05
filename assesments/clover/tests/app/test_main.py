from unittest.mock import patch

from app.main import main


@patch("app.repository.Repository.save")
def test_main(save):
    main()
