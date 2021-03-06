# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
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
# ==============================================================================
"""##Signal ops.

@@frame
@@hamming_window
@@hann_window
@@overlap_and_add
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow.contrib.signal.python.ops.reconstruction_ops import overlap_and_add
from tensorflow.contrib.signal.python.ops.shape_ops import frame
# `frame` used to be named `frames`, which is a noun and not a verb.
# Keep an alias to `frames` for backwards compatibility.
from tensorflow.contrib.signal.python.ops.shape_ops import frame as frames
from tensorflow.contrib.signal.python.ops.window_ops import hamming_window
from tensorflow.contrib.signal.python.ops.window_ops import hann_window

from tensorflow.python.util.all_util import remove_undocumented
remove_undocumented(__name__)
