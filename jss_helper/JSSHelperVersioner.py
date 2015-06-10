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


import imp
import os

from autopkglib import Processor, ProcessorError


__all__ = ["JSSHelperVersioner"]



class JSSHelperVersioner(Processor):
    """Grab the jss_helper __version__."""
    input_variables = {
        "input_path": {
            "required": True,
            "description": "Path to jss_helper.",
        },
    }
    output_variables = {
        "version": {
            "description": "Version of jss_helper.",
        },
    }
    description = __doc__

    def main(self):
        with open(self.env["input_path"], "r") as jss_helper:
            for line in jss_helper:
                if line.startswith("__version__"):
                    version_line = line
                    break

        self.env["version"] = version_line.split("=")[1].strip("\"\n ")


if __name__ == "__main__":
    processor = JSSHelperVersioner()
    processor.execute_shell()
