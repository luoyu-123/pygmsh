from helpers import compute_volume

import pygmsh


def test():
    with pygmsh.built_in.Geometry() as geom:
        geom.add_circle(
            [0.0, 0.0, 0.0],
            1.0,
            mesh_size=0.1,
            num_sections=4,
            # If compound==False, the section borders have to be points of the
            # discretization. If using a compound circle, they don't; gmsh can
            # choose by itself where to point the circle points.
            compound=True,
        )
        mesh = pygmsh.generate_mesh(geom, prune_z_0=True)

    ref = 3.1363871677682247
    assert abs(compute_volume(mesh) - ref) < 1.0e-2 * ref
    return mesh


if __name__ == "__main__":
    test().write("circle.vtk")