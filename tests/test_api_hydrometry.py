import unittest

from api.hydrometry import HydrometryApi


class TestApiHydrometry(unittest.TestCase):
    def test_get_observations_tr_by_code_entite_should_return_data(self):
        code_station = 'V294201001'
        client = HydrometryApi()
        data = client.get_observations_tr(code_entite=code_station)

        assert data['count'] > 0
        assert data['data'][0]['code_station'] == code_station

    def test_get_observations_tr_by_invalid_code_entite_should_return_zero_data(self):
        code_station = 'this_is_a_test'
        client = HydrometryApi()
        data = client.get_observations_tr(code_entite=code_station)

        assert data['count'] == 0
        assert len(data['data']) == 0

    def test_get_sites_by_libelle_cours_eau_should_return_data(self):
        libelle_cours_eau = 'Ain'
        client = HydrometryApi()
        data = client.get_sites(libelle_cours_eau=libelle_cours_eau)

        assert data['count'] > 0
        assert len(data['data']) > 0

    def test_get_stations_by_libelle_cours_eau_should_return_data(self):
        libelle_cours_eau = 'Ain'
        client = HydrometryApi()
        data = client.get_stations(libelle_cours_eau=libelle_cours_eau)

        assert data['count'] > 0
        assert len(data['data']) > 0


if __name__ == "__main__":
    unittest.main()
