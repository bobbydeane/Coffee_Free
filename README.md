# Caffeine Free Club

Caffeine Free Club is a website where users come together to be inspired to limit or quit Coffee/Caffeine. The site is built using the Django Framework in python.

![Site Preview](https://res.cloudinary.com/bobdean/image/upload/v1649661888/RESPONSIVE_vgpbqd.png)


Live app link can be found [here](https://coffee-free.herokuapp.com/)

# User Experience

***


## User Stories
1. As a Admin I would like to be abel to...
    1.1 Have an Admin area to the site
    1.2 Creat draft posts.
    1.3 Publish Posts, and comments

2. A a User I would like to be able to...
    2.1 Register on the site using my username, email and password.
    3.2 View all posts on the site
    4.3 View Comments on the site
    5.4 View Posts by Category on the site

1. A a Logged in User I would like to be able to...
    3.1 Create a Blog Post
    3.2 Like a Blog Post
    4.3 Leave Comments on the site
    5.4 Edit and Delete my Posts

## 1. Strategy

 - ### Project Goal
 Create a site that allows users to get support and motivation to quit Caffeine through the site community and Blog Posts.

## 2. Scope
- Simple, functional Blog Site
- explicit content
- Site is easily Navigated
- Appealing on Mobile devices.

# Functional Scope

***
### Caffeine Free Flow chart

![Flow Chart](https://res.cloudinary.com/bobdean/image/upload/v1649661887/flow_chart_jode9d.png)


### Caffeine Free Diagram Entity Relationship

![DER](https://res.cloudinary.com/bobdean/image/upload/v1649661887/Schema_kpxtou.png)

### Agile Methodology

All development and functioanlity of this project were managed using [Github](https://github.com/bobbydeane/Coffee_Free/projects/1).

## 3. Structure

- The site has a simple layout to ensure intuitive navigation.
- Forms are straightfoward an easy to understand
- Edit, update and delete forms are easy to use


## 4. Skeleten

This site was created with Balsamic wireframes and took the style from a Bootstrap template.

### Homepage
![Homepage](https://res.cloudinary.com/bobdean/image/upload/v1649661888/Hompage_ya7kzm.png)
### Index
![Index](https://res.cloudinary.com/bobdean/image/upload/v1649661888/Edit_dpo6f0.png)
### Categories
![Categories](https://res.cloudinary.com/bobdean/image/upload/v1649661888/Categories_h0y4zi.png)

### Edit
![Edit](https://res.cloudinary.com/bobdean/image/upload/v1649661888/Edit_dpo6f0.png)


## 5. Surface

The Blog is a stripped down version of a Bootstrap [Blog](https://getbootstrap.com/docs/4.0/examples/blog/) template.

# Existing Features

***

Login and Register User buttons are present on the navbar if the user is not logged.
Logout and Submit a Post buttons are present if the user is logged.
The Logged in User can also Edit/ and Delete their post.

![Home](https://res.cloudinary.com/bobdean/image/upload/v1649661888/Home_ww877z.png)

The Home page list the posts via Category and Creation date so user can browse for a post to read or comment on.

![Index](https://res.cloudinary.com/bobdean/image/upload/v1649661888/indexmain_edsx6l.png)

The User can click on a blog post from the list and open the blog. The post will be displayed and the logged in USer can comment or like the post. The post will display likes and comments.

![Blog](https://res.cloudinary.com/bobdean/image/upload/v1649661887/Blog_o3adwv.png)

If the user has submited a Post, they will then be able to retrieve and edit the post via a form.

![Edit](https://res.cloudinary.com/bobdean/image/upload/v1649661887/Editpost_rsjs0v.png)


# Future Features
***
I would like to 
    1. Create a User profile page, so that users can display bio and profile pic.
    2. Add an API to automatically pull relevant news stories to the site.
    3. Let users Upvote and downvote Posts/Comments.

# Languages Used
***
Python 3.0
HTML
CSS
JS
Django Frameworks

# Frameworks, Libraries & Programmes Used
***
- GitHub: GitHub is used to store the project's code after being pushed from Git.
- Django: Framework used to add structure to the platform.
- Gitpod: was used as a CLI/Code editor.
- Balsamiq: used to create the wireframes during the design process.
- Lucidchart: used to create Database schema diagram and flow chart diagram.
- Font Awesome: Used to add icons to the Blog posts.

# Testing and Code validation
***

## Automated Tests
***
Automated tests were carried out using Djangos testing functionality.
The tests looked at the Python files in the App to validate the code. The Coverage repost can be found int he htmlcov folder in the app.
![Tests](https://res.cloudinary.com/bobdean/image/upload/v1649661888/Coverage_iqryub.png)

Other Functionality tests  were carried out by the User:
    -test that forms display as expected
    -form submission reacts with Models as expected
    - Test that unathorised user cannot edit/delete a post.
    -Test that unathorised user cannot comment/like a post.
    
Html Tests using - https://validator.w3.org/nu/
CSS testing - https://jigsaw.w3.org/css-validator/
Python Testing - http://www.pep8online.com/

# Credits
***

## Media
***
 - All Images were found on Google images.

## Work based on other Code
***
[Codemy](https://www.youtube.com/channel/UCFB0dxMudkws1q8w5NJEAmw) was used as a guide to develop CRUD functionality for Blog Posts
Stack Overflow was valuable in troubleshoiting many issues.

[Bootstrap Templates](https://getbootstrap.com/docs/4.0/examples/blog/) and documentation was used for the HTML and styling of the majority of the site.

[Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) was used for many of the forms on the site.

[Summernote](https://github.com/summernote/django-summernote) was used to style the admin site and forms 

## Acknowledgements
***

- Codemy for getting me through some tricky code implementation
- Code Institute Slack Community for the support and time
- Stackoverflow for the lifeline when i'm struggling

I would also like to thank:
- Rahul, my mentor. For keeping me within my project scope and boosting morale.
- Code Institute for this opporuntity.
- Caragh & Ban.



