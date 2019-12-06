#!/usr/bin/env python
#
# Copyright 2014 Shea G. Craig
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import absolute_import

import glob
import os
import re

from autopkglib import Processor, ProcessorError

__all__ = ["CowsaySourceFinder"]



class CowsaySourceFinder(Processor):
    """Finds the root schacon-cowsay-foo folder from the expanded
    zip archive, and determines the version, setting the env variable. Also,
    sets the %PREFIX% variable where needed.

    """
    input_variables = {
        "input_path": {
            "required": True,
            "description": "Path the zip archive was expanded to.",
        },
    }
    output_variables = {
        "cowsay_path": {
            "description": "Root path of expanded cowsay archive.",
        },
        "version": {
            "description": "The version of the software.",
        },
    }
    description = __doc__

    def find_match(self, root_dir, match_string):
        """Finds a file or directory using shell globbing"""
        matches = glob.glob(os.path.join(root_dir, match_string))
        if matches:
            return matches[0][len(root_dir) + 1:]
        else:
            return ""

    def find_version(self, filename):
        """Grabs the version from the cowsay perl file."""

        with open(filename, 'r') as f:
            match = re.search(r'\$version = "([0-9.]+)', f.read())
        self.env["version"] = match.group(1)

    def replace_text(self, filename, replacement_code, replacement):
        with open(filename, 'r') as f:
            cowsay_text = f.read()
        cowsay_replaced_text = cowsay_text.replace(replacement_code,
                                                   replacement)
        with open(filename, 'w') as f:
            f.write(cowsay_replaced_text)

    def main(self):
        # Get root dir
        root_dir = self.env["input_path"]
        try:
            autopkg_dir = self.find_match(
                root_dir, 'schacon-cowsay-*')
            self.env["cowsay_path"] = os.path.join(
                root_dir, autopkg_dir)
            self.output(self.env["cowsay_path"])
            self.output("autopkg_dir %s" % autopkg_dir)
            cowsay_file = os.path.join(self.env['cowsay_path'], 'cowsay')

            self.find_version(cowsay_file)
            self.replace_text(cowsay_file, '%BANGPERL%', '!/usr/bin/perl')
            self.output("Set perl shebang.")
            self.replace_text(cowsay_file, '%PREFIX%', '/usr/local')
            self.output("Set cows folder default.")
            self.output("Found %s" % self.env["cowsay_path"])
            self.output("Found version is %s" % self.env["version"])
        except Exception as err:
            raise ProcessorError(err)


if __name__ == "__main__":
    processor = CowsaySourceFinder()
    processor.execute_shell()
