#!/bin/bash
python3 app.py & # 后端
python3 -m http.server # 前端
