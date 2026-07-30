from unittest.mock import patch, MagicMock

from app.main import check_server, load_servers


def test_check_server_up():
    mock_response = MagicMock(status_code=200)
    with patch("app.main.requests.get", return_value=mock_response):
        assert check_server("example.com") == "example.com: UP (200)"


def test_check_server_down():
    with patch("app.main.requests.get", side_effect=Exception("boom")):
        assert check_server("example.com") == "example.com: DOWN"


def test_load_servers(tmp_path):
    servers_file = tmp_path / "servers.json"
    servers_file.write_text('{"servers": ["a.com", "b.com"]}')

    assert load_servers(str(servers_file)) == ["a.com", "b.com"]
