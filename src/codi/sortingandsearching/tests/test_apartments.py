from codi.sortingandsearching.apartments import *


class TestApartments:
    def test_one_apartment_one_applicant(self):
        assert allocate(apartments=[30], applicants=[25], tolerance=5) == 1
        assert allocate(apartments=[30], applicants=[5], tolerance=5) == 0

    def test_zero_allocation(self):
        assert allocate(apartments=[30, 75], applicants=[45, 80], tolerance=1) == 0

    def test_case_1(self):
        apartments = [30, 60, 75]
        applicants = [60, 45, 80, 60]
        assert allocate(apartments, applicants, tolerance=5) == 2
        assert allocate(apartments, applicants, tolerance=0) == 1
        assert allocate(apartments, applicants, tolerance=15) == 3
