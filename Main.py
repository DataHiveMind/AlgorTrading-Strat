import pandas as pd
import datetime as dt
from openbb_terminal.sdk import openbb
import nasdaqdatalink

nasdaqdatalink.ApiConfig.api_key = "1KZewE_bhxyQ79dWDXba"

data = nasdaqdatalink.get("CHRIS/CME_ES1")
print(data)

import func as f
f.getNasDaqData()

