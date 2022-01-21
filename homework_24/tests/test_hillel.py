def test_check_autorization_with_valid_data(autorization_page):
    autorisation = autorization_page.make_autorization()

    assert 'QA Automation Python' in autorisation.get_title()
