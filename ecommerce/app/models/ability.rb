class Ability
  include CanCan::Ability

  def initialize(user)
    # binding.pry
    case user.role
    when "admin"
     can :edit, Product
     can :manage, Invoice
      can :manage, User
    else
      can :read, Product
      can :read, Invoice, :customer_id => user.customer_id
      cannot :read, User
    end
  end
end
