-- 4. Trigger that decreases the quantity of an item after adding an order

CREATE TRIGGER update_quantity AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END
