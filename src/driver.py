import contextlib
from pathlib import Path

from libcloud.storage.drivers.local import LocalStorageDriver
from libcloud.storage.types import ContainerAlreadyExistsError
from sqlalchemy_file.storage import StorageManager

root = Path("upload")
root.mkdir(0o777, exist_ok=True)
upload_driver = LocalStorageDriver(root)

with contextlib.suppress(ContainerAlreadyExistsError):
    upload_driver.create_container(container_name="default")

with contextlib.suppress(ContainerAlreadyExistsError):
    upload_driver.create_container(container_name="user-avatar")

with contextlib.suppress(ContainerAlreadyExistsError):
    upload_driver.create_container(container_name="job-attachments")


for container in upload_driver.list_containers():
    StorageManager.add_storage(
        name=container.name,
        container=container,
    )


StorageManager.set_default("default")
