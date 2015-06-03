from main import generate_population

def _generated_population():
    n_p = 100
    n_d = 2
    l = 0
    u = 1
    points = generate_population(n_p, n_d, l, u)
    assert(len(points) == 100), "Length wrong"
    for point in points:
        assert(len(point) == 2), "Dimension wrong"
        for d in point:
            assert(l<=d<=u), "Ranges wrong"
    print "Test _generated_population() passed"


if __name__ == "__main__":
    _generated_population()