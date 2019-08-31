#!/usr/bin/env python
#
# Copyright 2015 Shea G. Craig
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
import re

from autopkglib import Processor, ProcessorError


__all__ = ["NetHackVersioner"]



class NetHackVersioner(Processor):
    """Finds the version strings in the NetHack binary."""
    input_variables = {
        "input_path": {
            "required": True,
            "description": "Path the zip archive was expanded to.",
        },
    }
    output_variables = {
        "version": {
            "description": "Version of NetHack.",
        },
    }
    description = __doc__

    def main(self):
        with open(self.env["input_path"], "rb") as nethack:
            nethack_data = nethack.read()

        regex = re.compile("MacOSX NetHack Version ([\d+\.]{3,})")
        found = re.search(regex, nethack_data)
        if found:
            self.env["version"] = found.group(1)
            self.output("Found version %s" % self.env["version"])
        else:
            self.env["version"] = "0.0.0"
            self.output("No version found!")
        # except BaseException as err:
        #     raise ProcessorError(err)


if __name__ == "__main__":
    processor = NetHackVersioner()
    processor.execute_shell()
