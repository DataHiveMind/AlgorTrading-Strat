def helloworld() -> str:
    return "Hello World"

def getNasDaqData(api_key: str, data: str) -> pd.DataFrame:
    """
    Parameters
    ---------- 
    api_key = String

    data = String

    Returns
    -------
    Data = pd.DataFrame

    """
    import nasdaqdatalink
    nasdaqdatalink.ApiConfig.api_key = api_key
    return nasdaqdatalink.get(data)