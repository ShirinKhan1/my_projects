import variant1
import random
import variant3
import variant2

M = 6
N = 3
T1 = 1
T2 = 10
O_count = 3
vector = []
O = []
O_for_tour = []
best_copy = 20
p_cros = 0.99
p_mut = 0.2

for i in range(N):
    sub_b = []
    [sub_b.append(random.randint(T1, T2)) for _ in range(M)]
    vector.append(sub_b)


def create_O():
    O_new = [random.randint(0, int(255 / O_count))]
    # if v2:
    #     [O_new.append(random.randint(0, 255)) for _ in range(len(vector[0][1:]) - 1)]
    #     O_new.insert(0, O_v2)
    # else:
    [O_new.append(random.randint(0, 255)) for _ in range(len(vector[0][1:]))]
    O.append(O_new)


print(vector)
print(M,N)
O_v2 = variant2.main(vector, (M, N))
print(O_v2)
# O.clear()
[create_O() for _ in range(O_count-1)]
O.insert(0, O_v2)
# print(O)


# [create_O() for _ in range(O_count)]
variant1.main(O, vector, M, N, best_copy, p_cros, p_mut, O_count)
# variant3.main(O, vector, M, N, best_copy, p_cros, p_mut, O_count)
