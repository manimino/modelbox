import numpy as np
import pandas as pd

from datetime import date, timedelta


def predict(model, page: Page):
    pd.DataFrame(page_df)
    model.predict(page_df)


def predictMany(model, pages:pd.DataFrame):
    return model.predict(pages)

if __name__ == '__main__':
    js = {'id': 0, 'start_utc': date.today() - timedelta(days=99999), 'characteristic': 'baige'}
    p, errs = json_to_Page(js)
    if not p:
