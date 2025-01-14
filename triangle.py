import unittest

def area(a, h): 
    """
     Вычисляет площадь треугольника
     
     Параметр a - Сторона треугольника
     Параметр h - Высота треугольника к стороне a
     
     Возвравщает площадь треугольника
    """
    return a * h / 2 

def perimeter(a, b, c): 
    """
     Вычисляет периметр треугольника
     
     Параметр a - сторона 1 треугольника
     Параметр b - сторона 2 треугольника 
     Параметр c - сторона 3 треугольника 
     
     Возвравщает периметр треугольника
    """
    return a + b + c 


class TriangleCalculationsTestCase(unittest.TestCase):

    """
    Класс для тестирования функций расчета площади и периметра треугольника.

    Методы класса тестируют функции area и perimeter на соответствие математическим
    расчетам для различных входных значений.
    """

    def test_area(self):
        """
        Тестирование функции area.

        Проверяет, что функция верно вычисляет площадь треугольника.
        В данном тесте используется сторона 10 и высота 5. 
        Ожидаемый результат - площадь треугольника, равная 25.
        """
        self.assertEqual(area(10, 5), 25)

    def test_perimeter(self):
        """
        Тестирование функции perimeter.

        Проверяет, что функция верно вычисляет периметр треугольника.
        В данном тесте используются стороны 10 15 20. 
        Ожидаемый результат - периметр треугольника, равный 45.
        """
        self.assertEqual(perimeter(10, 15, 20), 45)

    def test_area_zero(self):
        """
        Тестирование функции area с нулевой стороной.

        Проверяет, что площадь треугольника со стороной 0 равна 0.
        """
        
        self.assertEqual(area(10, 0), 0)

    def test_perimeter_zero(self):
        """
        Тестирование функции perimeter с нулевыми сторонами.

        Проверяет, что результат периметра при нулевых значениях сторон треугольника равен 0.
        """
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_area_negative(self):
        """
        Тестирование функции area при отрицательных значениях сторон.
        Ожидаемый результат - ошибка.
        """
        with self.assertRaises(ValueError):
            area(-10, 5)

    def test_perimeter_negative(self):
        """
        Тестирование функции perimeter при отрицательных значениях сторон.
        Ожидаемый результат - ошибка.
        """
        with self.assertRaises(ValueError):
            perimeter(-10, 15, 20)

    def test_area_string(self):
        """
        Тестирование функции area со строковыми значениями сторон.
        Ожидаемый результат - ошибка.
        """
        with self.assertRaises(TypeError):
            area("10", "5")

    def test_perimeter_string(self):
        """
        Тестирование функции perimeter со строковыми значениями сторон.
        Ожидаемый результат - ошибка.
        """
        with self.assertRaises(TypeError):
            perimeter("10", "15", "20")

    def test_area_boolean(self):
        """
        Тестирование функции area с булевыми значениями сторон.
        Ожидаемый результат - ошибка.
        """
        with self.assertRaises(TypeError):
            area(True, False)

    def test_perimeter_boolean(self):
        """
        Тестирование функции perimeter с булевыми значениями сторон.
        Ожидаемый результат - ошибка.
        """
        with self.assertRaises(TypeError):
            perimeter(True, False, True)

    def test_existence(self):
        """
        Тестирование функции perimeter со сторонами, образуюзщими несуществующий треугольник.
        Ожидаемый результат - ошибка.
        """
        with self.assertRaises(ValueError):
            perimeter(10, 50, 100)

    def test_exist(self):
        """
        Тестирование функции perimeter с неправильными сторонами.

        Проверяет, что результат периметра при нулевых значениях сторон треугольника равен 0.
        """
        self.assertEqual(perimeter(1, 5, 10), 0)
