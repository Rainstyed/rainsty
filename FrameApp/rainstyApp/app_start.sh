#!/bin/bash

gunicorn -w 1 manage_app:app -b 0.0.0.0:5000 --timeout 1800
