# Copyright (c) 2020  PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"
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

import paddle
from onnxbase import APIOnnx


class Net(paddle.nn.Layer):
    """
    simplr Net
    """

    def __init__(self):
        super(Net, self).__init__()

    def forward(self, inputs, inputs_):
        """
        forward
        """
        x = paddle.matmul(inputs, inputs_, transpose_x=False, transpose_y=True)
        return x


def test_matmul_9():
    """
    api: paddle.matmul
    op version: 9
    """
    op = Net()
    op.eval()
    # func, name, input_shape, ver_list, delta=1e-6, rtol=1e-5
    obj = APIOnnx(op, 'add', [3, 10], [9], binputs=True)
    obj.run()


def test_matmul_10():
    """
    api: paddle.matmul
    op version: 10
    """
    op = Net()
    op.eval()
    # func, name, input_shape, ver_list, delta=1e-6, rtol=1e-5
    obj = APIOnnx(op, 'add', [3, 10], [10], binputs=True)
    obj.run()


def test_matmul_11():
    """
    api: paddle.matmul
    op version: 11
    """
    op = Net()
    op.eval()
    # func, name, input_shape, ver_list, delta=1e-6, rtol=1e-5
    obj = APIOnnx(op, 'add', [3, 10], [11], binputs=True)
    obj.run()


def test_matmul_12():
    """
    api: paddle.matmul
    op version: 12
    """
    op = Net()
    op.eval()
    # func, name, input_shape, ver_list, delta=1e-6, rtol=1e-5
    obj = APIOnnx(op, 'add', [3, 10], [12], binputs=True)
    obj.run()
