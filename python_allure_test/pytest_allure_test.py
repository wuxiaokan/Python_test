import pytest





class TestClass:

        check=1

        def test_one(self):
            x = "this"
            assert 'h' in x

        def test_two(self):
            x = "hello"

            assert hasattr(TestClass, 'check')

        def test_three(self):
            a = "hello"
            b = "hello world"
            assert a in b

if __name__ == "__main__":
    pytest.main('-q test_class.py')