import json
import logging

from .commons import GrandeurHydro, _params_validation
from .constants import API_ENDPOINT_HYDRO_OBSERVATION_TR, API_ENDPOINT_HYDRO_SITES, API_ENDPOINT_HYDRO_STATIONS
from .rest_client import HubeauRestApi

log = logging.getLogger(__name__)


class HydrometryApi(HubeauRestApi):

    def get_observations_tr(self, bbox=None, distance=None, code_entite=None, cursor=None,
                            date_debut_obs=None, date_fin_obs=None, fields=None, grandeur_hydro=GrandeurHydro.H.value,
                            latitude=None, longitude=None, size=None, sort=None, timestep=None
                            ):

        params = _params_validation(
            bbox=bbox,
            distance=distance,
            code_entite=code_entite,
            cursor=cursor,
            date_debut_obs=date_debut_obs,
            date_fin_obs=date_fin_obs,
            fields=fields,
            grandeur_hydro=grandeur_hydro,
            latitude=latitude,
            longitude=longitude,
            size=size,
            sort=sort,
            timestep=timestep
        )

        data = self.get(path=API_ENDPOINT_HYDRO_OBSERVATION_TR, params=params)
        return json.loads(data)

    def get_sites(self, bbox=None, code_commune_site=None, code_cours_eau=None, code_departement=None,
                  code_region=None, code_site=None, code_troncon_hydro_site=None, code_zone_hydro_site=None,
                  distance=None, fields=None, format=None, latitude=None, libelle_cours_eau=None,
                  libelle_site=None, longitude=None, page=None
                  ):

        params = _params_validation(
            bbox=bbox,
            code_commune_site=code_commune_site,
            code_cours_eau=code_cours_eau,
            code_departement=code_departement,
            code_region=code_region,
            code_site=code_site,
            code_troncon_hydro_site=code_troncon_hydro_site,
            code_zone_hydro_site=code_zone_hydro_site,
            distance=distance,
            fields=fields,
            format=format,
            latitude=latitude,
            libelle_cours_eau=libelle_cours_eau,
            libelle_site=libelle_site,
            longitude=longitude,
            page=page
        )

        data = self.get(path=API_ENDPOINT_HYDRO_SITES, params=params)
        return json.loads(data)

    def get_stations(self, bbox=None, code_commune_station=None, code_cours_eau=None, code_departement=None,
                     code_region=None, code_sandre_reseau_station=None, code_site=None, code_station=None,
                     date_fermeture_station=None, date_ouverture_station=None, distance=None,
                     en_service=True, fields=None, format=None, libelle_cours_eau=None, libelle_site=None,
                     libelle_station=None, latitude=None, longitude=None, page=None, size=None
                     ):

        params = _params_validation(
            bbox=bbox,
            code_commune_station=code_commune_station,
            code_cours_eau=code_cours_eau,
            code_departement=code_departement,
            code_region=code_region,
            code_sandre_reseau_station=code_sandre_reseau_station,
            code_site=code_site,
            code_station=code_station,
            date_fermeture_station=date_fermeture_station,
            date_ouverture_station=date_ouverture_station,
            distance=distance,
            en_service=en_service,
            fields=fields,
            format=format,
            libelle_cours_eau=libelle_cours_eau,
            libelle_site=libelle_site,
            libelle_station=libelle_station,
            latitude=latitude,
            longitude=longitude,
            page=page,
            size=size
        )

        data = self.get(path=API_ENDPOINT_HYDRO_STATIONS, params=params)
        return json.loads(data)
