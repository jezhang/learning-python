from splinter import Browser
                    
with Browser() as browser: 
    # Visit URL 
    url = "http://www.baidu.com" 
    browser.visit(url) 
    browser.fill('wd', 'splinter - python acceptance testing for web applications') 
    # Find and click the 'search' button 
    button = browser.find_by_id('su') 
    # Interact with elements 
    button.click()     
    if browser.is_text_present('splinter.cobrateam.info'): 
        # browser.click_link_by_href('http://www.baidu.com/link?url=nNIqRwCn4-_fTFExsH27u5orKpw4ABPHxleO031e97_MN0NSh9YcbIufSP-xefHdhMzzALviHa564cXNn4Wn6K')
        # browser.click_link_by_partial_text('splinter 0.5.4 documentation')
        browser.click_link_by_partial_text('documentation')
        print "Yes, the official website was found!" 
    else: 
        print "No, it wasn't found... We need to improve our SEO techniques"