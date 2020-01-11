SELECT person.first_name, person.last_name, COUNT(DISTINCT `order`.id) as total_orders,
SUM(order_item.quantity) AS total_items_bought,
SUM(item.price * order_item.quantity - order_item.discount) AS total_money_spent
FROM person
LEFT OUTER JOIN `order` ON `order`.person_id = person.id
LEFT OUTER JOIN order_item ON order_item.order_id = `order`.id
LEFT OUTER JOIN item ON item.id = order_item.item_id
GROUP BY person.id