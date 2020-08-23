class A:
    def __init__(self):
        print("This is class A")
        super().__init__()


class B(A):
    def __init__(self):
        print("This is class B")
        super().__init__()


class C:
    def __init__(self):
        print("This is class C")
        super().__init__()


class MRO_Order1(B, C):
    def __init__(self):
        print("This is class MRO_Order1")
        super().__init__()


class MRO_Order2(C, B):
    def __init__(self):
        print("This is class MRO_Order2")
        super().__init__()


if __name__ == "__main__":

    mroOrder1 = MRO_Order1()
    """
    Output: 
    This is class MRO_Order1
    This is class B
    This is class A
    This is class C
    """

    mroOrder2 = MRO_Order2()
    """
    Outputs:
    This is class MRO_Order2
    This is class C
    This is class B
    This is class A
    """
