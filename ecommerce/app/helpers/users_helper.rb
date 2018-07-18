module UsersHelper
  def customer_ids(user)
    customer_ids = []
    User.available_customer_ids.find_each do |customer|
      customer_ids << [customer.customer_id, customer.customer_id]
    end
    customer_ids << [user.customer_id, user.customer_id]
  end
end
