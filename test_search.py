import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging

BASE_URL = 'http://127.0.0.1:5000'

#настройка логиров.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler('test_search.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger()

@pytest.fixture(scope="class")
def auth_session():
    session = requests.Session()

    response = session.post(
         f"{BASE_URL}/auth",
        auth=HTTPBasicAuth('test_user', 'test_pass')
    )

    logger.info(f"Auth response status: {response.status_code}")
    assert response.status_code == 200

    access_token = response.json()['access_token']

    session.headers.update({
        'Authorization': f'Bearer {access_token}'
    })
    return session
class TestSearch:

    @pytest.mark.parametrize("sort_by,limit",[
        ("price", 20),
        ("year", 3),
        ("engine_volume", 10),
        ("brand", 7),
        (None, 5),
        ("price", None),
    ])
    def test_search(self, auth_session, sort_by, limit):

        params = {}

        if sort_by:
            params['sort_by'] = sort_by
        if limit:
            params['limit'] = limit

        logger.info(f"Testing with params: {params}")

        response = auth_session.get(f"{BASE_URL}/cars", params=params)

        logger.info(f"Response status: {response.status_code}")
        assert response.status_code == 200

        data = response.json()

        logger.info(f"Response data length: {len(data)}")
        assert isinstance(data, list)

        if limit:
            assert len(data) <= limit

        if sort_by and data:
            values = [car[sort_by] for car in data]
            assert values == sorted(values)
