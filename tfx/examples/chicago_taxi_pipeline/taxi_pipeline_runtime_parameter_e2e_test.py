# Lint as: python2, python3
# Copyright 2019 Google LLC. All Rights Reserved.
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
"""End-to-end tests for tfx.examples.chicago_taxi_pipeline.taxi_pipeline_runtime_parameter."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import sys
import tensorflow as tf

from tfx.examples.chicago_taxi_pipeline import taxi_pipeline_runtime_parameter
from tfx.orchestration.kubeflow import test_utils


class TaxiPipelineRuntimeParameterEndToEndTest(test_utils.BaseKubeflowTest):

  def testEndToEndPipelineRun(self):
    """End-to-end test for pipeline with RuntimeParameter."""
    pipeline_name = 'kubeflow-e2e-test-parameter-{}'.format(self._random_id())
    pipeline = taxi_pipeline_runtime_parameter._create_parameterized_pipeline(
        pipeline_name=pipeline_name)

    parameters = {
        'pipeline-root': self._pipeline_root(pipeline_name),
        'module-file': self._taxi_module_file,
        'data-root': self._data_root,
        'train-steps': 10,
        'eval-steps': 5,
        'slicing-column': 'trip_start_hour',
    }

    self._compile_and_run_pipeline(pipeline, parameters)


if __name__ == '__main__':
  logging.basicConfig(stream=sys.stdout, level=logging.INFO)
  tf.test.main()
