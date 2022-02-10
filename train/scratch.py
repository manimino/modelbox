from pydantic import BaseModel, validator, ValidationError


class Page(BaseModel):
    id: int
    start_utc: date
    characteristic: str

    @validator('start_utc')
    def date_is_recent(cls, v):
        assert v > date.today() - timedelta(days=1000)
        return v

    @validator('id')
    def id_is_positive(cls, v):
        assert v > 0


def json_to_Page(json: str):
    try:
        return Page(**json), ''
    except ValidationError as e:
        errstr = '' + str(e.errors())
        return None, errstr


def pages_to_np_array(pages: list[Page]):
    arr = pd.DataFrame(p.__dict__ for p in pages)[['characteristic', 'id']].values
    return arr

