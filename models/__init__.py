""" Init module
    This module sets all need requirements for model usage
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()