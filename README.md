# complex-calculator
Для выполнения проекта потребуется Python 3.x. Убедитесь, что у вас установлены следующие пакеты:

Python 3.x
pip (пакетный менеджер Python)
Вы можете установить необходимые пакеты с помощью следующей команды:
pip install -r requirements.txt
Для запуска программы выполните следующую команду:
python main.py




Принципы SOLID и паттерны проектирования
Single Responsibility Principle (SRP): Каждый класс в проекте выполняет только одну задачу.
Open/Closed Principle (OCP): Классы открыты для расширения, но закрыты для модификации.
Liskov Substitution Principle (LSP): Все созданные классы могут быть использованы вместо своих базовых типов.
Interface Segregation Principle (ISP): У нас нет интерфейсов, которые клиент не использует.
Dependency Inversion Principle (DIP): Модули верхнего уровня (main.py) не зависят от модулей нижнего уровня (complex_number.py, calculator.py), а оба зависят от абстракций (логгер).