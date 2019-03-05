class selectlist:
     def agino_ption_value(self,tag_name,option_text,element_id):
        element_id= self.opdriver.driver.find_element_by_xpath(element_id)
        tag_name=element_id.find_elements_by_tag_name(tag_name)
        for option in tag_name:
            # print ("Value is: " + option.get_attribute("value"))
            # print ("Text is:" +option.text)
            if option_text in option.text:
                select_value=option.get_attribute("value")
                print ("option_textoption_textoption_textValue is: " + select_value)
                option_text.click()
                break