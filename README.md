# uts-chinese-website-ui-test
<div align="center">
  <img height="400" src="https://i.imgur.com/s0CDqF5.png" />

   <br>
  <small> <b><i>Show your support!</i> </b></small>
  <br>
   <a href="https://github.com/MarketingPipeline/Python-Selenium-Action">
    <img title="Star on GitHub" src="https://img.shields.io/github/stars/MarketingPipeline/Python-Selenium-Action.svg?style=social&label=Star">
  </a>
  <a href="https://github.com/MarketingPipeline/Python-Selenium-Action/fork">
    <img title="Fork on GitHub" src="https://img.shields.io/github/forks/MarketingPipeline/Python-Selenium-Action.svg?style=social&label=Fork">
  </a>
   </p>  
 
 


   
 
No need to struggle to figure out how to run a Python Selenium script with a  [GitHub Action](https://github.com/features/actions). 
  This is a <b>ready to use</b> template for running Selenium with Python via [GitHub Actions](https://github.com/features/actions) on non-headless. <br> 
</div>



## Example and usage


To use <b><i>Github Action</b></i>:

- Push/merge any code to the main branch and it will run the tests on the UTS website on Github Actions

- Make changes as needed to the Python script <code>utilities.py</code>. 

- Make changes as needed to the <code>selenium-action.yaml</code> file. For Github actions.

## Runthrough Breakdown
1. It will first check whether the website has a valid certificate by checking whether the URL starts with 'https://'
2. NOTE: The page may take a long time to render. Tests won't start until the image at the top of the website is fully rendered. 
3. First it will click through the first 4 blue dots to browse through the articles
4. Simply hover down to the video below those buttons
5. It will click on the "Faculty and Course" section in blue under the video previously. Hint: It has these chinese words: 院系
6. Wait until the page is fully loaded then it will click on the contact form button (联系我们)
7. This page will load a form and it will use the fill_survey() to complete the form (it will not be submitted)
8. This will fill out everything on the form and will dabble on some of the dropdown bars.
9. Then it will go back to the home page to click on the "World Rankings" section (Hint: It has these chinese words: 排名)
10. Then it will click on the "Course Pathways" sidebar at the top of the page (Hint: It has these chinese words: 入读)
11. Then it will click on the "How to Apply" sidebar next to the "Course Pathways" sidebar (申请指南)
12. Then it will click on the "News" sidebar next to the "How to Apply" sidebar (UTS新闻)
13. Then it will click on the search icon right at the top of the page to search for "uts"
14. Then it will go back to the home page via the UTS icon at the top left of the page
<br>

## Demo(s) 
An example of the script sucessfully running on GitHub:
- [Successful Action Run](https://github.com/uts-itd/uts-chinese-website-ui-test/actions/runs/5150335458)


## Branches:
- main, selenium-grid: Run tests on Selenium Grid
  
## Contributing

Want to improve this? Create a pull request with detailed changes / improvements! If approved you will be added to the list of contributors of this awesome project!



See also the list of
[contributors](https://github.com/uts-itd/uts-chinese-website-ui-test/graphs/contributors) who
participate in this project.


