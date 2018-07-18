# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 2018_07_16_021946) do

  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "alembic_version", primary_key: "version_num", id: :string, limit: 32, force: :cascade do |t|
  end

  create_table "customers", id: :serial, force: :cascade do |t|
    t.string "customer_id", limit: 45
    t.string "password", limit: 45
    t.string "country", limit: 45
    t.index ["customer_id", "country"], name: "index_on_ci_c", unique: true
  end

  create_table "invoices", id: :serial, force: :cascade do |t|
    t.string "invoice_number", limit: 45
    t.string "stock_code", limit: 45
    t.string "description", limit: 45
    t.integer "quantity"
    t.datetime "invoice_date"
    t.float "unit_price"
    t.string "customer_id", limit: 45
    t.string "country", limit: 45
  end

  create_table "products", id: :serial, force: :cascade do |t|
    t.string "stock_code", limit: 45
    t.string "description", limit: 45
    t.float "unit_price"
    t.index ["stock_code", "unit_price"], name: "index_on_sc_up", unique: true
  end

  create_table "users", force: :cascade do |t|
    t.string "email", default: "", null: false
    t.string "encrypted_password", default: "", null: false
    t.string "reset_password_token"
    t.datetime "reset_password_sent_at"
    t.datetime "remember_created_at"
    t.integer "sign_in_count", default: 0, null: false
    t.datetime "current_sign_in_at"
    t.datetime "last_sign_in_at"
    t.inet "current_sign_in_ip"
    t.inet "last_sign_in_ip"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.integer "role"
    t.string "customer_id"
    t.index ["email"], name: "index_users_on_email", unique: true
    t.index ["reset_password_token"], name: "index_users_on_reset_password_token", unique: true
  end

end
