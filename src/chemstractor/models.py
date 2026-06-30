from typing import Literal, get_args, Union

pricing_matrix = {
    "gemini-2.5-flash": {
        "input_per_m": 0.30,   # $0.30 per 1M tokens
        "output_per_m": 2.50    # $2.50 per 1M tokens
    },
    "gemini-2.5-pro": {
        "input_per_m": 1.25,    # $1.25 per 1M tokens
        "output_per_m": 10.00   # $10.00 per 1M tokens
    },
    "gemini-3.5-flash": {
        "input_per_m": 1.50,    # $12.50 per 1M tokens
        "output_per_m": 9.00   # $60.00 per 1M tokens
    },
    "gemini-3.1-flash-lite": {
        "input_per_m": 0.25,    # $0.25 per 1M tokens
        "output_per_m": 1.50   # $1.50 per 1M tokens
    }
}

OnlineModels = Literal["gemini-2.5-flash", "gemini-2.5-pro", "gemini-3.5-flash"]
OfflineModels = Literal["llama3.1"]
AllSupportedModels = Union[OnlineModels, OfflineModels]

ONLINE_MODELS = list(pricing_matrix.keys())
OFFLINE_MODELS = list(get_args(OfflineModels))
