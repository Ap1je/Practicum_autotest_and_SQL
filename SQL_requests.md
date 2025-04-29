## Команды SQL запросов для работы с БД

# Задание 1
SELECT c.login AS "Логин курьера" , COUNT(o.*) AS "Заказов в работе" FROM "Couriers" c LEFT JOIN "Orders" o ON c.id = o."courierId" WHERE o."inDelivery" = true GROUP BY c.login;

# Задание 2
SELECT "track" AS "Номер заказа", CASE WHEN "finished" = true THEN 2 WHEN "cancelled" = true THEN -1 WHEN "inDelivery" = true THEN 1 ELSE 0 END AS "Статус заказа" FROM "Orders";