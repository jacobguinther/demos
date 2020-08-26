import pandas as pd

sys_params = {
    'fee_numerator': [997],
    'fee_denominator': [1000],
    'uniswap_events': [pd.read_pickle('~/Documents/uniswap/uniswap_events.pickle')],
    'c_rule': [3],
    'conv_tolerance': [0.05]
}