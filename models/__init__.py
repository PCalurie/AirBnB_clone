#!/usr/bin/python3
"""Initializes the package with serialized data
and reloads it in the application memory"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
