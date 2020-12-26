import random
import time
import pytest

from driver_setup import setup_driver, teardown_driver
from settings import WEBDRIVER_TYPE, BAT_END, BAT_NAME, MOLE_START, MOLE_NAME, MOLE_END, DOG_NAME, DOG_START, DOG_END, \
    CAT_START, CAT_NAME, CAT_END, TIGER_START, TIGER_NAME, TIGER_END, HAWK_START, HAWK_NAME, HAWK_END, ROBOT_START, \
    ROBOT_NAME, TIMER_START, ENG_URL, SWE_URL
from page_objects import GamePage


@pytest.fixture(scope='session', autouse=True)
def run_before_and_after_tests():
    """Fixture to execute asserts before and after a test is run"""
    # Setup: fill with any logic you want
    global driver
    driver = setup_driver(WEBDRIVER_TYPE)

    yield # this is where the testing happens

    teardown_driver(driver)


@pytest.mark.smoke
@pytest.mark.positive
def test_fin():
    page = GamePage(driver)
    page.go_to_site()
    assert page.find_logo()


@pytest.mark.smoke
@pytest.mark.positive
def test_eng():
    page = GamePage(driver)
    page.go_to_site(ENG_URL)
    assert page.find_logo()


@pytest.mark.smoke
@pytest.mark.positive
def test_swe():
    page = GamePage(driver)
    page.go_to_site(SWE_URL)
    assert page.find_logo()


@pytest.mark.positive
def test_score_match():
    expected_score = random.randint(1, 10)
    page = GamePage(driver)
    page.go_to_site()
    for score in range(expected_score):
        page.click_right_square()
    assert page.score_value() == expected_score


@pytest.mark.positive
def test_bat():
    page = GamePage(driver)
    page.go_to_site()
    for score in range(BAT_END):
        page.click_right_square()
    assert page.result_value().lower() == BAT_NAME.lower()


@pytest.mark.positive
def test_mole_from():
    page = GamePage(driver)
    page.go_to_site()
    for score in range(MOLE_START):
        page.click_right_square()
    assert page.result_value().lower() == MOLE_NAME.lower()


@pytest.mark.positive
def test_mole_till():
    page = GamePage(driver)
    page.go_to_site()
    for score in range(MOLE_END):
        page.click_right_square()
    assert page.result_value().lower() == MOLE_NAME.lower()


@pytest.mark.positive
def test_dog_from():
    page = GamePage(driver)
    page.go_to_site()
    for score in range(DOG_START):
        page.click_right_square()
    assert page.result_value().lower() == DOG_NAME.lower()


@pytest.mark.positive
def test_dog_till():
    page = GamePage(driver)
    page.go_to_site()
    for score in range(DOG_END):
        page.click_right_square()
    assert page.result_value().lower() == DOG_NAME.lower()


@pytest.mark.positive
def test_cat_from():
    page = GamePage(driver)
    page.go_to_site()
    for score in range(CAT_START):
        page.click_right_square()
    assert page.result_value().lower() == CAT_NAME.lower()


@pytest.mark.positive
def test_cat_till():
    page = GamePage(driver)
    page.go_to_site()
    for score in range(CAT_END):
        page.click_right_square()
    assert page.result_value().lower() == CAT_NAME.lower()


@pytest.mark.positive
def test_tiger_from():
    page = GamePage(driver)
    page.go_to_site()
    for score in range(TIGER_START):
        page.click_right_square()
    assert page.result_value().lower() == TIGER_NAME.lower()


@pytest.mark.positive
def test_tiger_till():
    page = GamePage(driver)
    page.go_to_site()
    for score in range(TIGER_END):
        page.click_right_square()
    assert page.result_value().lower() == TIGER_NAME.lower()


@pytest.mark.positive
def test_hawk_from():
    page = GamePage(driver)
    page.go_to_site()
    for score in range(HAWK_START):
        page.click_right_square()
    assert page.result_value().lower() == HAWK_NAME.lower()


@pytest.mark.positive
def test_hawk_till():
    page = GamePage(driver)
    page.go_to_site()
    for score in range(HAWK_END):
        page.click_right_square()
    assert page.result_value().lower() == HAWK_NAME.lower()


@pytest.mark.positive
def test_robot_from():
    page = GamePage(driver)
    page.go_to_site()
    for score in range(ROBOT_START):
        page.click_right_square()
    assert page.result_value().lower() == ROBOT_NAME.lower()


@pytest.mark.positive
def test_best_result_inc():
    page = GamePage(driver)
    page.go_to_site()
    best_result = random.randint(1, 10)
    for score in range(best_result):
        page.click_right_square()
    assert page.best_result() == best_result
    page.play_again()
    new_best_result = best_result + 1
    for score in range(new_best_result):
        page.click_right_square()
    assert page.best_result() == new_best_result


@pytest.mark.positive
def test_best_result_dec():
    page = GamePage(driver)
    page.go_to_site()
    best_result = random.randint(2, 10)
    for score in range(best_result):
        page.click_right_square()
    assert page.best_result() == best_result
    page.play_again()
    new_best_result = best_result - 1
    for score in range(new_best_result):
        page.click_right_square()
    assert page.best_result() == best_result


@pytest.mark.positive
def test_timer_run():
    page = GamePage(driver)
    page.go_to_site()
    assert page.timer_run() == TIMER_START
    page.click_right_square()
    time.sleep(random.randint(1, 10))
    assert page.timer_run() < TIMER_START


@pytest.mark.positive
def test_timer_rerun():
    page = GamePage(driver)
    page.go_to_site()
    page.click_right_square()
    time.sleep(random.randint(1, 10))
    page.click_right_square()
    assert page.timer_run() == TIMER_START


@pytest.mark.negative
def test_wrong_click():
    page = GamePage(driver)
    page.go_to_site()
    page.click_wrong_square()
    assert page.timer_run() == TIMER_START


@pytest.mark.negative
def test_timer_decrease():
    page = GamePage(driver)
    page.go_to_site()
    page.click_right_square()
    timer_start = page.timer_run()
    page.click_wrong_square()
    page.click_wrong_square()
    timer_after = page.timer_run()
    assert timer_start - timer_after >= 3


@pytest.mark.negative
def test_penalty_match():
    expected_penalty = random.randint(1, 4)
    page = GamePage(driver)
    page.go_to_site()
    page.click_right_square()
    for score in range(expected_penalty):
        page.click_wrong_square()
    time.sleep(1)
    assert page.penalty_value() == expected_penalty

