#!/usr/bin/env python
#
# Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
# except in compliance with the License. A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "LICENSE.txt" file accompanying this file. This file is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, express or implied. See the License for
# the specific language governing permissions and limitations under the License.

import argparse
import sys
import logging
from tensorrt_llm_toolkit import create_model_repo
from utils import load_properties
import logging

def create_trt_llm_repo(properties, model_path):
    model_id_or_path = model_path or properties['option.model_id']
    kwargs = {}
    for key, value in properties.items():
        if key.startswith("option."):
            kwargs[key[7:]] = value
        else:
            kwargs[key] = value
    create_model_repo(model_id_or_path, **kwargs)

def main():
    logging.basicConfig(stream=sys.stdout,
                        format="%(message)s",
                        level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--properties_dir',
        type=str,
        required=True,
        help='path of the model directory containing properties file')
    parser.add_argument(
        '--model_path',
        type=str,
        required=False,
        default=None,
        help='local path to downloaded model'
    )

    args = parser.parse_args()
    properties = load_properties(args.properties_dir)
    create_trt_llm_repo(properties, args.model_path)

if __name__ == "__main__":
    main()
