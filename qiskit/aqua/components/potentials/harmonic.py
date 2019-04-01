# -*- coding: utf-8 -*-

# Copyright 2018 IBM.
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
# =============================================================================
"""
This module contains the definition of a base class for potentials.
"""


from abc import abstractmethod

from qiskit import QuantumCircuit, QuantumRegister

from qiskit.aqua import Pluggable, AquaError
import numpy as np

from . import Potential

class Harmonic(Potential):

    """Base class for iHarmonic Potentials: 1/2 m w^2 (x0+delta*x)^2

        This method should initialize the module and its configuration, and
        use an exception if a component of the module is
        available.

        Args:
            configuration (dict): configuration dictionary
    """

    @abstractmethod
    def __init__(self, num_qubits, m, omega, x0, delta):
        super().__init__()
        self._num_qubits = num_qubits
        self._m = m
        self._omega = omega
        self._x0 = x0
        self._delta = delta

    # @classmethod
    # def init_params(cls, num_qubits, m, omega, x0, delta):
    #     cls._num_qubits = num_qubits
    #     cls._m = m
    #     cls._omega = omega
    #     cls._x0 = x0
    #     cls._delta = delta

    @abstractmethod
    def construct_circuit(self, mode, register=None):
        """
        Construct a circuit to apply a harmonic potential on the statevector.

        Args:

        Returns:

        Raises:
        """

        if mode=='matrix':

            circ = np.zeros((1<<self._num_qubits,1<<self._num_qubits))
            c = np.sqrt(2 * np.pi / (self._num_qubits)) * 0.5
            for i in range(1<<self._num_qubits):
                circ[i,i]=(c*(self._x0 + i*self._delta))**2


        elif mode=='circuit':
            q = QuantumRegister(self._num_qubits, name='q')
            circ = QuantumCircuit(q)

            for i in range(self._num_qubits):
                circ.u1(self._x0, q[i])
                circ.x(q[i])
                circ.u1(self._x0, q[i])
                circ.x(q[i])
                circ.u1()







        raise NotImplementedError()