export default function CheckoutPage() {
  return (
    <div>
      <h1>Checkout</h1>

      <h2>Order Summary</h2>

      <p>Mobile - ₹25,000</p>
      <p>Laptop - ₹50,000</p>

      <h3>Total: ₹75,000</h3>

      <h2>Shipping Details</h2>

      <form>
        <div>
          <label>Name:</label>
          <input type="text" placeholder="Enter your name" />
        </div>

        <br />

        <div>
          <label>Address:</label>
          <input type="text" placeholder="Enter your address" />
        </div>

        <br />

        <div>
          <label>Phone:</label>
          <input type="text" placeholder="Enter phone number" />
        </div>

        <br />

        <button type="submit">
          Place Order
        </button>
      </form>
    </div>
  );
}