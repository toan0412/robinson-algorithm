from sympy import Or, to_cnf, Not, Implies
from itertools import combinations

# Nhập các biểu thức từ bàn phím
def input_expressions():
    expressions = []
    while True:
        expr_str = input("Nhập biểu thức ( &, |, Implies(->), nhập 'q' để kết thúc: ")
        if expr_str.lower() == 'q':
            break
        expressions.append(to_cnf(expr_str))
    conclude_str = input("Nhập kết luận: ")
    expressions.append(Not(to_cnf(conclude_str)))
    return expressions

def main():
    array = input_expressions()
    print('Mảng biểu thức: P = Q =', array)

    # Thực hiện kiểm tra và tạo biểu thức mới
    while True:
        if not is_proved(array):
            if not create_new_new_expression(array):
                print("Kết luận bị bác bỏ.")
                break
        else:
            print("Bài toán được chứng minh.")
            break

# Kiểm tra xem có cặp biến đối ngẫu không
def is_proved(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == ~array[j]:
                print("Bài toán được chứng minh bởi các mệnh đề:", array[i], "và", array[j])
                return True

    print("Không tìm thấy 2 mệnh đề nào đối ngẫu, thực hiện tạo biểu thức mới")
    return False

# Tạo biểu thức mới từ các cặp biến đối ngẫu
def create_new_new_expression(array):
    pairs = combinations(array, 2)

    for pair in list(pairs):
        for i in pair[0].args:
            for j in pair[1].args:
                if i == ~j:
                    print(pair[0], ' và', pair[1], 'có biến đối ngẫu là:', i)
                    new_args = [arg for arg in (pair[0].args + pair[1].args) if arg != i and arg != ~i]
                    new_expression = Or(*new_args)
                    print('Ta có biểu thức mới là: ', new_expression)
                    array.append(new_expression)
                    print('P = ', array)
    print('Không tạo được biểu thức mới')
    return False  # Không tạo được biểu thức mới, trả về False

if __name__ == "__main__":
    main()
