import pytest
import Utilities.CustomLogger as cl
import Static.Constants as const
import logging
import softest
import time
import allure

log = cl.customLogger(logging.INFO)

val = ''


@pytest.mark.regression
@pytest.mark.usefixtures('create_resource')
class TestProduct(softest.TestCase):
    """
    Test Class for Contact Page
    """

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/2440")
    @allure.story('Cannot Add Box Products To Cart')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
        UAC1: First enter the delivery address in the beginning on home page and then selecting the box product
                        Given User is on home page​
                        When User selects the delivery address​
                        And Enter the delivery address​
                        And select one address from the address suggestion list​
                        And user select Boxes​
                        And select a box product "Insomniac (24 traditional)"​
                        And Click "Pick for me"​
                        And click "Add to Order"​
                        Then the product should get added to the cart​""")
    def test_2517_add_box_product_to_cart(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.enter_and_select_delivery_address(
            const.location_page_dict["TestStore"])
        self.home_obj.wait_for_menu_to_load()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        flag = self.home_obj.is_item_Added()
        self.soft_assert(
            self.assertTrue,
            flag,
            'Test failed as item did not get '
            'added to cart')
        self.assert_all()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/2440")
    @allure.story('Cannot Add Box Products To Cart')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
            UAC2: First select the box product and then enter the delivery address​
                    Given User is on home page​
                    When user select Boxes​
                    And select a box product "Insomniac (24 traditional)"​
                    And Click "Pick for me"​
                    When user click "Add to Order"​
                    Then address popup to enter the address should get displayed​
                    When User selects the delivery address​
                    And Enter the delivery address​
                    And select one address from the address suggestion list​
                    Then the product should get added to the cart """)
    def test_2518_add_box_product_to_cart(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.enter_and_select_delivery_address(
            const.location_page_dict["TestStore"])
        self.home_obj.wait_for_menu_to_load()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        flag = self.home_obj.is_item_Added()
        self.soft_assert(
            self.assertTrue,
            flag,
            'Test failed as item did not get '
            'added to cart')
        self.assert_all()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/2707")
    @allure.story('Cannot Add Box Products To Cart')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
            UAC: Clear Pick for me selection
                            Given User is on home page​
                            When User selects the delivery address​
                            And Enter the delivery address​
                            And select one address from the address suggestion list​
                            And user select Boxes​
                            And select a box product "Insomniac (24 traditional)"​
                            And Click "Pick for me"​
                            Then the items should get pick
                            When user clicks on clear selection
                            Then pick for me selection should get cleared​""")
    def test_2707_clear_pick_for_me_selection(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.enter_and_select_delivery_address(
            const.location_page_dict["TestStore"])
        self.home_obj.wait_for_menu_to_load()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        flag1 = product_obj.verify_add_to_order_button_is_displayed()
        self.soft_assert(
            self.assertTrue,
            flag1,
            "add to order button is not displayed")
        product_obj.click_clear_selections()
        flag2 = product_obj.verify_add_to_order_button_is_not_displayed()
        self.soft_assert(
            self.assertTrue,
            flag2,
            "pick for me selection not cleared")
        self.assert_all()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/3188")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("""Given a Guest User is on home page
        When they select Address
        And enter the <delivery address> |1084 East Lancaster Ave Bryn|
        And select the delivery address from the drop-down list
        When user clicks a product with total under 20$
        | product | Chocolate Chip Brownie |
        And selects 2 toppings
        And increase the quantity to 3
        And click "Add to Order"
        Then verify points earned total is calculated based on the condition for order total under $20""")
    def test_3188_loyalty_under_20(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.enter_and_select_delivery_address(
            const.location_page_dict["TestStore"])
        self.home_obj.wait_for_menu_to_load()
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.select_product_quantity(3)
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj.click_cart_btn(2)
        points = product_obj.get_loyalty_points_text()
        self.soft_assert(self.assertGreaterEqual, int(
            points.split()[2]), 0, "Loyalty points not upated")
        self.assert_all()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/3189")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Guest User: Verify loyalty point earned for Delivery total above 20$ "
                  "calculates to 1$ = 1.25 point with total points round off to the nearest lowest whole number")
    @allure.description("""GGiven Guest User is on home page
        When they select Address
        And enter the <delivery address> |1084 East Lancaster Ave Bryn|
        And select the delivery address from the drop-down list
        When user cl icks a product with total above 20$
        | product | Insomniac (24 Traditional) |
        And click "pick for me"
        And click "Add to Order"
        And user clicks the cart icon
        Then verify points earned total is calculated based on the condition for order total above $20""")
    def test_3189_loyalty_above_20(self):
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
        points = product_obj.get_loyalty_points_text()
        self.soft_assert(self.assertGreaterEqual, int(
            points.split()[2]), 0, "Loyalty points not upated")
        self.assert_all()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/3190")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Guest User: Verify loyalty point earned for Pickup total under 20$ "
                  "calculates to 1$ = 1point with total points round off to the nearest whole number")
    @allure.description("""Given guest user is on homepage ​
        When user click on Select Address​
        And user clicks on Pickup button​
        When user enter the address and select address from suggestion​
            | address | 1000 MacDougal Street New York |
        Then verify user navigates to locations page​
        When user clicks the "View Menu" button on a store
        Then verify home page with available menu options specific to store should be displayed
        When user clicks a product with total under 20$
            | product | Whole milk |
        And click "Add to Order"
        And user clicks the cart icon
        Then verify points earned total is calculated based on the condition for order total under $20""")
    def test_3190_pickup_loyalty_under_20(self):
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
        product_obj.select_product_quantity(3)
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj.click_cart_btn(3)
        points = product_obj.get_loyalty_points_text()
        self.soft_assert(self.assertGreaterEqual, int(
            points.split()[2]), 0, "Loyalty points not updated")
        self.assert_all()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/3191")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Guest User: Verify loyalty point earned for Pickup total above 20$ "
                  "calculates to 1$ = 1.25 point with total points round off to the nearest whole number")
    @allure.description("""Given guest user is on homepage ​
        When user click on Select Address​
        And user clicks on Pickup button​
        When user enter the address and select address from suggestion​
            | address | 1000 MacDougal Street New York |
        Then verify user navigates to locations page​
        When user clicks the "View Menu" button on a store
        Then verify home page with available menu options specific to store should be displayed
        When user clicks a product with total above 20$
            | product | 100 cookies |
        And click "pick for me"
        And click "Add to Order"
        And user clicks the cart icon
        Then verify points earned total is calculated based on the condition for order total above $20""")
    def test_3191_pickup_loyalty_above_20(self):
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
        points = product_obj.get_loyalty_points_text()
        self.soft_assert(self.assertGreaterEqual, int(
            points.split()[2]), 0, "Loyalty points not upated")
        self.assert_all()
