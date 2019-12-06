#!/usr/bin/env python
#
# Copyright 2014 Shea Craig
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

import urllib2

from autopkglib import Processor, ProcessorError

__all__ = ["GeogebraURLProvider"] 


BASE_URL = "http://www.geogebra.org/download/?os=mac"

class GeogebraURLProvider(Processor):
    """Provides a download URL for the latest Geogebra release."""
    input_variables = {
        "base_url": {
            "required": False,
            "description": "Default is %s" % BASE_URL,
        },
    }
    output_variables = {
        "url": {
            "description": "URL to the latest Geogebra release.",
        },
    }
    description = __doc__


    def get_geogebra_dmg_url(self, base_url):
        # Read HTML index.
        try:
            f = urllib2.urlopen(base_url)
            html = f.geturl()
            f.close()
        except Exception as err:
            raise ProcessorError("Can't download %s: %s" % (base_url, err))
        
        return urllib2.quote(f.geturl(), safe=":/%")
        

    def main(self):
        """Find and return a download URL"""
        base_url = self.env.get("base_url", BASE_URL)
        self.env["url"] = self.get_geogebra_dmg_url(base_url)
        self.output("Found URL %s" % self.env["url"])


if __name__ == "__main__":
    processor = GeogebraURLProvider()
    processor.execute_shell()
