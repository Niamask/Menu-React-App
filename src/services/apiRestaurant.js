const API_URL = 'https://react-fast-pizza-api.onrender.com/api';
// const API_URL = 'http://127.0.0.1:5000';

export async function getMenu() {
  // const res = await fetch(`${API_URL}/menu`);
  const res = await fetch(`http://127.0.0.1:5000/all_dishes`);

  // fetch won't throw error on 400 errors (e.g. when URL is wrong), so we need to do it manually. This will then go into the catch block, where the message is set
  if (!res.ok) throw Error('Failed getting menu');

  const { data } = await res.json();
  // console.log('Menu', data);
  return data;
}

export async function getOrder(id) {
  const res = await fetch(`http://127.0.0.1:5000/order/${id}`);
  if (!res.ok) throw Error(`Couldn't find order #${id}`);

  const { data } = await res.json();
  // console.log('get Order: ', data);
  // console.log('check name', data.cart);
  // console.log('check name2', data.cart[0].pizzaId);

  return data;
}

export async function createOrder(newOrder) {
  try {
    const res = await fetch(`http://127.0.0.1:5000/order`, {
      method: 'POST',
      body: JSON.stringify(newOrder),
      headers: {
        'Content-Type': 'application/json',
      },
    });
    // console.log('new order: ', newOrder);

    if (!res.ok) throw Error();
    const { data } = await res.json();
    return data;
  } catch {
    throw Error('Failed creating your order');
  }
}

export async function updateOrder(id, updateObj) {
  try {
    const res = await fetch(`${API_URL}/order/${id}`, {
      method: 'PATCH',
      body: JSON.stringify(updateObj),
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!res.ok) throw Error();
    // We don't need the data, so we don't return anything
  } catch (err) {
    throw Error('Failed updating your order');
  }
}
