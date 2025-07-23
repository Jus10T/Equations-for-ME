import numpy as np

class Node:
    def __init__(self, index):
        self.index = index
        self.dofs = [2 * index, 2 * index + 1]  # vertical, rotation

class BeamElement:
    def __init__(self, index, node_start, node_end, EI, L):
        self.index = index
        self.node_start = node_start
        self.node_end = node_end
        self.EI = EI
        self.L = L

    def stiffness_matrix(self):
        L, EI = self.L, self.EI
        coeff = EI / L**3
        return coeff * np.array([
            [12,    6*L,   -12,   6*L],
            [6*L,  4*L**2, -6*L,  2*L**2],
            [-12,  -6*L,   12,  -6*L],
            [6*L,  2*L**2, -6*L,  4*L**2],
        ])

    def dof_map(self):
        return self.node_start.dofs + self.node_end.dofs

    def distributed_load_vector(self, w0, wL):
        L = self.L
        return (L / 20) * np.array([
            7*w0 + 3*wL,
            L*(3*w0 + 2*wL)/12,
            3*w0 + 7*wL,
            -L*(2*w0 + 3*wL)/12
        ])

class BeamModel:
    def __init__(self, length, num_elements, EI, units="SI"):
        self.length = length
        self.num_elements = num_elements
        self.EI = EI
        self.units = units
        self.nodes = [Node(i) for i in range(num_elements + 1)]
        self.elements = [
            BeamElement(i, self.nodes[i], self.nodes[i+1], EI, length / num_elements)
            for i in range(num_elements)
        ]
        self.supports = {}  # node_index: 'fixed'/'pinned'/'roller'
        self.point_loads = {}  # dof_index: load
        self.distributed_loads = {}  # element_index: (w0, wL)
        self.ndof = 2 * len(self.nodes)
        self.K = np.zeros((self.ndof, self.ndof))
        self.F = np.zeros(self.ndof)
        self.d = np.zeros(self.ndof)

    def add_support(self, node_index, support_type):
        self.supports[node_index] = support_type

    def add_point_load(self, node_index, value, moment=False):
        dof = 2 * node_index + (1 if moment else 0)
        self.point_loads[dof] = self.point_loads.get(dof, 0) + value

    def add_distributed_load(self, element_index, w0, wL):
        self.distributed_loads[element_index] = (w0, wL)

    def assemble(self):
        for elem in self.elements:
            k_local = elem.stiffness_matrix()
            dof_map = elem.dof_map()
            for i in range(4):
                for j in range(4):
                    self.K[dof_map[i], dof_map[j]] += k_local[i, j]

            if elem.index in self.distributed_loads:
                w0, wL = self.distributed_loads[elem.index]
                f_local = elem.distributed_load_vector(w0, wL)
                for i in range(4):
                    self.F[dof_map[i]] += f_local[i]

        for dof, load in self.point_loads.items():
            self.F[dof] += load

    def apply_boundary_conditions(self):
        self.prescribed_dofs = []
        for node_index, support in self.supports.items():
            if support in ['fixed', 'pinned', 'roller']:
                self.prescribed_dofs.append(2 * node_index)  # vertical
            if support == 'fixed':
                self.prescribed_dofs.append(2 * node_index + 1)  # rotation

        self.free_dofs = [i for i in range(self.ndof) if i not in self.prescribed_dofs]
        self.K_ff = self.K[np.ix_(self.free_dofs, self.free_dofs)]
        self.F_f = self.F[self.free_dofs]

    def solve(self):
        self.d[self.free_dofs] = np.linalg.solve(self.K_ff, self.F_f)
        self.reactions = self.K @ self.d - self.F

    def print_results(self):
        print("Nodal Displacements:")
        for i in range(len(self.nodes)):
            v = self.d[2*i]
            theta = self.d[2*i+1]
            print(f"Node {i}: v = {v:.6e}, θ = {theta:.6e}")
        print("\nSupport Reactions:")
        for i in self.prescribed_dofs:
            print(f"DOF {i}: R = {self.reactions[i]:.2f}")
