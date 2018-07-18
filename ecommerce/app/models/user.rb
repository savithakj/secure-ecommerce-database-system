class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :trackable, :validatable

  enum role: [:admin, :customer, :supplier]

  roles.each do |key, _|
    define_method "#{key}?" do
      key == role
    end
  end

  def self.available_customer_ids
    Customer.joins("left join users on customers.customer_id::integer = users.customer_id::integer")
        .where(users: {customer_id: nil})
        .select(:id, :customer_id)
  end

  def ability
    Ability.new(self)
  end
end
