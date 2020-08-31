from .constants import API_BASE_URL


def _endpoints_url(endpoint_path, base_url=API_BASE_URL):
    """Return full endpoint url."""
    return API_BASE_URL + endpoint_path


def _params_validation(
    bbox=None,
    distance=None,
    code_entite=None,
    cursor=None,
    date_debut_obs=None,
    date_fin_obs=None,
    fields=None,
    grandeur_hydro=None,
    latitude=None,
    longitude=None,
    size=None,
    sort=None,
    timestep=None,
    code_commune_site=None,
    code_cours_eau=None,
    code_departement=None,
    code_region=None,
    code_site=None,
    code_troncon_hydro_site=None,
    code_zone_hydro_site=None,
    format=None,
    libelle_cours_eau=None,
    libelle_site=None,
    page=None,
    code_commune_station=None,
    code_sandre_reseau_station=None,
    code_station=None,
    date_fermeture_station=None,
    date_ouverture_station=None,
    en_service=None,
    libelle_station=None
):
    """Validate parameters."""
    result = {}

    if bbox:
        result['bbox'] = bbox

    if distance:
        result['distance'] = distance

    if code_entite:
        result['code_entite'] = code_entite

    if cursor:
        result['cursor'] = cursor

    if date_debut_obs:
        result['date_debut_obs'] = date_debut_obs

    if date_fin_obs:
        result['date_fin_obs'] = date_fin_obs

    if fields:
        result['fields'] = fields

    if grandeur_hydro:
        result['grandeur_hydro'] = grandeur_hydro

    if latitude:
        result['latitude'] = latitude

    if longitude:
        result['longitude'] = longitude

    if size:
        result['size'] = size

    if sort:
        result['sort'] = sort

    if timestep:
        result['timestep'] = timestep

    if code_commune_site:
        result['code_commune_site'] = code_commune_site

    if code_cours_eau:
        result['code_cours_eau'] = code_cours_eau

    if code_departement:
        result['code_departement'] = code_departement

    if code_region:
        result['code_region'] = code_region

    if code_site:
        result['code_site'] = code_site

    if code_troncon_hydro_site:
        result['code_troncon_hydro_site'] = code_troncon_hydro_site

    if code_zone_hydro_site:
        result['code_zone_hydro_site'] = code_zone_hydro_site

    if format:
        result['format'] = format

    if libelle_cours_eau:
        result['libelle_cours_eau'] = libelle_cours_eau

    if libelle_site:
        result['libelle_site'] = libelle_site

    if page:
        result['page'] = page

    if code_commune_station:
        result['code_commune_station'] = code_commune_station

    if code_sandre_reseau_station:
        result['code_sandre_reseau_station'] = code_sandre_reseau_station

    if code_station:
        result['code_station'] = code_station

    if date_fermeture_station:
        result['date_fermeture_station'] = date_fermeture_station

    if date_ouverture_station:
        result['date_ouverture_station'] = date_ouverture_station

    if en_service:
        result['en_service'] = en_service

    if libelle_station:
        result['libelle_station'] = libelle_station

    return result
