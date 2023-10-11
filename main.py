import time
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

username = os.getenv("LT_USERNAME")  # Replace the username
access_key = os.getenv("LT_ACCESS_KEY")  # Replace the access key
build_name = os.getenv("LT_BUILD_NAME")
# username = "rupamd"
# access_key = "g8bSPewKA2UPOBkcfGMcv1Vmc8N9CM11gIDUUyL9q9a8OpxUwc"

class FirstSampleTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions();
        options.browser_version = "117.0"
        # options.platform_name = "macOS Sonoma";
        lt_options = {};
        lt_options["platformName"]="macOS Sonoma";
        lt_options["username"] = "rupamd";
        lt_options["accessKey"] = "g8bSPewKA2UPOBkcfGMcv1Vmc8N9CM11gIDUUyL9q9a8OpxUwc";
        lt_options["project"] = "Untitled";
        lt_options["w3c"] = True;
        lt_options["plugin"] = "python-python";
        lt_options["build"] = build_name;
        lt_options["name"] = "rupamd";
        lt_options["tunnel"] = True;
        # lt_options["tunnelName"] = os.getenv("LT_TUNNEL_NAME");
        # lt_options["tunnelName"] = "rupamd";
        options.set_capability('LT:Options', lt_options);

        self.driver = webdriver.Remote(
            command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key),
            options=options)

# tearDown runs after each test case

    def tearDown(self):
        self.driver.quit()

    # """ You can write the test cases here """
    def test_demo_site(self):

        # try:
        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        driver.set_window_size(1920, 1080)

        # driver.get("file:///C:/Users/")
        # driver.implicitly_wait(20)

        # driver.get("http://localhost:8000/")
        # driver.implicitly_wait(20)

        # Url
        print('Loading URL')
        driver.get("https://stage-lambda-devops-use-only.lambdatestinternal.com/To-do-app/index.html")

        # Let's click on a element
        driver.find_element(By.NAME, "li1").click()
        location = driver.find_element(By.NAME, "li2")
        location.click()
        print("Clicked on the second element")
        time.sleep(60)

        #Take Smart UI screenshot
        #driver.execute_script("smartui.takeScreenshot")

        # Let's add a checkbox
        driver.find_element(By.ID, "sampletodotext").send_keys("LambdaTest")
        add_button = driver.find_element(By.ID, "addbutton")
        add_button.click()
        print("Added LambdaTest checkbox")

        # print the heading
        search = driver.find_element(By.CSS_SELECTOR, ".container h2")
        assert search.is_displayed(), "heading is not displayed"
        print(search.text)
        search.click()
        driver.implicitly_wait(80)

        # Let's download the invoice
        heading = driver.find_element(By.CSS_SELECTOR, ".container h2")
        if heading.is_displayed():
            heading.click()
            driver.execute_script("lambda-status=passed")
            print("Tests are run successfully!")
        else:
            driver.execute_script("lambda-status=failed")


if __name__ == "__main__":
    unittest.main()
