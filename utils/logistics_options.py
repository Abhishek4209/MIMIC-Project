from src.logger import logging
from src.exception import CustomException
import os
import sys
import numpy as np
import pandas as pd
from dataclasses import dataclass




@dataclass
class Options(object):
    try:
        logging.info('Options class is Starting here')
        chart_events_v_not_nan = True
        apply_scaler = False
        scaler_type = "MinMax"    # MinMax, Standard
    except Exception as e:
        raise CustomException(e,sys)
        logging.info("Some Exception occured into Logistics Option Class is arrived...")