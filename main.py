from examples.authentication import generate_user_credentials
from google.shopping import merchant_inventories_v1beta


_ACCOUNT = "INSERT_ACCOUNT_HERE"
_PRODUCT = "INSERT_PRODUCT_HERE"
_PARENT = f"accounts/{_ACCOUNT}/products/{_PRODUCT}"
_STORE_CODE = "INSERT_STORE_CODE_HERE"


def insert_local_inventory():
  """Inserts a `LocalInventory` to a given product.

  Replaces the full `LocalInventory` resource if an entry with the same
  `region` already exists for the product.

  It might take up to 30 minutes for the new or updated `LocalInventory`
  resource to appear in products.
  """

  # Gets OAuth Credentials.
  credentials = generate_user_credentials.main()

  # Creates a client.
  client = merchant_inventories_v1beta.LocalInventoryServiceClient(
      credentials=credentials)

  # Creates a Local inventory and populate its attributes.
  local_inventory = merchant_inventories_v1beta.LocalInventory()
  local_inventory.store_code = _STORE_CODE
  local_inventory.availability = "in stock"
  local_inventory.price = {
      "currency_code": "USD",
      "amount_micros": 33450000,
  }

  # Creates the request.
  request = merchant_inventories_v1beta.InsertLocalInventoryRequest(
      parent=_PARENT,
      local_inventory=local_inventory,
  )

  # Makes the request and catch and print any error messages.
  try:
    response = client.insert_local_inventory(request=request)

    print("Insert successful")
    print(response)
  except Exception as e:
    print("Insert failed")
    print(e)


if __name__ == "__main__":
  insert_local_inventory()