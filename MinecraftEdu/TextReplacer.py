#!/usr/bin/python
#
# Copyright 2014 Shea G. Craig
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#	  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import absolute_import
from autopkglib import Processor, ProcessorError


__all__ = ["TextReplacer"]


class TextReplacer(Processor):
    description = "Replaces text in a file."
    input_variables = {
        "source_path": {
            "required": True,
            "description": "Path to a file to perform string replacement on."
        },
        "replacement_marker": {
            "required": False,
            "description": "String to use as replacement marker. Defaults to" \
                   " %REPLACE%",
            "default": "%REPLACE%"
        },
        "replacement_text": {
            "required": True,
            "description": "Text to replace into file."
        },
    }
    output_variables = {
    }

    __doc__ = description

    def main(self):
        with open(self.env['source_path'], 'r+') as replacement_file:
            self.output(self.env['source_path'])
            input_string = replacement_file.read()

        output_string = input_string.replace(self.env['replacement_marker'],
                                             self.env['replacement_text'])

        with open(self.env['source_path'], 'w') as replacement_file:
            replacement_file.write(output_string)


if __name__ == '__main__':
	processor = TextReplacer()
	processor.execute_shell()
