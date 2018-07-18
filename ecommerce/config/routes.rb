Rails.application.routes.draw do
  resources :users
  resources :invoices
  resources :products
  get 'home/index'
  devise_for :users, path: 'authorize'
  root to: 'home#index'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
