import java.util.Comparator;
import java.util.PriorityQueue;

enum OrderType {
    BUY(0), SELL(1);

    private final int value;

    private OrderType(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }
}

class Order {
    private int amount;
    private int price;
    private OrderType type;

    public Order(int amount, int price, OrderType type) {
        this.amount = amount;
        this.price = price;
        this.type = type;
    }

    public OrderType getType() {
        return type;
    }

    public int getAmount() {
        return amount;
    }

    public int getPrice() {
        return price;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }
}

class Solution {
    private PriorityQueue<Order> buyQueue;
    private PriorityQueue<Order> sellQueue;
    private static final long MODULO = 1_000_000_007L;

    public Solution() {
        this.buyQueue = new PriorityQueue<>(Comparator.comparing(Order::getPrice).reversed());
        this.sellQueue = new PriorityQueue<>(Comparator.comparing(Order::getPrice));
    }

    private void addBuyOrder(Order order) {
        if (!sellQueue.isEmpty()) {
                Order sellOrder = sellQueue.peek();

                while (sellOrder != null && sellOrder.getPrice() <= order.getPrice() && order.getAmount() > 0) {
                    int buyingAmount = Math.min(order.getAmount(), sellOrder.getAmount());

                    order.setAmount(order.getAmount() - buyingAmount);
                    sellOrder.setAmount(sellOrder.getAmount() - buyingAmount);

                    if (sellOrder.getAmount() == 0) {
                        sellQueue.poll();
                        // Get next sell order
                        sellOrder = sellQueue.peek();
                    }
                }
            }

            if (order.getAmount() > 0) {
                    buyQueue.add(order);
            }
    }

    private void addSellOrder(Order order) {
        if (!buyQueue.isEmpty()) {
                Order buyOrder = buyQueue.peek();

                while (buyOrder != null && buyOrder.getPrice() >= order.getPrice() && order.getAmount() > 0) {
                    int sellingAmount = Math.min(order.getAmount(), buyOrder.getAmount());

                    order.setAmount(order.getAmount() - sellingAmount);
                    buyOrder.setAmount(buyOrder.getAmount() - sellingAmount);

                    if (buyOrder.getAmount() == 0) {
                        buyQueue.poll();
                        // Get next sell order
                        buyOrder = buyQueue.peek();
                    }
                }
            }

            if (order.getAmount() > 0) {
                    sellQueue.add(order);
            }
    }

    public void handleOrder(Order order) {
        if (order.getType() == OrderType.BUY) {
            // Check the sell queue if there are any
            addBuyOrder(order);
            return;
        }

        // If it is a sell
        addSellOrder(order);

    }

    public int getNumberOfBacklogOrders(int[][] orders) {
        for (var order : orders) {
            OrderType typeOfOrder = order[2] == 1 ? OrderType.SELL : OrderType.BUY;

            Order currentOrder = new Order(order[1], order[0], typeOfOrder);
            handleOrder(currentOrder);
        }

        long temp_result = 0;

        for (var order : buyQueue) {
            temp_result += order.getAmount();
        }

        for (var order : sellQueue) {
            temp_result += order.getAmount();
        }

        return (int) (temp_result % MODULO);
    }
}