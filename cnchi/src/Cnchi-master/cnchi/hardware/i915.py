#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  i915.py
#
#  Copyright © 2015 Apricity
#
#  This file is part of Cnchi.
#
#  Cnchi is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  Cnchi is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Cnchi; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

""" Intel driver installation """

from hardware.hardware import Hardware

import os

CLASS_NAME = "i915"
CLASS_ID = "0x0300"
VENDOR_ID = "0x8086"
DEVICES = []


class i915(Hardware):
    def __init__(self):
        Hardware.__init__(self)

    def get_packages(self):
        pkgs = ["xf86-video-intel", "libva-intel-driver", "libtxc_dxtn"]
        if os.uname()[-1] == "x86_64":
            pkgs.extend(["lib32-mesa", "lib32-mesa-libgl"])
        return pkgs

    def post_install(self, dest_dir):
        path = os.path.join(dest_dir, "etc/modprobe.d/i915.conf")
        with open(path, 'w') as modprobe:
            modprobe.write("options i915 modeset=1\n")

    def check_device(self, class_id, vendor_id, product_id):
        """ Checks if the driver supports this device """
        if class_id == CLASS_ID and vendor_id == VENDOR_ID:
            return True
        return False

    def get_name(self):
        return CLASS_NAME
