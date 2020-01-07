WITH previous_query AS (
   SELECT customer_id,
      COUNT(subscription_id) AS 'subscriptions'
   FROM orders
   GROUP BY customer_id
)

SELECT first_name, last_name
FROM person;



SELECT name, price, quantity, discount, (price*quantity)-discount as sum
FROM order_item, item
	WHERE item.id = order_item.item_id

SELECT first_name, last_name, quantity, name, price
FROM person
JOIN order2
ON order2.person_id = person.id
JOIN order_item
ON order_item.order_id = order2.id
JOIN item
on order_item.item_id = item.id;