
def test_get_create_update_delete_author_endpoints(test_client, author):
    """
        Тест на создание автора, получение,
            получение списка авторов, обновление и удаление
    """
    response = test_client.post("/authors", json=author)
    assert response.status_code == 201

    response = test_client.get('/authors')
    response_json = response.json()
    assert response.status_code == 200
    assert len(response_json) == 1
    assert response_json[0]['first_name'] == author['first_name']
    assert response_json[0]['last_name'] == author['last_name']

    response = test_client.get('/authors/1')
    response_json = response.json()
    assert response.status_code == 200
    assert response_json['first_name'] == author['first_name']
    assert response_json['last_name'] == author['last_name']

    author['last_name'] = 'Roronoa'
    response = test_client.put('/authors/1', json=author)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json['last_name'] == author['last_name']

    response = test_client.delete('/authors/1')
    assert response.status_code == 204


def test_get_author_by_id_endpoint_404_error(test_client, author):
    """
        Тесты на получение автора по id, ошибка
    """
    response = test_client.get('/authors/1')
    assert response.status_code == 404

