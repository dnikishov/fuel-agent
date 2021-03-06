# Copyright 2014 Mirantis, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from fuel_agent.objects.bootloader import Grub
from fuel_agent.objects.configdrive import ConfigDriveCommon
from fuel_agent.objects.configdrive import ConfigDriveMcollective
from fuel_agent.objects.configdrive import ConfigDrivePuppet
from fuel_agent.objects.configdrive import ConfigDriveScheme
from fuel_agent.objects.device import Loop
from fuel_agent.objects.image import Image
from fuel_agent.objects.image import ImageScheme
from fuel_agent.objects.operating_system import Centos
from fuel_agent.objects.operating_system import OperatingSystem
from fuel_agent.objects.operating_system import Ubuntu
from fuel_agent.objects.partition.fs import FileSystem
from fuel_agent.objects.partition.lv import LogicalVolume
from fuel_agent.objects.partition.md import MultipleDevice
from fuel_agent.objects.partition.parted import Parted
from fuel_agent.objects.partition.parted import Partition
from fuel_agent.objects.partition.pv import PhysicalVolume
from fuel_agent.objects.partition.scheme import PartitionScheme
from fuel_agent.objects.partition.vg import VolumeGroup
from fuel_agent.objects.repo import DEBRepo
from fuel_agent.objects.repo import Repo
from fuel_agent.objects.repo import RepoProxies


PV = PhysicalVolume
VG = VolumeGroup
LV = LogicalVolume
MD = MultipleDevice
FS = FileSystem


__all__ = [
    'Partition',
    'Parted',
    'PhysicalVolume',
    'PV',
    'VolumeGroup',
    'VG',
    'LogicalVolume',
    'LV',
    'MultipleDevice',
    'MD',
    'FileSystem',
    'FS',
    'PartitionScheme',
    'ConfigDriveCommon',
    'ConfigDrivePuppet',
    'ConfigDriveMcollective',
    'ConfigDriveScheme',
    'Image',
    'ImageScheme',
    'Grub',
    'OperatingSystem',
    'Ubuntu',
    'Centos',
    'Repo',
    'DEBRepo',
    'Loop',
    'RepoProxies'
]
