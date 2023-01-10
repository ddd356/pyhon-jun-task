# type Fields = [Field]
# data Field = Field Name Type
# type Name = String
# data Type = Email | Phone | Date | Text
# type Request = [(Name, Value)]
# type Value = String

# result :: Request -> [Form]
# result = Fi2Fo . Req2Fo

# Fi2Fo :: Fields -> [Form]

# (Request -> Fields) -> [Form]

# Req2Fi:: Request -> Fields
# Req2Fi = map validator

# validator :: (Name, Value) -> Field
# validator :: (n, v)
#   | isDate = Field n Date
#   | isPhone = Field n Phone
#   | isEmail = Field n Email
#   | otherwise = Field n Text

import datetime
import re
import json
from tinydb import Query, TinyDB
from email_validator import validate_email, EmailNotValidError
from flask import Flask, request
from copy import deepcopy

# settings
dbname = 'db.json'

app = Flask(__name__)

@app.route("/", methods=['POST'])
def form_template():
    return result(request.get_json().items())

def result(request):
    db = TinyDB(dbname)
    fields = Req2Fi(request)
    forms = Fi2Fo(fields, db)
    if forms:
        return json.dumps(forms)
    else:
        return dict(fields)

def Fi2Fo(p_fields, db):

    res = []
    Q = Query()
    fields = deepcopy(p_fields)

    if not fields:
        return res

    
    for f in fields:
        f_name, f_type = f
        other_fields = fields
        other_fields.pop(0)
        if not other_fields:
            return res
        for of in other_fields:
            of_name, of_type = of
            res += db.search((Q[f_name] == f_type) & (Q[of_name] == of_type))

        res += (Fi2Fo(other_fields, db))

    return res

def Req2Fi(request):
    # rf: request field
    return list(map(lambda rf: validator(rf[0], rf[1]), request))

def validator(name, value):
    if isDate(value):
        return (name, "date")
    elif isPhone(value):
        return (name, "phone")
    elif isEmail(value):
        return (name, "email")
    else:
        return (name, "text")

def isDate(val):
    formatStrings = ['%Y-%m-%d', '%d.%m.%Y']
    return any([isDateFormat(val, fs) for fs in formatStrings])

def isDateFormat(val, formatString):
    try:
        if val != datetime.datetime.strptime(val, formatString).strftime(formatString):
            raise ValueError
        return True
    except ValueError:
        return False

def isPhone(val):
    pattern = re.compile('^\+7 [0-9]{3} [0-9]{3} [0-9]{2} [0-9]{2}')
    return re.fullmatch(pattern, val)

def isEmail(val):
    try:
        v = validate_email(val)
        email = v.email
        return True
    except EmailNotValidError:
        return False
