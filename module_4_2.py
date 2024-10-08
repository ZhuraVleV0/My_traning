def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


test_function()
inner_function() # при выводе появится ошибка имя "inner_function" не определено в глобальном пространстве имен


