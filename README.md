# geoCalculator
 Измеряет прямое расстояние между МКАД и добавленным адресом

Инструкция по использованию приложения:
1) Запустить приложение 
2) Отправить методом POST(используя Postman, например) запрос на url '.../geo/coordinates' формата json с данными вида: {"check_address": "Москва, Погодинская улица, 8к1"}
3) Вы получите ответ, соответствующий условиям:
        а) Если адрес находится за территорией МКАДа - расстояние от ближайшей внешней точки МКАДа до введенного адреса (в километрах)
        б) Если адрес расположен на территории МКАДа - соответствующее сообщение
        в) Если адрес введен некорректно/не введен - соответствующее сообщение
        
Стоит понимать, что расстояние рассчитывается 'напрямую', т.е. не учитывает схемы проезда, расположение объектов на пути и текущую ситуацию на дорогах, т.к. приложение рассчитывает расстояние на основании геолокационных данных. Так же стоит отметить, что крайними точками МКАДа являются точки километров МКАДа. Именно от одной из них (ближайшей к введенному адресу) производится рассчет расстояния.
