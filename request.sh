#!/bin/bash

# mail and text
curl --request POST --header 'Content-Type: application/json' --data '{"fname1": "mail@site.com", "fname2":"some text"}' 'http://127.0.0.1:5000'
echo ''

# phone and date
curl --request POST --header 'Content-Type: application/json' --data '{"field11": "+7 999 999 99 99", "field12":"01.01.2023"}' 'http://127.0.0.1:5000'
echo ''

# missing template
curl --request POST --header 'Content-Type: application/json' --data '{"impossible_field_name1": "bad@mail.com", "impossible_field_name2":"something mystical"}' 'http://127.0.0.1:5000'
