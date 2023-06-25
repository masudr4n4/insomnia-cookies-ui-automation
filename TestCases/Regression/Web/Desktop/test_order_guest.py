import time

import pytest
import Utilities.CustomLogger as cl
import Static.Constants as const
import logging
import softest
import allure

log = cl.customLogger(logging.INFO)

val = ''


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.usefixtures('create_resource')
class TestHome(softest.TestCase):
    """
    Test Class for Order Module for guest user
    """

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/2933")
    @allure.story('place a pickup order with payment method as CC')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
                            Given user is on homepage ​
                            When user click on Select Address​
                            And user clicks on Pickup button​
                            When user enter the address and select address from suggestion​
                                | address | 1084 East Lancaster Avenue |
                            Then verify user navigates to locations page​
                            When user clicks the "View Menu" button on a store
                            Then verify home page with available menu options specific to store should be displayed
                            When user clicks a box product
                                | product | Insomniac |
                            And click "pick for me"
                            And click "Add to Cart"
                            Then verify product gets added to the cart
                            When user clicks the cart icon
                            And click "Review Order" button
                            Then verify checkout page is displayed
                            When user enter your contact details
                                |firstName|
                                |lastName|
                                |phoneNumber|
                                |email|
                            And click "Add Contact"
                            And user selects payment method as credit/debit card
                            And enter the card details
                                | Cardholder Name | Test |
                                | CardNumber | 4111111111111111 |
                                | ExpirationDate | 07/20 |
                                | BillZipCode | 19010 |
                            And click Add card button
                            And Click Place order
                            Then verify Order confirmed page is displayed""")
    def test_2933_place_pickup_CC_Box_Order(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.click_pickup_btn()
        locations_obj = self.home_obj.enter_and_select_pickup_address(
            const.location_page_dict["TestStore"])
        locations_obj.click_store_in_store_list(0)
        locations_obj.click_view_menu_btn()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj.click_cart_btn(1)
        checkout_obj = product_obj.click_review_order_btn()
        checkout_obj.click_pick_up_time()
        checkout_obj.select_date_from_dropdown(1)
        checkout_obj.select_time_from_dropdown(1)
        checkout_obj.click_select_button()
        checkout_obj.click_contact_info(3)
        checkout_obj.enter_and_add_contact_details(
            const.checkout_page_dict["firstName"],
            const.checkout_page_dict["lastName"],
            const.checkout_page_dict["phoneNumber"],
            const.checkout_page_dict["email"])
        checkout_obj.click_choose_a_payment_method(4)
        checkout_obj.enter_cc_dc_details_and_Add_card(
            const.checkout_page_dict["cardHolderName"],
            const.checkout_page_dict["cardNumber"],
            const.checkout_page_dict["expirationDate"],
            const.checkout_page_dict["cvvNumber"],
            const.checkout_page_dict["zipCode"])
        checkout_obj.click_place_order_btn()
        boolean = checkout_obj.verify_order_confirm_page()
        self.soft_assert(
            self.assertTrue,
            boolean,
            "Order confirmation page not displayed")
        self.assert_all()

    @allure.story('Click ON product for viewing single item PDP')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
                            Given user is on home page
                            When user enters the address
                            | address | 228 E Clayton St, Athens GA |
                            And user clicks on a product
                            Then the single item PDP should open
                            When user select cookie falvor
                            And user click Add to order button
                            And clicks on cart
                            Then view order page should open
                            When user click on Review order button
                            x  Then checkout page should open
                            When user enters Delivery time and Delivery date
                            And user enter contact info
                            And user enters credit card detai   ls
                                | cc no     | 4111111111111111 |
                                | cc expiry | 12 20            |
                                | cvv       | 111              |
                            And user clicks on Place Order
                            Then Order confirmation page should appear  """)
    def test_2566_single_item_pdp(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.enter_and_select_delivery_address(
            const.location_page_dict["TestStore"])
        self.home_obj.wait_for_menu_to_load()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj.click_cart_btn(1)
        checkout_obj = product_obj.click_review_order_btn()
        checkout_obj.click_delivery_time()
        checkout_obj.select_date_from_dropdown(1)
        checkout_obj.select_time_from_dropdown(1)
        checkout_obj.click_select_button()
        checkout_obj.click_contact_info(4)
        checkout_obj.enter_and_add_contact_details(
            const.checkout_page_dict["firstName"],
            const.checkout_page_dict["lastName"],
            const.checkout_page_dict["phoneNumber"],
            const.checkout_page_dict["email"])
        checkout_obj.click_choose_a_payment_method(5)
        checkout_obj.enter_cc_dc_details_and_Add_card(
            const.checkout_page_dict["cardHolderName"],
            const.checkout_page_dict["cardNumber"],
            const.checkout_page_dict["expirationDate"],
            const.checkout_page_dict["cvvNumber"],
            const.checkout_page_dict["zipCode"])
        checkout_obj.click_place_order_btn()
        boolean = checkout_obj.verify_order_confirm_page()
        self.soft_assert(
            self.assertTrue,
            boolean,
            "Order confirmation page not displayed")
        self.assert_all()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/3088")
    @allure.story('Gift for someone else CC order')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
                            Given user is on home page
                            When user enters the address
                            | address | 1000 MacDougal Street, New York |
                            And user clicks on a product
                            Then the single item PDP should open
                            When user select cookie flavor
                            And user click Add to order button
                            And clicks on cart
                            Then view order page should open
                            When user click on Review order button
                            And check this is a gift for someone else
                            And click and enter the recipient contact information
                            And user enter contact info
                            And user enters credit card details
                                | cc no     | 4111111111111111 |
                                | cc expiry | 12 20            |
                                | cvv       | 111              |
                            And user clicks on Place Order
                            Then Order confirmation page should appear""")
    def test_3088_gift_for_someone_else_CC(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.enter_and_select_delivery_address(
            const.location_page_dict["TestStore"])
        self.home_obj.wait_for_menu_to_load()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj.click_cart_btn(1)
        checkout_obj = product_obj.click_review_order_btn()
        checkout_obj.click_this_is_a_gift_chkbx()
        checkout_obj.click_gift_recipient_lnk()
        checkout_obj.enter_recipient_details_and_save(
            const.checkout_page_dict["firstName"],
            const.checkout_page_dict["lastName"],
            const.checkout_page_dict["phoneNumber"])
        checkout_obj.click_delivery_time()
        checkout_obj.select_date_from_dropdown(1)
        checkout_obj.select_time_from_dropdown(1)
        checkout_obj.click_select_button()
        checkout_obj.click_contact_info(5)
        checkout_obj.enter_and_add_contact_details(
            const.checkout_page_dict["firstName"],
            const.checkout_page_dict["lastName"],
            const.checkout_page_dict["phoneNumber"],
            const.checkout_page_dict["email"])
        checkout_obj.click_choose_a_payment_method(6)
        checkout_obj.enter_cc_dc_details_and_Add_card(
            const.checkout_page_dict["cardHolderName"],
            const.checkout_page_dict["cardNumber"],
            const.checkout_page_dict["expirationDate"],
            const.checkout_page_dict["cvvNumber"],
            const.checkout_page_dict["zipCode"])
        checkout_obj.click_place_order_btn()
        boolean = checkout_obj.verify_order_confirm_page()
        self.soft_assert(
            self.assertTrue,
            boolean,
            "Order confirmation page not displayed")
        self.assert_all()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/3017")
    @allure.story('Guest User is able to place a Delivery order using Cash on delivery')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
                            Given a Guest User is on home page
                            When they select Select Address
                            And enter the <delivery address>
                            And select the delivery address from the drop-down list
                            And select a brownie (e.g. Chocolate Chip Brownie) from the Brownies category
                            And selects 2 toppings
                            And increase the quantity to 3
                            And select Add to Order
                            And select the shopping cart icon
                            And select the Review Order option
                            And enter the contact details
                            And select the Add contact option
                            And select the Cash on Delivery option from the Payment Method section
                            And select the Save Changes option
                            And select the Place Order option
                            Then the order confirmation page should be displayed""")
    def test_3017_cash_on_delivery(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.enter_and_select_delivery_address(
            const.location_page_dict["TestStore"])
        self.home_obj.wait_for_menu_to_load()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.select_product_quantity(4)
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj.click_cart_btn(3)
        checkout_obj = product_obj.click_review_order_btn()
        checkout_obj.click_delivery_time()
        checkout_obj.select_date_from_dropdown(1)
        checkout_obj.select_time_from_dropdown(1)
        checkout_obj.click_select_button()
        checkout_obj.click_contact_info(4)
        checkout_obj.enter_and_add_contact_details(
            const.checkout_page_dict["firstName"],
            const.checkout_page_dict["lastName"],
            const.checkout_page_dict["phoneNumber"],
            const.checkout_page_dict["email"])
        checkout_obj.click_choose_a_payment_method(5)
        checkout_obj.select_cash_on_delivery()
        checkout_obj.click_place_order_btn()
        boolean = checkout_obj.verify_order_confirm_page()
        self.soft_assert(
            self.assertTrue,
            boolean,
            "Order confirmation page not displayed")
        self.assert_all()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/3193")
    @allure.story('Guest User: modify delivery order from cart and place order')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
        Given a Guest User is on home page
        When they select Select Address
        And enter the <delivery address>
        And select the delivery address from the drop-down list
        When user clicks a box product
        | product | Major Rager |
        And click "pick for me"
        And click "Add to Order"
        When user clicks the cart icon
        And click "Modify Order"
        And update the product quantity to 3
        And select both special packaging options
        And click Update Order
        Then verify special packaging options are displayed on the cart
        And verify updated quantity is displayed on the cart
        When click "Review Order" button
        Then verify checkout page is displayed
        When user enter your contact details
            |firstName|
            |lastName|
            |phoneNumber|
            |email|
        And click "Add Contact"
        And select the Cash on Delivery option from the Payment Method section
        And select the Save Changes option
        And select the Place Order option
        Then the order confirmation page should be displayed""")
    def test_3193_modify_order(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.enter_and_select_delivery_address(
            const.location_page_dict["TestStore"])
        self.home_obj.wait_for_menu_to_load()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj.click_cart_btn(1)
        product_obj.click_modify_order_lnk()
        product_obj.click_pick_for_me()
        product_obj.select_product_quantity(3)
        product_obj.click_update_order_btn()
        checkout_obj = product_obj.click_review_order_btn()
        checkout_obj.click_delivery_time()
        checkout_obj.select_date_from_dropdown(1)
        checkout_obj.select_time_from_dropdown(1)
        checkout_obj.click_select_button()
        checkout_obj.click_contact_info(4, False)
        checkout_obj.enter_and_add_contact_details(
            const.checkout_page_dict["firstName"],
            const.checkout_page_dict["lastName"],
            const.checkout_page_dict["phoneNumber"],
            const.checkout_page_dict["email"])
        checkout_obj.click_choose_a_payment_method(5)
        checkout_obj.select_cash_on_delivery()
        checkout_obj.click_place_order_btn()
        boolean = checkout_obj.verify_order_confirm_page()
        self.soft_assert(
            self.assertTrue,
            boolean,
            "Order confirmation page not displayed")
        self.assert_all()

    @allure.story("Guest User: modify pickup order from cart and place order")
    @allure.link("https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/3194")
    @allure.description("""Given guest user is on homepage ​
        When user click on Select Address​
        And user clicks on Pickup button​
        When user enter the address and select address from suggestion​
            | address | 1000 MacDougal Street New York |
        When user clicks the "View Menu" button on a store
        And user clicks a box product
            | product | Six Pack |
        And click "pick for me"
        And click "Add to Cart"
        When user clicks the cart icon
        And click "Modify Order"
        And update the product quantity to 3
        And select special packaging option
        And click Update Order
        Then verify special packaging options are displayed on the cart
        And verify updated quantity is displayed on the cart
        When click "Review Order" button
        And user enter your contact details
            |firstName|
            |lastName|
            |phoneNumber|
            |email|
        And click "Add Contact"
        And select the Cash on Delivery option from the Payment Method section
        And select the Save Changes option
        And select the Place Order option
        Then the order confirmation page should be displayed""")
    def test_3194_modify_order(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.click_pickup_btn()
        locations_obj = self.home_obj.enter_and_select_pickup_address(
            const.location_page_dict["TestStore"])
        locations_obj.click_store_in_store_list(0)
        locations_obj.click_view_menu_btn()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj.click_cart_btn(1)
        product_obj.click_modify_order_lnk()
        product_obj.click_pick_for_me()
        product_obj.select_product_quantity(3)
        product_obj.click_update_order_btn()
        checkout_obj = product_obj.click_review_order_btn()
        checkout_obj.click_pick_up_time()
        checkout_obj.select_date_from_dropdown(1)
        checkout_obj.select_time_from_dropdown(1)
        checkout_obj.click_select_button()
        checkout_obj.click_contact_info(3)
        checkout_obj.enter_and_add_contact_details(
            const.checkout_page_dict["firstName"],
            const.checkout_page_dict["lastName"],
            const.checkout_page_dict["phoneNumber"],
            const.checkout_page_dict["email"])
        checkout_obj.click_choose_a_payment_method(4)
        checkout_obj.enter_cc_dc_details_and_Add_card(
            const.checkout_page_dict["cardHolderName"],
            const.checkout_page_dict["cardNumber"],
            const.checkout_page_dict["expirationDate"],
            const.checkout_page_dict["cvvNumber"],
            const.checkout_page_dict["zipCode"])
        checkout_obj.click_place_order_btn()
        boolean = checkout_obj.verify_order_confirm_page()
        self.soft_assert(
            self.assertTrue,
            boolean,
            "Order confirmation page not displayed")
        self.assert_all()

    @allure.story('Click ON remove item from cart')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
                            Given user is on home page
                            When user enters the address
                            | address | 228 E Clayton St, Athens GA |
                            And user clicks on a product
                            Then the single item PDP should open
                            When user click pick for me
                            And user click Add to order button
                            And user clicks on a product
                            Then the single item PDP should open
                            When user click pick for me
                            And user click Add to order button
                            And clicks on cart
                            Then view order page should open
                            Then click on remove link of first product
                            Then review order button should be displayed  """)
    def test_3200_remove_single_item_functionality(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.enter_and_select_delivery_address(
            const.location_page_dict["TestStore"])
        self.home_obj.wait_for_menu_to_load()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj.click_cart_btn(2)
        product_obj.click_remove_link()
        flag1 = product_obj.is_review_order_btn_present()
        self.soft_assert(
            self.assertTrue,
            flag1,
            "Review order button is not displayed")
        self.assert_all()

    @allure.story('Click ON remove all item from cart')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
                            Given user is on home page
                            When user enters the address
                            | address | 228 E Clayton St, Athens GA |
                            And user clicks on a product
                            Then the single item PDP should open
                            When user click pick for me
                            And user click Add to order button
                            And user clicks on a product
                            Then the single item PDP should open
                            When user click pick for me
                            And user click Add to order button
                            And clicks on cart
                            Then view order page should open
                            And click on remove link of first product
                            Then click on remove link of second product
                            Then cart is empty message should be displayed  """)
    def test_3201_remove_all_item_functionality(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.enter_and_select_delivery_address(
            const.location_page_dict["TestStore"])
        self.home_obj.wait_for_menu_to_load()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj.click_cart_btn(2)
        product_obj.click_remove_link()
        product_obj.click_remove_link()
        flag = product_obj.is_cart_empty_present()
        self.soft_assert(
            self.assertTrue,
            flag,
            'Test failed as items are present in cart')
        self.assert_all()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/3292")
    @allure.story("Guest User: Add Cutsom tip ($10)")
    @allure.description("""
    Given a Guest User is on home page
    When they select Select Address
    And enter the <delivery address>
    And select the delivery address from the drop-down list
    And select a product (Insomniac (24 Traditional))
    Click pick for me button
     And select Add to Order
    And select the shopping cart icon
    And select the Review Order option
    And select a delivery time
    And enter the contact details
    And select the Add contact option
    And select the Add new Credit/Debit card option from the Payment Method section
    And enter the card details
    And select the Add card option
    Select Custom Tip option
    Add $10 Tip
    Press Custom button again
    And select the Place Order option
    Then the order confirmation page should be displayed""")
    def test_3292_custom_tip_Scenario(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.enter_and_select_delivery_address(
            const.location_page_dict["TestStore"])
        self.home_obj.wait_for_menu_to_load()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj.click_cart_btn(1)
        checkout_obj = product_obj.click_review_order_btn()
        checkout_obj.click_delivery_time()
        checkout_obj.select_date_from_dropdown(1)
        checkout_obj.select_time_from_dropdown(1)
        checkout_obj.click_select_button()
        checkout_obj.click_contact_info(4)
        checkout_obj.enter_and_add_contact_details(
            const.checkout_page_dict["firstName"],
            const.checkout_page_dict["lastName"],
            const.checkout_page_dict["phoneNumber"],
            const.checkout_page_dict["email"])
        checkout_obj.click_choose_a_payment_method(5)
        checkout_obj.enter_cc_dc_details_and_Add_card(
            const.checkout_page_dict["cardHolderName"],
            const.checkout_page_dict["cardNumber"],
            const.checkout_page_dict["expirationDate"],
            const.checkout_page_dict["cvvNumber"],
            const.checkout_page_dict["zipCode"])

        amt = checkout_obj.get_subtotal_amount().split('$')[1]
        checkout_obj.add_tip("Custom")
        checkout_obj.click_place_order_btn()
        boolean = checkout_obj.verify_order_confirm_page()
        self.soft_assert(
            self.assertTrue,
            boolean,
            "Order confirmation page not displayed")
        self.assert_all()

    @allure.story('For pickup order remove item from cart until empty')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
                            Given user is on homepage ​
                            When user click on Select Address​
                            And user clicks on Pickup button​
                            | address | 228 E Clayton St, Athens GA |
                            And user clicks on a product
                            Then the single item PDP should open
                            When user click pick for me
                            And user click Add to order button
                            And user clicks on a product
                            Then the single item PDP should open
                            When user click pick for me
                            And user click Add to order button
                            And clicks on cart
                            Then view order page should open
                            And click on remove link of first product
                            Then click on remove link of second product
                            Then cart is empty message should be displayed  """)
    def test_2930_remove_all_item_functionality(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.click_pickup_btn()
        locations_obj = self.home_obj.enter_and_select_pickup_address(
            const.location_page_dict["TestStore"])
        locations_obj.click_store_in_store_list(0)
        locations_obj.click_view_menu_btn()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj.click_cart_btn(2)
        product_obj.click_remove_link()
        product_obj.click_remove_link()
        flag = product_obj.is_cart_empty_present()
        self.soft_assert(
            self.assertTrue,
            flag,
            'Test failed as items are present in cart')
        self.assert_all()

    @allure.story('For pickup order remove item from cart without emptying it')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
                            Given user is on homepage ​
                            When user click on Select Address​
                            And user clicks on Pickup button​
                            | address | 228 E Clayton St, Athens GA |
                            And user clicks on a product
                            Then the single item PDP should open
                            When user click pick for me
                            And user click Add to order button
                            And user clicks on a product
                            Then the single item PDP should open
                            When user click pick for me
                            And user click Add to order button
                            And clicks on cart
                            Then view order page should open
                            Then click on remove link of first product
                            Then review order button should be displayed  """)
    def test_2929_remove_single_item_functionality(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.click_pickup_btn()
        locations_obj = self.home_obj.enter_and_select_pickup_address(
            const.location_page_dict["TestStore"])
        locations_obj.click_store_in_store_list(0)
        locations_obj.click_view_menu_btn()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj.click_cart_btn(2)
        product_obj.click_remove_link()
        flag1 = product_obj.is_review_order_btn_present()
        self.soft_assert(
            self.assertTrue,
            flag1,
            "Review order button is not displayed")
        self.assert_all()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/3291")
    @allure.story("Gues USer : Add tip to the order (18 %)")
    @allure.description("""
    Given a Guest User is on home page
    When they select Select Address
    And enter the <delivery address>
    And select the delivery address from the drop-down list
    And select a product (Insomniac (24 Traditional))

    Click pick for me button
     And select Add to Order
    And select the shopping cart icon
    And select the Review Order option
    And select a delivery time
    And enter the contact details
    And select the Add contact option
    And select the Add new Credit/Debit card option from the Payment Method section
    And enter the card details
    And select the Add card option
    Add the tip ( 18%)
    And select the Place Order option
    Then the order confirmation page should be displayed""")
    def test_3291_tip_Scenario(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.enter_and_select_delivery_address(
            const.location_page_dict["TestStore"])
        self.home_obj.wait_for_menu_to_load()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj.click_cart_btn(1)
        checkout_obj = product_obj.click_review_order_btn()
        checkout_obj.click_delivery_time()
        checkout_obj.select_date_from_dropdown(1)
        checkout_obj.select_time_from_dropdown(1)
        checkout_obj.click_select_button()
        checkout_obj.click_contact_info(4)
        checkout_obj.enter_and_add_contact_details(
            const.checkout_page_dict["firstName"],
            const.checkout_page_dict["lastName"],
            const.checkout_page_dict["phoneNumber"],
            const.checkout_page_dict["email"])
        checkout_obj.click_choose_a_payment_method(5)
        checkout_obj.enter_cc_dc_details_and_Add_card(
            const.checkout_page_dict["cardHolderName"],
            const.checkout_page_dict["cardNumber"],
            const.checkout_page_dict["expirationDate"],
            const.checkout_page_dict["cvvNumber"],
            const.checkout_page_dict["zipCode"])
        amt = checkout_obj.get_subtotal_amount().split('$')[1]
        checkout_obj.add_tip("18%")
        checkout_obj.click_place_order_btn()
        boolean = checkout_obj.verify_order_confirm_page()
        self.soft_assert(
            self.assertTrue,
            boolean,
            "Order confirmation page not displayed")
        self.assert_all()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/3300")
    @allure.story('Guest User: apply discount coupon and place order')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
                        Given a Guest User is on home page
                        When they select Select Address
                        And enter the <delivery address>
                        And select the delivery address from the drop-down list
                        And select a product Major Rager (18 Traditional)
                        And Click pick for me button
                        And select the shopping cart icon
                        And select the Review Order option
                        And enter the contact details
                        And select the Add contact option
                        And enter the Discount promotional code "TestCoupon"
                        And click submit button
                        Then verify coupon code applied successfully
                        When select the CC option from the Payment Method section and enter the CC details
                        And select the Save Changes option
                        And select the Place Order option
                        Then the order confirmation page should be displayed""")
    def test_3300_apply_discount_coupon(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.enter_and_select_delivery_address(
            const.location_page_dict["TestStore"])
        self.home_obj.wait_for_menu_to_load()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj.click_cart_btn(1)
        checkout_obj = product_obj.click_review_order_btn()
        checkout_obj.click_delivery_time()
        checkout_obj.select_date_from_dropdown(1)
        checkout_obj.select_time_from_dropdown(1)
        checkout_obj.click_select_button()
        checkout_obj.click_contact_info(4)
        checkout_obj.enter_and_add_contact_details(
            const.checkout_page_dict["firstName"],
            const.checkout_page_dict["lastName"],
            const.checkout_page_dict["phoneNumber"],
            const.checkout_page_dict["email"])
        checkout_obj.enter_coupon_code_and_Submit(
            const.coupons_dict["discountcoupon"])
        flag = checkout_obj.get_coupon_validation_text()
        self.soft_assert(
            self.assertTrue,
            flag,
            "You must be logged in to use this coupon")
        self.assert_all()

    @allure.story('Guest User is able to place a Delivery order using Credit card')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
                            Given user is on home page
                            When user enters the address
                            | address | 228 E Clayton St, Athens GA |
                            And user clicks on a product
                            Then the single item PDP should open
                            When user select cookie falvor
                            And user click Add to order button
                            And clicks on cart
                            Then view order page should open
                            When user click on Review order button
                            x  Then checkout page should open
                            When user enters Delivery time and Delivery date
                            And user enter contact info
                            And user enters credit card detai   ls
                                | cc no     | 4111111111111111 |
                                | cc expiry | 12 20            |
                                | cvv       | 111              |
                            And user clicks on Place Order
                            Then Order confirmation page should appear
                            And store name should be displayed
                            """)
    def test_3007_delivery_order_using_credit_card(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.enter_and_select_delivery_address(
            const.location_page_dict["TestStore"])
        self.home_obj.wait_for_menu_to_load()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj.click_cart_btn(1)
        checkout_obj = product_obj.click_review_order_btn()
        checkout_obj.click_delivery_time()
        checkout_obj.select_date_from_dropdown(1)
        checkout_obj.select_time_from_dropdown(1)
        checkout_obj.click_select_button()
        checkout_obj.click_contact_info(4)
        checkout_obj.enter_and_add_contact_details(
            const.checkout_page_dict["firstName"],
            const.checkout_page_dict["lastName"],
            const.checkout_page_dict["phoneNumber"],
            const.checkout_page_dict["email"])
        checkout_obj.click_choose_a_payment_method(5)
        checkout_obj.enter_cc_dc_details_and_Add_card(
            const.checkout_page_dict["cardHolderName"],
            const.checkout_page_dict["cardNumber"],
            const.checkout_page_dict["expirationDate"],
            const.checkout_page_dict["cvvNumber"],
            const.checkout_page_dict["zipCode"])
        checkout_obj.click_place_order_btn()
        boolean = checkout_obj.verify_order_confirm_page()
        self.soft_assert(
            self.assertTrue,
            boolean,
            "Order confirmation page not displayed")

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/3884")
    @allure.story('Guest User is able to place a Delivery order using Credit card')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
                    Given user is on home page
                    When user enters the address
                    | address | insomnia cookies 1084 |
                    And user clicks on a product
                    Then the single item PDP should open
                    When user click Add to order button
                    And clicks on cart
                    Then view order page should open
                    When user click on Review order button
                    Then checkout page should open
                    When user enter contact info
                    And user enters credit card details
                        | cc no     | 4111111111111111 |
                        | cc expiry | 12 20            |
                        | cvv       | 111              |
                        | zipcode   | 19010            |
                    And user clicks on Place Order
                    Then Order confirmation page should appear
                    When user clicks on Track Order
                    Then tracker step page should open
                    When user clicks trackit button
                    Then tracker final page along with map navigation should be displayed
                                            """)
    def test_3884_track_delivery_order(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.enter_and_select_delivery_address(
            const.location_page_dict["TestStore"])
        self.home_obj.wait_for_menu_to_load()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj.click_cart_btn(1)
        checkout_obj = product_obj.click_review_order_btn()
        checkout_obj.click_delivery_time()
        checkout_obj.select_date_from_dropdown(1)
        checkout_obj.select_time_from_dropdown(1)
        checkout_obj.click_select_button()
        checkout_obj.click_contact_info(4)
        checkout_obj.enter_and_add_contact_details(
            const.checkout_page_dict["firstName"],
            const.checkout_page_dict["lastName"],
            const.checkout_page_dict["phoneNumber"],
            const.checkout_page_dict["email"])
        checkout_obj.click_choose_a_payment_method(5)
        checkout_obj.enter_cc_dc_details_and_Add_card(
            const.checkout_page_dict["cardHolderName"],
            const.checkout_page_dict["cardNumber"],
            const.checkout_page_dict["expirationDate"],
            const.checkout_page_dict["cvvNumber"],
            const.checkout_page_dict["zipCode"])
        confirmation_obj = checkout_obj.click_place_order_btn()
        boolean = checkout_obj.verify_order_confirm_page()
        self.soft_assert(
            self.assertTrue,
            boolean,
            "Order confirmation page not displayed")
        confirmation_obj.click_track_order()
        is_tracker_step_page_displayed = confirmation_obj.verify_track_order_step_page()
        self.soft_assert(
            self.assertTrue,
            is_tracker_step_page_displayed,
            "Tracker step page is not displayed")
        confirmation_obj.click_trackIt_order()
        is_tracker_page_displayed = confirmation_obj.verify_track_order_page()
        self.soft_assert(
            self.assertTrue,
            is_tracker_page_displayed,
            "Tracker final page is not displayed")

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/3943")
    @allure.story(
        'Guest User: Change Delivery to shipping address and clicking Okay should clear the cart and address should '
        'be changed to Shipping')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
                            Given guest user is on home page
                            When user enters the address
                            | address | insomnia cookies 1084 |
                            And user clicks on a product
                            Then the single item PDP should open
                            When user click Add to order button
                            And user clicks Ship Cookies link
                            Then Confirm changing store popup should display
                            When User clicks Okay on the popUp window
                            Then Cart should get cleared and address should be changed to Shipping
                                                            """)
    def test_3943_change_del_to_ship(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.enter_and_select_delivery_address(
            const.location_page_dict["TestStore"])
        self.home_obj.wait_for_menu_to_load()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        self.home_obj.click_ship_cookies()
        self.home_obj.click_ok_popup()
        order_method = self.home_obj.get_order_method()
        self.soft_assert(self.assertTrue, order_method, "Shipping to")
        cart_quantity = self.home_obj.get_cart_quantity()
        self.soft_assert(self.assertTrue, cart_quantity, "0")
        self.assert_all()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/3944")
    @allure.story(
        'Guest User: Change Delivery to shipping address and clicking Cancel should not clear the cart and address '
        'should remain to delivery')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
            Given guest user is on home page
            When user enters the address
            | address | insomnia cookies 1084 |
            And user clicks on a product
            Then the single item PDP should open
            When user click Add to order button
            And user clicks Ship Cookies link
            Then Confirm changing store popup should display
            When User clicks Cancel
            Then Cart should not get cleared and address should still remain to delivering to
                                            """)
    def test_3944_change_del_to_ship(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.enter_and_select_delivery_address(
            const.location_page_dict["TestStore"])
        self.home_obj.wait_for_menu_to_load()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        self.home_obj.click_ship_cookies()
        self.home_obj.click_cancel_popup()
        order_method = self.home_obj.get_order_method_delivery()
        self.soft_assert(self.assertTrue, order_method, "Delivering to")
        cart_quantity = self.home_obj.get_cart_quantity()
        self.soft_assert(self.assertTrue, cart_quantity, "1")
        self.assert_all()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/3988")
    @allure.story('Add Form Validation for First and Last Names on the Checkout Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
                    Given user is on home page
                    When user enters the address
                    | address | insomnia cookies 1084 |
                    And user clicks on a product
                    Then the single item PDP should open
                    When user click Add to order button
                    And clicks on cart
                    Then view order page should open
                    When user click on Review order button
                    Then checkout page should open
                    When user enter numeric values in firstname and lastname contact info
                    And then click Add contact
                    Then validation messages stating only letters and spaces are allowed should be displayed
                                            """)
    def test_3988_fName_lName_form_validation(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.enter_and_select_delivery_address(
            const.location_page_dict["TestStore"])
        self.home_obj.wait_for_menu_to_load()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj.click_cart_btn(1)
        checkout_obj = product_obj.click_review_order_btn()
        checkout_obj.click_contact_info(4)
        checkout_obj.enter_and_add_contact_details_form_validation(
            const.checkout_page_dict["alphaNumeric_Fname"],
            const.checkout_page_dict["alphanumeric_Lname"],
            const.checkout_page_dict["phoneNumber"],
            const.checkout_page_dict["email"])
        is_fName_error_msg_displayed = checkout_obj.is_fName_validation_msg_displayed()
        self.soft_assert(
            self.assertTrue,
            is_fName_error_msg_displayed,
            "Form validation for firstName is not displayed")
        is_lName_error_msg_displayed = checkout_obj.is_lName_validation_msg_displayed()
        self.soft_assert(
            self.assertTrue,
            is_lName_error_msg_displayed,
            "Form validation for lastName is not displayed")
        self.assert_all()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/3109")
    @allure.story('Guest User is able to place a Delivery order using Credit card')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
                                    Given user is on home page
                                    When user enters the address
                                    | address | 228 E Clayton St, Athens GA |
                                    And user clicks on a product
                                    Then the single item PDP should open
                                    When user select cookie falvor
                                    And user click Add to order button
                                    And clicks on cart
                                    Then view order page should open
                                    When user click on Review order button
                                    x  Then checkout page should open
                                    When user enters Delivery time and Delivery date
                                    And user enter contact info
                                    And user enters credit card details
                                        | cc no     | 4111111111111111 |
                                        | cc expiry | 12 20            |
                                        | cvv       | 111              |
                                    And user clicks on Place Order
                                    Then Order confirmation page should appear
                                    And store name should be displayed
                                    """)
    def test_3109_delivery_order_using_school_cash(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.enter_and_select_delivery_address(
            const.location_page_dict["TestStore"])
        self.home_obj.wait_for_menu_to_load()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj.click_cart_btn(1)
        checkout_obj = product_obj.click_review_order_btn()
        checkout_obj.click_delivery_time()
        checkout_obj.select_date_from_dropdown(1)
        checkout_obj.select_time_from_dropdown(1)
        checkout_obj.click_select_button()
        checkout_obj.click_contact_info(4)
        checkout_obj.enter_and_add_contact_details(
            const.checkout_page_dict["firstName"],
            const.checkout_page_dict["lastName"],
            const.checkout_page_dict["phoneNumber"],
            const.checkout_page_dict["email"])
        checkout_obj.click_choose_a_payment_method(5)
        checkout_obj.enter_school_cash_details_and_Add_card(
            const.checkout_page_dict["schoolcash_number"],
            const.checkout_page_dict["zipCode"])
        checkout_obj.click_place_order_btn()
        boolean = checkout_obj.verify_order_confirm_page()
        self.soft_assert(
            self.assertTrue,
            boolean,
            "Order confirmation page not displayed")
