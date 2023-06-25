import pytest
import Utilities.CustomLogger as cl
import logging
import softest
import Static.Constants as const
import time
import allure
from Utilities.PageBase import PageBase

log = cl.customLogger(logging.INFO)

val = ''


@pytest.mark.usefixtures('create_resource')
class TestShipGuestNative(softest.TestCase):
    '''
    Test Class for Order Logged In Page
    '''

    def test_single_item_order_ship(self):
        self.home_obj.select_address(const.location_page)
        login_obj = self.home_obj.click_hamburger_menu()
        login_obj.click_ship_cookies()
        product_obj = self.home_obj.click_add_ship_product()
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order()
        checkout_obj = self.home_obj.click_checkout_btn()
        checkout_obj.click_review_order_btn()

    def test_ship_order_multiple_products(self):
        self.home_obj.select_address(const.location_page)
        login_obj = self.home_obj.click_hamburger_menu()
        login_obj.click_ship_cookies()
        product_obj = self.home_obj.click_add_ship_product()
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order()
        login_obj.click_ship_cookies()
        product_obj = self.home_obj.click_add_ship_product()
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order()
        checkout_obj = self.home_obj.click_checkout_btn()
        checkout_obj.click_review_order_btn()

    def test_ship_order_fedEx_homeDel(self):
        self.home_obj.select_address(const.location_page)
        login_obj = self.home_obj.click_hamburger_menu()
        login_obj.click_ship_cookies()
        product_obj = self.home_obj.click_add_ship_product()
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order()
        checkout_obj = self.home_obj.click_checkout_btn()
        checkout_obj.click_review_order_btn()

    def test_remove_all_items_ship(self):
        self.home_obj.select_address(const.location_page)
        login_obj = self.home_obj.click_hamburger_menu()
        login_obj.click_ship_cookies()
        product_obj = self.home_obj.click_add_ship_product()
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order()
        self.home_obj.click_boxes_btn()
        product_obj = self.home_obj.click_single_item_product()
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order()
        checkout_obj = self.home_obj.click_checkout_btn()
        checkout_obj.click_remove_item_btn()
        checkout_obj.click_remove_item_btn()
        flag2 = checkout_obj.verify_empty_cart_banner()
        self.soft_assert(self.assertTrue, flag2, "Your cart is empty")
        self.assert_all()

    def test_remove_single_item_ship(self):
        self.home_obj.select_address(const.location_page)
        login_obj = self.home_obj.click_hamburger_menu()
        login_obj.click_ship_cookies()
        product_obj = self.home_obj.click_add_ship_product()
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order()
        self.home_obj.click_boxes_btn()
        product_obj = self.home_obj.click_single_item_product()
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order()
        checkout_obj = self.home_obj.click_checkout_btn()
        checkout_obj.click_remove_item_btn()
        flag2 = checkout_obj.verify_review_order_btn()
        self.soft_assert(self.assertTrue, flag2)
        self.assert_all()

    def gift_for_someone_else_CC_ship(self):
        self.home_obj.select_address(const.location_page)
        login_obj = self.home_obj.click_hamburger_menu()
        login_obj.click_ship_cookies()
        product_obj = self.home_obj.click_add_ship_product()
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order()
        checkout_obj = self.home_obj.click_checkout_btn()
        checkout_obj.click_review_order_btn()
