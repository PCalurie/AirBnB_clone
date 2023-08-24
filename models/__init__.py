#!/usr/bin/python3
"""method initializer for models directory"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
