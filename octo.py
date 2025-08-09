from seleniumbase import SB

with SB(uc=True, test=True) as octoc:

    url = "https://kick.com/brutalles"
    octoc.uc_open_with_reconnect(url, 4)
    octoc.sleep(4)
    octoc.uc_gui_click_captcha()
    octoc.sleep(1)
    octoc.uc_gui_handle_captcha()
    octoc.sleep(4)
    if octoc.is_element_present('button:contains("Accept")'):
        octoc.uc_click('button:contains("Accept")', reconnect_time=4)
    if octoc.is_element_visible('#injected-channel-player'):
        octoc2 = octoc.get_new_driver(undetectable=True)
        octoc2.uc_open_with_reconnect(url, 5)
        octoc2.uc_gui_click_captcha()
        octoc2.uc_gui_handle_captcha()
        octoc.sleep(10)
        if octoc2.is_element_present('button:contains("Accept")'):
            octoc2.uc_click('button:contains("Accept")', reconnect_time=4)
        while octoc.is_element_visible('#injected-channel-player'):
            octoc.sleep(10)
        octoc.quit_extra_driver()
    octoc.sleep(1)
