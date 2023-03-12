from functools import wraps
from typing import List


def worker_builder(name=None):
    print(f"building {name}...")


def worker_updater(name=None):
    print(f"updating {name}...")


def field_changed(field_name, instance, updated_data):
    ret_val = False
    if field_name in updated_data:
        new_field_value = updated_data.get(field_name)
        ret_val = getattr(instance, field_name) != new_field_value
    return ret_val


def on_change(field_names: List[str], target):
    def worker_flag(func):
        @wraps(func)
        def drive_worker(*args, **kwargs):
            for field_name in field_names:
                if field_changed(field_name, *args[1:]):
                    target(field_name)
            return func(*args, **kwargs)
        return drive_worker
    return worker_flag
